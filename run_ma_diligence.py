"""
Run the M&A Diligence Lite swarm against the synthetic deal memo and data room
(Card B — M&A Diligence Lite).

Inlines the deal memo and all data room documents into the user message.
Streams events so you can watch the parallel thread fan-out — this is the demo.

Saves the final transcript and any produced files to outputs/.

Usage:
    python run_ma_diligence.py
"""

import os
from pathlib import Path

from anthropic import Anthropic


DEAL_MEMO_PATH = Path("synthetic-data/deal-memo-horizon-analytics.md")
DATA_ROOM_DIR = Path("synthetic-data/data-room")
OUTPUT_DIR = Path("outputs")


def load_inputs_as_context() -> str:
    blocks = []

    if not DEAL_MEMO_PATH.exists():
        raise SystemExit(f"Deal memo not found: {DEAL_MEMO_PATH}")
    print(f"  including {DEAL_MEMO_PATH.name}")
    blocks.append(
        f"=====  DEAL MEMO: {DEAL_MEMO_PATH.name}  =====\n{DEAL_MEMO_PATH.read_text()}"
    )

    if DATA_ROOM_DIR.exists():
        for doc in sorted(DATA_ROOM_DIR.glob("*.md")):
            print(f"  including data room: {doc.name}")
            blocks.append(
                f"=====  DATA ROOM: {doc.name}  =====\n{doc.read_text()}"
            )
    else:
        print(f"  WARNING: {DATA_ROOM_DIR} not found — running with deal memo only")

    return "\n\n".join(blocks)


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY before running.")

    coordinator_id_path = Path(".ma_coordinator_id")
    environment_id_path = Path(".environment_id")

    if not coordinator_id_path.exists():
        raise SystemExit(
            "Missing .ma_coordinator_id. Run create_ma_specialists.py, "
            "upload_ma_skills.py, then create_ma_coordinator.py first."
        )
    if not environment_id_path.exists():
        raise SystemExit(
            "Missing .environment_id. Run setup_environment.py first."
        )

    coordinator_id = coordinator_id_path.read_text().strip()
    environment_id = environment_id_path.read_text().strip()

    client = Anthropic()

    print("Loading deal memo + data room documents...")
    context = load_inputs_as_context()

    print(f"\nStarting diligence session against coordinator {coordinator_id}...")
    session = client.beta.sessions.create(
        agent=coordinator_id,
        environment_id=environment_id,
        title="M&A Diligence — Project Horizon",
    )
    Path(".ma_last_session_id").write_text(session.id)

    user_message = (
        "A deal memo and data room have just been shared for Project Horizon "
        "(target: Horizon Analytics Ltd). Please run a full diligence sweep:\n\n"
        "1. Read the deal memo yourself and form an initial view.\n"
        "2. Delegate to all four specialists in parallel. Each specialist should apply "
        "their skill framework and return a structured assessment.\n"
        "3. Synthesise all four assessments into a single diligence memo.\n"
        "4. Produce the memo as a Word document (using the docx skill if available; "
        "otherwise as structured markdown). The memo must be investment-committee-ready.\n\n"
        "Specialists have their domain skills attached. Move efficiently — the IC "
        "presentation is tomorrow.\n\n"
        f"{context}"
    )

    print("\n=== EVENT STREAM (this is the demo) ===\n")
    final_text_parts: list[str] = []

    with client.beta.sessions.events.stream(session.id) as stream:
        client.beta.sessions.events.send(
            session.id,
            events=[
                {
                    "type": "user.message",
                    "content": [{"type": "text", "text": user_message}],
                }
            ],
        )
        for event in stream:
            t = event.type
            if t == "session.thread_created":
                print(f"  [thread spawned]   {event.agent_name}", flush=True)
            elif t == "session.thread_status_running":
                name = getattr(event, "agent_name", "?")
                print(f"  [thread running]   {name}", flush=True)
            elif t == "agent.thread_message_received":
                print(f"  [reply ←]          {event.from_agent_name}", flush=True)
            elif t == "agent.thread_message_sent":
                print(f"  [delegate →]       {event.to_agent_name}", flush=True)
            elif t == "agent.message":
                for block in event.content:
                    if getattr(block, "type", None) == "text":
                        final_text_parts.append(block.text)
                        print(block.text, end="", flush=True)
            elif t == "agent.tool_use":
                print(f"\n  [tool: {getattr(event, 'name', '?')}]", flush=True)
            elif t == "session.status_idle":
                print("\n\n[diligence swarm finished]")
                break

    OUTPUT_DIR.mkdir(exist_ok=True)
    transcript_path = OUTPUT_DIR / "ma-diligence-transcript.txt"
    transcript_path.write_text("".join(final_text_parts))
    print(f"\nCoordinator transcript saved to {transcript_path}")

    print("\nDownloading deliverables from the session container...")
    files = client.beta.files.list(
        scope_id=session.id,
        betas=["managed-agents-2026-04-01"],
    )
    file_count = 0
    for f in files.data:
        out_path = OUTPUT_DIR / f.filename
        print(f"  {f.filename}  ->  {out_path}")
        content = client.beta.files.download(f.id)
        content.write_to_file(str(out_path))
        file_count += 1

    if file_count == 0:
        print("  (no files found — agents may have produced text-only output)")
    else:
        print(f"\nDownloaded {file_count} file(s) to {OUTPUT_DIR}/")

    print(f"\nView the full session (including all sub-agent threads) at:")
    print(f"  https://platform.claude.com/sessions/{session.id}")


if __name__ == "__main__":
    main()
