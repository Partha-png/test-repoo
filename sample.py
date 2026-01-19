import math

def calculate_sum(numbers):
    """Calculate sum of numbers."""
    return sum(num for num in numbers if num > 0)

def process_data(data):
    return [value * 2 for value in data]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(calculate_sum(numbers))
print(process_data(numbers))