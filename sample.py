from dataclasses import dataclass
from typing import Iterable, Union

class Number:
    @staticmethod
    def to_float(num: Union[int, float, str]) -> float:
        try:
            return float(num)
        except (ValueError, TypeError):
            return 0.0

def is_number(num: object) -> bool:
    return isinstance(num, (int, float, str))

@dataclass
class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        numbers = [num for num in numbers if is_number(num)]
        return sum(Number.to_float(num) for num in numbers), [Number.to_float(num) for num in numbers]

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)