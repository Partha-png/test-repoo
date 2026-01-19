from dataclasses import dataclass
from typing import Iterable, Union

class Number(Protocol):
    def to_float(self) -> float: ...

def is_number(num: object) -> bool:
    return isinstance(num, (int, float))

def to_float(num: Union[int, float, str]) -> float:
    if isinstance(num, str):
        return float(num) if num else 0.0
    return float(num)

def process_numbers(numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
    return sum(to_float(num) for num in numbers if is_number(num)), [
        to_float(num) for num in numbers if is_number(num)
    ]

class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        return process_numbers(numbers)

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)