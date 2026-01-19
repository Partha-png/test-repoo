from dataclasses import dataclass
from typing import Iterable, Protocol, Union

class Number(Protocol):
    def to_float(self) -> float: ...

def is_number(num: object) -> bool:
    return isinstance(num, (int, float, str)) or num == ''

def to_float(num: Union[int, float, str]) -> float:
    return float(num)

def process_numbers(numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
    total = sum(to_float(num) for num in numbers if is_number(num))
    return total, [to_float(num) for num in numbers]

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