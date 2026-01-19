from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Iterable, Protocol, Union

class Number(Protocol):
    @abstractmethod
    def to_float(self) -> float:
        pass

@dataclass
class Calculator:
    def process_data(self, numbers: Iterable[Number]) -> list[float]:
        return [num.to_float() * 2 for num in numbers]

    def sum_non_negative_numbers(self, numbers: Iterable[Number]) -> float:
        return sum(num.to_float() for num in numbers if num.to_float() >= 0)

    def validate_numbers(self, numbers: Iterable[Number]) -> tuple[float, list[float]]:
        non_negative_numbers = self.filter_non_negative_numbers(numbers)
        return self.sum_non_negative_numbers(non_negative_numbers), self.process_data(non_negative_numbers)

    def filter_non_negative_numbers(self, numbers: Iterable[Number]) -> list[float]:
        return [num.to_float() for num in numbers if isinstance(num, (int, float)) and num >= 0]

def main() -> None:
    calculator = Calculator()
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    try:
        result, data = calculator.validate_numbers(numbers)
        print(result)
        print(data)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()