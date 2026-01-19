from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable, Union, Tuple

class ParseError(Exception):
    pass

class ParseType(Enum):
    FLOAT = 1
    INT = 2
    STR = 3

@dataclass(frozen=True)
class Number:
    value: float
    type: ParseType

    @classmethod
    def from_value(cls, num: Union[int, float, str]) -> 'Number':
        try:
            if isinstance(num, (int, float)):
                return cls(float(num), ParseType.FLOAT)
            elif isinstance(num, str):
                return cls(float(num), ParseType.STR)
            else:
                raise ValueError("Invalid number type")
        except ValueError as e:
            raise ParseError(f"Invalid numeric value: {num}") from e

class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> Tuple[float, list[float]]:
        parsed_numbers = self.parse_numbers(numbers)
        return self._process_parsed_numbers(parsed_numbers)

    def parse_numbers(self, numbers: Iterable) -> Iterable[Number]:
        for num in numbers:
            try:
                yield Number.from_value(num)
            except ParseError as e:
                raise e

    def _process_parsed_numbers(self, numbers: Iterable[Number]) -> Tuple[float, list[float]]:
        return sum(n.value for n in numbers), sorted(n.value for n in numbers, reverse=True)

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    try:
        result, data = processor.process_numbers(numbers)
        print(result)
        print(data)
    except (ValueError, TypeError, ParseError) as e:
        print(f"Error: {e}")