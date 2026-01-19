from typing import List, Union

def filter_numbers(numbers: List[Union[int, float]]) -> list[float]:
    """Filters positive numbers from a list."""
    return [num for num in numbers if isinstance(num, (int, float)) and num > 0]

def process_data(data: List[Union[int, float]]) -> list[float]:
    """Doubles all numbers in a list."""
    return [value * 2 for value in data if isinstance(value, (int, float))]

def sum_positive_numbers(numbers: List[Union[int, float]]) -> float:
    """Calculates the sum of positive numbers in a list."""
    positive_numbers = filter_numbers(numbers)
    if positive_numbers:
        return sum(positive_numbers)
    raise ValueError("No positive numbers found in the list")

def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    try:
        result = sum_positive_numbers(numbers)
        print(result)
        print(process_data(numbers))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()