import math
from typing import List, Union

def calculate_positive_sum(numbers: List[Union[int, float]]) -> float:
    return sum(num for num in numbers if num > 0)

def process_data(data: List[Union[int, float]]) -> List[Union[int, float]]:
    return [value * 2 for value in data]

def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(calculate_positive_sum(numbers))
    print(process_data(numbers))

if __name__ == "__main__":
    main()