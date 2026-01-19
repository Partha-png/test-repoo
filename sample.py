from dataclasses import dataclass
from typing import Iterable, Union

class Number:
    def to_float(self) -> float: ...

def is_number(num: object) -> bool:
    return isinstance(num, (int, float, str))

def to_float(num: Union[int, float, str]) -> float:
    return float(num) if isinstance(num, (int, float, str)) else 0.0

@dataclass
class Calculator:
    def process_numbers(self, numbers: Iterable[Union[int, float, str]]) -> tuple[float, list[float]]:
        total, data = 0, []
        for num in numbers:
            if is_number(num):
                total += to_float(num)
                data.append(to_float(num))
        return total, data

class NumberProcessor(Calculator):
    pass

def main() -> None:
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    processor = NumberProcessor()
    result, data = processor.process_numbers(numbers)
    print(result)
    print(data)