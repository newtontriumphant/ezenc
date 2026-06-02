#!/usr/bin/env python3
from __future__ import annotations
import sys, os, re, base64, hashlib, signal, platform
import urllib.parse
__version__ = "1.0.2"

# i love ascii generators i should make a tui one of those next!

LOGO = r"""
  ___ ____ ___ _  _  ___ 
 | __|_  /| __| \| |/ __|
 | _| / / | _||  ` | (__ 
 |___/___||___|_|\_|\___| 
 encode / decode anything!
"""

def out(*args, **kwargs):
    kwargs.setdefault("flush", True)
    print(*args, **kwargs)

def pr(text, end="\n"):
    print(text, end=end, flush=True)

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

clear_screen()
print(LOGO)