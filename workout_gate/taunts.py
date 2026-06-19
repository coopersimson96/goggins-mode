"""The gate's running commentary during a challenge - GOGGINS MODE.

Voice: David Goggins. Raw, hardcore, no-BS, no coddling. Signature beats:
"Stay hard," the 40% rule, "who's gonna carry the boats," "taking souls,"
callus your mind, discipline over motivation, don't die average.

Everything here is just word pools. Nothing else in the app depends on the
exact lines, so fork away. Selection is deterministic (indexed by rep count /
target) so the line holds steady between reps instead of flickering
frame-to-frame - readable on video.
"""

# Shown rep by rep as you grind through the set. Indexed by reps DONE, so a
# fresh jab lands on every rep. Keep them short - one line, fits the bubble.
GRIND = [
    "STAY HARD. Get down there.",
    "You think you're done? You're at 40 percent.",
    "Who's gonna carry the boats? Not you at this pace.",
    "This is the easy part. MOVE.",
    "I'm taking your soul one rep at a time.",
    "Comfortable? Wrong answer. Go deeper.",
    "Nobody's coming to save you. PUSH.",
    "That's not tired. That's soft. Again.",
    "Callus your mind. One more.",
    "You don't stop when you're tired. You stop when you're DONE.",
    "Be obsessed. To the point it scares people.",
    "Motivation's gone. Good. Discipline. Move.",
    "The pain IS the point. Eat it.",
    "Average dies right here. Not today.",
    "Get after it. No excuses, no exceptions.",
    "Stay hard. Don't you dare slow down.",
]

# count == 0: nothing done yet, you're stalling.
WAITING = [
    "You opened the laptop but not your legs. Get DOWN.",
    "Nobody cares that you don't feel like it. MOVE.",
    "The prompt waits. I wait. Forever. Get after it.",
    "Stop staring. Hit the floor. STAY HARD.",
]

# done == target - 1: last rep coming up.
ALMOST = [
    "One more. Take its soul.",
    "Last rep. Don't you half-ass it.",
    "Finish it. That's who carries the boats.",
]

# Body not detected.
CANT_SEE = [
    "Can't see you. Hiding is for the soft. In frame, NOW.",
    "Step up. The camera's not the problem. You are.",
    "You vanished right when it got hard. Typical. Back in frame.",
]

# Shown on the GET-IN-POSITION countdown.
ANNOUNCE = [
    "No warmup excuses. Get after it.",
    "Time to callus your mind. Move.",
    "Who's gonna carry the boats? You. Right now.",
    "Stay hard. Let's go to work.",
]

# Shown on the green VALIDATED screen.
VALIDATED = [
    "Soul taken. Prompt unlocked. Stay hard.",
    "That was 40 percent. Remember that. Cleared.",
    "Logged. Don't you dare get comfortable.",
    "Good. Now stay obsessed. Back to work.",
]

# Shown on the pick-your-pain choice screen.
CHOICE = "Pick your pain. Either way, you're carrying the boats."


def _pick(pool, seed):
    """Deterministic choice so a line is stable for a whole challenge but
    varies between challenges. `seed` is usually the target rep count."""
    return pool[seed % len(pool)]


def grind_line(done: int, target: int) -> str:
    """The bubble line for the live HUD, given progress."""
    if done <= 0:
        return _pick(WAITING, target)
    if target > 1 and done >= target - 1:
        return _pick(ALMOST, target)
    return GRIND[done % len(GRIND)]


def cant_see_line(target: int) -> str:
    return _pick(CANT_SEE, target)


def announce_line(target: int) -> str:
    return _pick(ANNOUNCE, target)


def validated_line(seed: int = 0) -> str:
    return _pick(VALIDATED, seed)
