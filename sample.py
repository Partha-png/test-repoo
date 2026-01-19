from typing import Union

def filter_positive_numbers(numbers: list[Union[int, float]]) -> list[float]:
    return [num for num in numbers if isinstance(num, (int, float)) and num > 0]

def process_data(data: list[Union[int, float]]) -> list[float]:
    return [value * 2 for value in data if isinstance(value, (int, float))]

def sum_positive_numbers(numbers: list[Union[int, float]]) -> float:
    return sum(num for num in numbers if isinstance(num, (int, float)) and num > 0) or 0

def main() -> None:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    try:
        result = sum_positive_numbers(numbers)
        print(result)
        print(process_data(numbers))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()