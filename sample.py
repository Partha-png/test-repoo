from dataclasses import dataclass, field
from typing import Iterable, Union, Tuple

@dataclass(frozen=True)
class Number:
    value: float

    @classmethod
    def from_value(cls, num: Union[int, float, str]) -> 'Number':
        try:
            return cls(float(num or 0))
        except ValueError as e:
            raise ValueError(f"Invalid numeric value: {num}") from e

class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> Tuple[float, list[float]]:
        return self._process_parsed_numbers(self._parse_numbers(numbers))

    def _parse_numbers(self, numbers: Iterable) -> Iterable[Number]:
        if not isinstance(numbers, Iterable):
            raise TypeError("Input must be iterable")
        return (
            Number.from_value(num)
            for num in numbers
            if isinstance(num, (int, float, str)) and num.strip() != ''
        )

    def _process_parsed_numbers(self, numbers: Iterable[Number]) -> Tuple[float, list[float]]:
        return sum((n.value for n in numbers), 0), sorted((n.value for n in numbers), reverse=True)

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)