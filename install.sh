#!/usr/bin/env bash
# Goggins Mode installer: venv + deps + pose model + the /goggins command + config.
#   ./install.sh            -> gate active in this folder
#   ./install.sh --global   -> gate active in ALL your Claude Code sessions
set -euo pipefail
cd "$(dirname "$0")"

MODEL_URL="https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_full/float16/1/pose_landmarker_full.task"

echo "==> Creating virtualenv..."
python3 -m venv .venv

echo "==> Installing dependencies (mediapipe, opencv)..."
.venv/bin/pip install -q -r requirements.txt

if [ ! -f models/pose_landmarker_full.task ]; then
  echo "==> Downloading pose model (~9 MB)..."
  mkdir -p models
  curl -sL -o models/pose_landmarker_full.task "$MODEL_URL"
fi

echo "==> Running tests..."
.venv/bin/python -m unittest discover -s tests >/dev/null 2>&1 && echo "    all green"

echo "==> Installing the /goggins command..."
mkdir -p "$HOME/.claude/commands"
cp commands/goggins.md "$HOME/.claude/commands/goggins.md"

echo "==> Applying Goggins config (lunges + thrusters + burpees, random, every 40 min)..."
PY=".venv/bin/python"
"$PY" -m workout_gate enable lunges        >/dev/null
"$PY" -m workout_gate enable goblet_press  >/dev/null
"$PY" -m workout_gate enable burpees       >/dev/null
"$PY" -m workout_gate disable pushups      >/dev/null
"$PY" -m workout_gate disable squats       >/dev/null
"$PY" -m workout_gate set reps lunges 15 15        >/dev/null
"$PY" -m workout_gate set reps goblet_press 15 15  >/dev/null
"$PY" -m workout_gate set reps burpees 15 15       >/dev/null
"$PY" -m workout_gate set mode random      >/dev/null
"$PY" -m workout_gate set time 40          >/dev/null

if [ "${1:-}" = "--global" ]; then
  echo "==> Installing globally (all Claude Code sessions)..."
  "$PY" -m workout_gate global on
fi

if [ -t 0 ] && [ "${1:-}" != "--no-setup" ]; then
  "$PY" -m workout_gate setup
else
  cat <<'EOF'

Done. Goggins mode is configured: lunges / thrusters / burpees, 15 reps,
one challenge at most every 40 min. Run /goggins in Claude Code to start.
EOF
fi
