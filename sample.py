import math
from typing import List, Union

def calculate_positive_sum(numbers: List[Union[int, float]]) -> float:
    positive_numbers = [num for num in numbers if num > 0]
    if not positive_numbers:
        raise ValueError("No positive numbers found in the list")
    return sum(positive_numbers)

def process_data(data: List[Union[int, float]]) -> List[Union[int, float]]:
    return [value * 2 for value in data]

def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    try:
        result = calculate_positive_sum(numbers)
        print(result)
        print(process_data(numbers))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()