# MODULE NAME:  util_funs.py

# IMPORTS
import functools
import time
import timeit

""" This section contains two different versions/ways to measure the
    execution time of functions or code snippits.    
    
    1. CUSTOM DECODRATOR
    The most flexible and industry-standard way to time a Python function 
    is by using a decorator with time.perf_counter(). This method provides 
    the highest precision for measuring execution time and allows you to 
    reuse the timing logic across multiple functions without modifying their 
    core code. This approach measures the CPU usage time of the function. 
    See https://www.youtube.com/watch?v=FblABqaKz_U), or 
     (https://www.youtube.com/shorts/TfccynZoF-c), or
    (https://stackoverflow.com/questions/14452145/how-to-measure-time-taken-between-lines-of-code-in-python)
    
    2. BUILT-IN timeit MODULE 
    If you need to benchmark a small code block or a quick function snippet 
    repeatedly to account for system fluctuations, the built-in timeit module 
    is ideal. This measures the wallclock execution time of a function, which 
    may not be exactly the same as the CPU execution time.
    See (https://docs.python.org/3/library/timeit.html), or 
        (https://pymotw.com/3/timeit/)
"""

# CUSTOM DECODER: timer_decorator
def timer_decorator(func):
    """A decorator that prints the execution time of a function."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Start the high-precision performance counter
        start_time = time.perf_counter()

        # Execute the actual function
        result = func(*args, **kwargs)

        # Calculate elapsed time
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Save the time for later
        wrapper.last_elapsed = execution_time

        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds.")
        return result
    
    return wrapper


###
# Make sure this module is imported
if __name__ == '__main__':
    print("The module named util_funs.py is intended to be imported and not executed.")
