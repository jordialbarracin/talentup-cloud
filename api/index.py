import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BACKEND_DIR = os.path.join(ROOT_DIR, "02_ENGINEERING", "backend")
AGENTS_DIR = os.path.join(ROOT_DIR, "03_AGENTS")

for p in (BACKEND_DIR, AGENTS_DIR, ROOT_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

from main import app
