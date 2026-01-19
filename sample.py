from typing import Union, Iterable

def filter_non_negative_numbers(numbers: Iterable[Union[int, float]]) -> list[float]:
    return [num for num in numbers if isinstance(num, (int, float)) and (num >= 0)]

def process_data(data: Iterable[Union[int, float]]) -> list[float]:
    return [value * 2 for value in filter_non_negative_numbers(data)]

def sum_non_negative_numbers(numbers: Iterable[Union[int, float]]) -> float:
    return sum(filter_non_negative_numbers(numbers))

def main() -> None:
    numbers = [1, 2, 3, 'a', 4.5, 6, 7, 8]
    try:
        result = sum_non_negative_numbers(numbers)
        print(result)
        print(process_data(numbers))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()