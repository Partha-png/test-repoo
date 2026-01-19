# data_processor.py - Test file with various code quality issues

import os
import sys
import json
import time  # Unused imports

class DataProcessor:
    def __init__(self, data, config, settings, options, flags):  # Too many parameters
        self.data = data
        self.config = config
        self.settings = settings
        self.options = options
        self.flags = flags
        self.temp = None  # Unused attribute
    
    def process(self, input_data):
        """Process data with multiple issues."""
        result = []
        
        # Deep nesting - bad practice
        if input_data:
            if len(input_data) > 0:
                if isinstance(input_data, list):
                    if input_data[0]:
                        if input_data[0] != "":
                            for item in input_data:
                                if item:
                                    result.append(item.upper())
        
        return result
    
    def calculate(self, a, b, c, d, e, f, g):  # Too many parameters
        """Calculate with complex logic."""
        total = 0
        
        # Should use enumerate
        for i in range(len([a, b, c, d, e, f, g])):
            total += [a, b, c, d, e, f, g][i]
        
        return total
    
    def validate_data(self, data):
        """Validate data - duplicate code."""
        if data is None:
            return False
        if data == "":
            return False
        if data == []:
            return False
        if data == {}:
            return False
        return True
    
    def transform(self, items):
        """Transform items - inefficient."""
        new_items = []
        for i in range(len(items)):  # Should use enumerate
            new_items.append(items[i] * 2)
        return new_items

# Global variables - bad practice
GLOBAL_COUNTER = 0
GLOBAL_DATA = []

def helper_function(x, y, z, a, b, c, d, e):  # Too many parameters
    """Helper with too many params."""
    return x + y + z + a + b + c + d + e
