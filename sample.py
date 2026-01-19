from dataclasses import dataclass
from typing import Iterable, Protocol, Union, Tuple

class Number(Protocol):
    def to_float(self) -> float: ...

class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> Tuple[float, list[float]]:
        processed = [num.to_float() for num in numbers if isinstance(num, (int, float))]
        non_negative_sum = sum(num.to_float() for num in numbers if isinstance(num, (int, float)) and num.to_float() >= 0)
        return non_negative_sum, processed

class NumberProcessor(Calculator):
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> Tuple[float, list[float]]:
        return super().process_numbers(numbers)

def main() -> None:
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)