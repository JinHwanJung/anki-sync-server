import os
import sys

sys.path.insert(0, "/usr/share/anki")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), "anki-bundled"))


if __package__ is None and not hasattr(sys, "frozen"):
    import os.path
    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))
