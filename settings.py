import json
from pathlib import Path
import requests
import os
import base64
import streamlit as st

TITLE = "YT Downloader"

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()


# lotties :
lottie_yt = current_dir / "files" / "yt.json"


def load_lottiefile(filepath : str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
