from dataclasses import dataclass
from typing import Iterable, Union, TypeAlias, Tuple

@dataclass(frozen=True)
class Number:
    value: Union[int, float]

    @classmethod
    def parse(cls, num: Union[int, float, str]) -> 'Number':
        try:
            return cls(float(num))
        except (ValueError, TypeError):
            raise ValueError("Invalid numeric value") from None

class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> Tuple[float, list[float]]:
        parsed_numbers = (self._parse_number(n) for n in numbers if isinstance(n, (int, float, str)) and n != '')
        return sum(n.value for n in parsed_numbers), list(n.value for n in parsed_numbers)

    def _parse_number(self, num: Union[int, float, str]) -> 'Number':
        try:
            return Number(float(num))
        except (ValueError, TypeError):
            raise ValueError("Invalid numeric value") from None

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)