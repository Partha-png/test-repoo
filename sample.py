from dataclasses import dataclass
from typing import Iterable, Protocol, Union, Tuple

class Number(Protocol):
    def to_float(self) -> float:
        ...

@dataclass
class Calculator:
    def process_numbers(self, numbers: Iterable[Number]) -> list[float]:
        return [num.to_float() for num in numbers if isinstance(num, (int, float))]

    def sum_non_negative_numbers(self, numbers: Iterable[Number]) -> float:
        return sum(num.to_float() for num in numbers if isinstance(num, (int, float)) and num.to_float() >= 0)

    def validate_numbers(self, numbers: Iterable[Number]) -> Tuple[float, list[float]]:
        return self._validate_and_process_numbers(numbers)

    def _validate_and_process_numbers(self, numbers: Iterable[Number]) -> Tuple[float, list[float]]:
        processed = self.process_numbers(numbers)
        non_negative_sum = sum(num.to_float() for num in numbers if isinstance(num, (int, float)) and num.to_float() >= 0)
        return non_negative_sum, processed

def main() -> None:
    calculator = Calculator()
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    result, data = calculator.validate_numbers(numbers)
    print(result)
    print(data)

if __name__ == "__main__":
    main()