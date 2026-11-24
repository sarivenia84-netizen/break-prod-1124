import os
import sys
from pathlib import Path


def main() -> int:
    base = Path(__file__).resolve().parent
    try:
        excuse = (base / "excuse.txt").read_text(encoding="utf-8").strip()
        if not excuse:
            print("error: excuse.txt is empty", file=sys.stderr)
            return 1
        out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or (base / "output"))
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "entry.txt").write_text(excuse + "\n", encoding="utf-8")
        return 0
    except Exception as exc:  # noqa: BLE001 - report any failure to stderr
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
