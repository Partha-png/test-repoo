from dataclasses import dataclass
from typing import Iterable, Union

@dataclass(frozen=True)
class Number:
    value: float

    @classmethod
    def parse(cls, num: Union[int, float, str]) -> 'Number':
        try:
            return cls(float(num))
        except (ValueError, TypeError):
            raise ValueError("Invalid numeric value") from None

class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        return self._process_numbers(numbers)

    def _process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        parsed_numbers = (Number.parse(n) for n in numbers if isinstance(n, (int, float, str)) and n != '')
        return sum(n.value for n in parsed_numbers), [n.value for n in parsed_numbers]

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)