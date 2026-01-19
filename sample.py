import math

def calculate_positive_sum(numbers):
    """Return the sum of positive numbers in the list."""
    return sum(num for num in numbers if num > 0)

def process_data(data):
    """Double each value in the list."""
    return [value * 2 for value in data]

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    print(calculate_positive_sum(numbers))
    print(process_data(numbers))

if __name__ == "__main__":
    main()