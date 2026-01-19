from dataclasses import dataclass
from typing import Iterable, Protocol, Union

class Number(Protocol):
    def to_float(self) -> float: ...

def is_number(num: object) -> bool:
    return isinstance(num, (int, float))

def to_float(num: Union[int, float, str]) -> float:
    return num if is_number(num) else float(num)

def process_numbers(numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
    floats = [to_float(num) for num in numbers]
    return sum(num for num in floats if num >= 0), floats

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