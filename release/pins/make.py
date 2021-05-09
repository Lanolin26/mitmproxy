#!/usr/bin/env python3
import platform
import re
import subprocess
from pathlib import Path

here = Path(__file__).parent
outfile = (here / f"requirements-{platform.system().lower()}.txt").absolute()

if __name__ == "__main__":
    subprocess.check_call([
        "pip-compile",
        "--generate-hashes", "--upgrade", "--allow-unsafe",
        "-o", outfile,
        "requirements.in",
    ], cwd=here)

    out = outfile.read_bytes()
    out = re.sub(b"-e .+", b"# --- line removed by make.py ---", out)
    out = re.sub(b"pip-compile --.+", b"./make.py  (on the same platform)", out)
    outfile.write_bytes(out)
