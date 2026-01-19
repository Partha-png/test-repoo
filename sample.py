def calculate_sum(a, b, c, d, e, f, g, h):  # Too many parameters!
    """Calculate sum of numbers."""
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:  # Deep nesting - bad!
                    if e > 0:
                        if f > 0:
                            return a + b + c + d + e + f + g + h
    return 0

import os  # Unused import
import sys  # Unused import

x = 10  # Unused variable

def process_data(data):
    result = []
    for i in range(len(data)):  # Should use enumerate
        result.append(data[i] * 2)
    return result
