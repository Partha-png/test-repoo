from dataclasses import dataclass
from typing import Iterable, Protocol, Union

class Number(Protocol):
    def to_float(self) -> float:
        pass

@dataclass
class Calculator:
    def process_numbers(self, numbers: Iterable[Number]) -> list[float]:
        return [num.to_float() for num in numbers if isinstance(num, (int, float))]

    def sum_non_negative_numbers(self, numbers: Iterable[Number]) -> float:
        return sum(num.to_float() for num in numbers if isinstance(num, (int, float)) and num.to_float() >= 0)

    def validate_numbers(self, numbers: Iterable[Number]) -> tuple[float, list[float]]:
        processed_numbers = self.process_numbers(numbers)
        non_negative_sum = self.sum_non_negative_numbers(numbers)
        return non_negative_sum, processed_numbers

def main() -> None:
    calculator = Calculator()
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    result, data = calculator.validate_numbers(numbers)
    print(result)
    print(data)

if __name__ == "__main__":
    main()