# MODULE NAME: utils_funs_driver.py

# IMPORTS
from util_funs import *

# Test decorator usage
@timer_decorator
def process_data(n):
    """Simulates a heavy computation task."""
    total = 0
    for i in range(n):
        total += i
    return total

# Run the function
result = process_data(10_000_000)

###
# Test timeit usage
def sample_function():
    return sum(i for i in range(1000))

# Measure how long it takes to run the function 10,000 times
execution_time = timeit.timeit(sample_function, number=10000)
print(f"Total time for 10,000 executions: {execution_time:.6f} seconds")


###
# Make sure this module is executed
if __name__ != '__main__':
    print("The module named util_funs_driver.py is intended to be executed and not imported.")
