from typing import List, Union

def extract_positive_numbers(numbers: List[Union[int, float]]) -> list[float]:
    try:
        return [num for num in numbers if num > 0]
    except TypeError:
        raise ValueError("Input list must contain numbers")

def process_data(data: List[Union[int, float]]) -> list[float]:
    return [value * 2 for value in data]

def calculate_sum_of_positive_numbers(numbers: List[Union[int, float]]) -> float:
    positive_numbers = extract_positive_numbers(numbers)
    if not positive_numbers:
        raise ValueError("No positive numbers found in the list")
    return sum(positive_numbers)

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