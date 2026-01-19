from dataclasses import dataclass
from typing import Iterable, Union

class Number:
    @staticmethod
    def to_float(num: Union[int, float, str]) -> float:
        return float(num) if isinstance(num, (int, float, str)) else 0.0

def is_number(num: object) -> bool:
    return isinstance(num, (int, float, str))

@dataclass
class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        return sum(Number.to_float(num) for num in numbers if is_number(num)), [
            Number.to_float(num) for num in numbers if is_number(num)
        ]

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)