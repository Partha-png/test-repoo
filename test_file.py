import json

class DataProcessor:
    def __init__(self, data, config):
        self.data = data
        self.config = config
        self.temp_data = None
        
    def process(self, input_data):
        return [item.upper() for item in input_data if item]
    
    def calculate(self, numbers):
        return sum(numbers)
    
    def is_valid_data(self, data):
        return data is not None and data != "" and data != [] and data != {}
    
    def transform(self, items):
        return [item * 2 for item in items]


GLOBAL_COUNTER = 0
GLOBAL_DATA = []

def helper_function(*args):
    return sum(args)