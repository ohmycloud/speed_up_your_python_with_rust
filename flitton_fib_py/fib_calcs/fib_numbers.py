from typing import List
from .flib_number import recurring_fibonacci_number

def calculate_numbers(numbers: List[int]) -> List[int]:
    return [recurring_fibonacci_number(number=1) for i in numbers]
