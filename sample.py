from dataclasses import dataclass
from typing import Iterable, Union, TypeAlias

@dataclass
class Number:
    value: Union[int, float, str]

    @classmethod
    def parse(cls, num: Union[int, float, str]) -> 'Number':
        try:
            return cls(float(num))
        except (ValueError, TypeError) as e:
            raise ValueError("Invalid numeric value") from e

class Calculator:
    @classmethod
    def process_numbers(cls, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        parsed_numbers = (cls.Number.parse(n) for n in numbers if isinstance(n, (int, float, str)) and n != '')
        return sum(n.value for n in parsed_numbers), list(n.value for n in parsed_numbers)

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)