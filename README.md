# Goggins Mode 🪖

> Claude won't let you work until you do your reps.

Goggins Mode turns Claude into a no-mercy drill sergeant. While you work, at random
intervals it **locks your prompts, turns on your webcam, and won't let you keep going
until you finish your reps** — counted live by pose detection, with David-Goggins
trash-talk the whole time. Skip it by closing the tab? The reps follow you.

Built on the excellent [workout-gate](https://github.com/BotchetDig/workout-gate)
by BotchetDig (MIT). Goggins Mode adds: a `/goggins` command, three knee-driven
exercises (lunges, thrusters, burpees), a random / circuit challenge mode, an
end-of-day rep **report**, and the Goggins voice.

## Install

### Quickest (clone + install)
```bash
git clone https://github.com/coopersimson96/goggins-mode.git
cd goggins-mode && ./install.sh --global
```
This sets up everything (venv, deps, pose model), installs the `/goggins` command,
configures the exercises, and runs a 30-second wizard (sizes reps to you + a camera
test so macOS asks for permission now, not mid-prompt).

### Or as a Claude Code plugin
```
/plugin marketplace add coopersimson96/goggins-mode
/plugin install goggins-mode@goggins-mode
```

## Use it

Type **`/goggins`** in Claude Code. The first time, it screens you like a real trainer
(goal, level, which moves it can make you do). After that, just work — at random it'll
lock you and make you earn the next prompt.

```
/goggins            start / set up Goggins mode
workout now         force a challenge right now (and grant the camera)
workout report      today's rep report (per exercise + total + streak)
workout stats       full stats + 7-day chart
workout set time 40 one challenge at most every 40 min (the daily driver)
workout set mode random|choice|circuit   one random | you pick | all of them
workout off         escape hatch (fail-open — you can never lock yourself out)
```

## The exercises

Out of the box Goggins mode enables **lunges, thrusters (goblet squat → press), and
burpees** at 15 reps, picked at random each time. They all use the knee-angle counter
(a rep = full squat down, full stand up). Push-ups and squats are still available
(`workout enable pushups`). Add your own in `workout_gate/detector.py` — one registry
entry, the counter is reused.

> Detection note: lunges and thrusters count cleanly. **Burpees count loosely** (the
> counter catches the squat/stand, not the plank) — finish each with a deep squat +
> full stand so it registers.

## The report

Every rep is recorded. `workout report` prints your day:
```
🏋  GOGGINS REPORT — today's work
   105  burpees
    90  lunges
    75  thrusters
  ------------------
   270  total reps
  🔥 4-day streak
```

## Credit & license

Goggins Mode is a fork of [BotchetDig/workout-gate](https://github.com/BotchetDig/workout-gate).
All credit for the gate engine, pose detection, and Claude Code hook goes to BotchetDig.
[MIT](LICENSE).
