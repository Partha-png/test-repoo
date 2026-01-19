from dataclasses import dataclass
from typing import Iterable, Union, Type

@dataclass
class Number:
    value: Union[int, float, str]

    @classmethod
    def from_value(cls, num: Union[int, float, str]) -> 'Number':
        try:
            return cls(float(num))
        except (ValueError, TypeError):
            return cls(0.0)

class Calculator:
    @classmethod
    def process_numbers(cls, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        numbers = [cls.Number.from_value(num) for num in numbers if isinstance(num, (int, float, str))]
        return sum(num.value for num in numbers), [num.value for num in numbers]

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)