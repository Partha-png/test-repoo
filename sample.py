from typing import List, Union

def extract_positive_numbers(numbers: List[Union[int, float]]) -> list[float]:
    try:
        return [num for num in numbers if isinstance(num, (int, float)) and num > 0]
    except Exception as e:
        raise ValueError("Input list must contain numbers") from e

def process_data(data: List[Union[int, float]]) -> list[float]:
    return [value * 2 for value in data if isinstance(value, (int, float))]

def calculate_sum_of_positive_numbers(numbers: List[Union[int, float]]) -> float:
    try:
        positive_numbers = [num for num in numbers if num > 0]
        return sum(positive_numbers)
    except Exception as e:
        raise ValueError("No positive numbers found in the list") from e

def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    try:
        result = calculate_sum_of_positive_numbers(numbers)
        print(result)
        print(process_data(numbers))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()