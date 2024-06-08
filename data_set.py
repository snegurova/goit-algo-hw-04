"""Module providing a function generating random data."""
import random

def generate_random_data(size):
    """Function generating random data"""
    return [random.randint(0, 100000) for _ in range(size)]
