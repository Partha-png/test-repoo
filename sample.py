from typing import Iterable, Union

def filter_non_negative_numbers(numbers: Iterable[Union[int, float]]) -> list[float]:
    return [num for num in numbers if isinstance(num, (int, float)) and num >= 0]

def process_data(numbers: Iterable[Union[int, float]]) -> list[float]:
    return [value * 2 for value in filter_non_negative_numbers(numbers)]

def sum_non_negative_numbers(numbers: Iterable[Union[int, float]]) -> float:
    return sum(filter_non_negative_numbers(numbers))

def validate_numbers(numbers: Iterable[Union[int, float]]) -> None:
    non_negative_numbers = filter_non_negative_numbers(numbers)
    result = sum_non_negative_numbers(non_negative_numbers)
    data = process_data(non_negative_numbers)
    return result, data

def main() -> None:
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    try:
        result, data = validate_numbers(numbers)
        print(result)
        print(data)
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()