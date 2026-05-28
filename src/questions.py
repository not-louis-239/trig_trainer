import random
import math
from enum import Enum
from typing import Literal, Callable
from dataclasses import dataclass

EVAL_EPSILON = 10 ** -6

MARKING_NS: dict[str, Callable[[float], float] | float] = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "sqrt": math.sqrt,
    "pi": math.pi,
}

class TrigFunc(Enum):
    SIN = math.sin
    COS = math.cos
    TAN = math.tan

@dataclass
class Question:
    direction: Literal[-1, 1]  # 1 = forward, -1 = inverse
    trig_func: TrigFunc
    is_radians: bool
    input_value: int | float         # holds angle for fwd, or ratio value for inverse
    true_value: float          # right answer

ANGLES: list[int] = [0, 30, 45, 60]

def gen_question() -> Question:
    func = random.choice(list(TrigFunc))
    angle_degrees = random.choice(ANGLES)
    angle_rad = math.radians(angle_degrees)

    direction = random.choice([-1, 1])
    is_radians = random.choice((True, False))

    # Calculate the trig ratio (e.g., sin(30) = 0.5)
    trig_ratio = func.value(angle_rad)

    i_val, o_val = (angle_rad if is_radians else angle_degrees), trig_ratio

    if direction == 1:
        input_value, true_value = i_val, o_val
    else:
        input_value, true_value = o_val, i_val

    assert direction in (-1, 1), "direction must be -1 or 1"

    return Question(
        direction=direction,
        is_radians=is_radians,
        trig_func=func,
        input_value=input_value,
        true_value=true_value
    )

def mark(user_input: str, q: Question) -> bool:
    try:
        # Explicitly blocking __builtins__ secures eval() from malicious text injection
        result = eval(user_input, globals={"__builtins__": None}, locals=MARKING_NS)
        return abs(result - q.true_value) < EVAL_EPSILON
    except (SyntaxError, NameError):
        # Don't penalise typos, raise instead so the caller
        # has a chance to catch it and accept another user input
        raise
    except Exception:
        return False
