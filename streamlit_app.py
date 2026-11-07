"""
ScamShield AI - Streamlit Community Cloud Root Launcher
======================================================
Self-healing launcher that automatically detects and handles both
structured and flat GitHub repository layouts.
"""

import os
import sys
import shutil

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# File lists for self-healing flat repo structure
challenge_files = [
    "evaluate_submission.py", "leaderboard.py", "leaderboard.json",
    "sample_submission.csv", "submission.csv", "submission_advanced.csv",
    "baseline_submission.py", "advanced_submission.py",
    "benchmark_analysis.py", "benchmark_metrics.json"
]
model_files = ["scamshield_model.joblib"]
data_files = [
    "train.csv", "val.csv", "test_ground_truth.csv", "test_unlabeled.csv"
]

# 1. Ensure src/ directory exists & populated with all python modules
src_dir = os.path.join(ROOT_DIR, "src")
if not os.path.exists(src_dir):
    os.makedirs(src_dir, exist_ok=True)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

init_src = os.path.join(src_dir, "__init__.py")
if not os.path.exists(init_src):
    with open(init_src, "w", encoding="utf-8") as f:
        f.write("")

# Copy all root python modules into src/ so both flat and package imports work
for item in os.listdir(ROOT_DIR):
    item_path = os.path.join(ROOT_DIR, item)
    if os.path.isfile(item_path) and item.endswith(".py") and item != "streamlit_app.py":
        dst_path = os.path.join(src_dir, item)
        if not os.path.exists(dst_path):
            try:
                shutil.copy2(item_path, dst_path)
            except Exception:
                pass

# 2. Ensure challenge/ directory exists & populated
challenge_dir = os.path.join(ROOT_DIR, "challenge")
if not os.path.exists(challenge_dir):
    os.makedirs(challenge_dir, exist_ok=True)
init_challenge = os.path.join(challenge_dir, "__init__.py")
if not os.path.exists(init_challenge):
    with open(init_challenge, "w", encoding="utf-8") as f:
        f.write("")
for f in challenge_files:
    src_path = os.path.join(ROOT_DIR, f)
    dst_path = os.path.join(challenge_dir, f)
    if os.path.exists(src_path) and not os.path.exists(dst_path):
        try:
            shutil.copy2(src_path, dst_path)
        except Exception:
            pass

# 3. Ensure models/ directory exists & populated
model_dir = os.path.join(ROOT_DIR, "models")
if not os.path.exists(model_dir):
    os.makedirs(model_dir, exist_ok=True)
for f in model_files:
    src_path = os.path.join(ROOT_DIR, f)
    dst_path = os.path.join(model_dir, f)
    if os.path.exists(src_path) and not os.path.exists(dst_path):
        try:
            shutil.copy2(src_path, dst_path)
        except Exception:
            pass

# 4. Ensure data/ directory exists & populated
data_dir = os.path.join(ROOT_DIR, "data")
if not os.path.exists(data_dir):
    os.makedirs(data_dir, exist_ok=True)
for f in data_files:
    src_path = os.path.join(ROOT_DIR, f)
    dst_path = os.path.join(data_dir, f)
    if os.path.exists(src_path) and not os.path.exists(dst_path):
        try:
            shutil.copy2(src_path, dst_path)
        except Exception:
            pass

# Locate master app script
if os.path.exists(os.path.join(src_dir, "app.py")):
    APP_PATH = os.path.join(src_dir, "app.py")
elif os.path.exists(os.path.join(ROOT_DIR, "app.py")):
    APP_PATH = os.path.join(ROOT_DIR, "app.py")
else:
    raise FileNotFoundError(f"Could not locate app.py in {ROOT_DIR} or {src_dir}.")

# Execute main dashboard app
with open(APP_PATH, "r", encoding="utf-8") as f:
    code = f.read()

exec(compile(code, APP_PATH, "exec"), globals())
