from dataclasses import dataclass
from typing import Iterable, Union

@dataclass
class Number:
    value: Union[int, float, str]

    @staticmethod
    def parse(num: Union[int, float, str]) -> 'Number':
        try:
            return Number(float(num))
        except (ValueError, TypeError):
            raise ValueError("Invalid numeric value")

class Calculator:
    @classmethod
    def process_numbers(cls, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        numbers = [cls.Number.parse(n) for n in numbers if isinstance(n, (int, float, str)) or n == '']
        return sum(n.value for n in numbers), [n.value for n in numbers]

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)