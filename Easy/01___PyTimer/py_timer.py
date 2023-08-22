# The aim of the "PyTimer" project is to provide a simple tool for measure and analyze the execution time of code.


import time

# Step 1: Define the decorator
def measure_execution_time(func):
    """
    A decorator function to measure the execution time of a given function.

    This decorator wraps the provided function with timing functionality,
    capturing the start and end times of the function's execution and
    calculating its execution time. 
    Example usage:

        @measure_execution_time
        def example_function():
            # Placeholder code: Replace with the code you want to measure
            for _ in range(5):
                _ = 2 * 2
        example_function()
    """

    # Step 2: Define the inner function (wrapper) that adds timing functionality
    def wrapper(*args, **kwargs):
        try:
            # Step 2.1: Record the current time before executing the function
            start_time = time.time()
            
            # Step 2.2: Call the original function (func) with its provided arguments
            result = func(*args, **kwargs)
            
            # Step 2.3: Record the current time after the function has executed
            end_time = time.time()
            
            # Step 2.4: Calculate the execution time by finding the difference between end and start times
            execution_time = end_time - start_time
            
            # Step 2.5: Print the execution time with 6 decimal places for clarity
            print(f"Execution time: {execution_time:.6f} seconds")
            
            # Step 2.6: Return the result of the original function to maintain its behavior
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            raise e  # Re-raise the exception for further handling
    
    # Step 3: Return the inner function (timed_function) as the modified version of the original function
    return wrapper

# Step 4: Apply the decorator to the function by using the @ symbol
@measure_execution_time
def example_function():
    # Placeholder code: Replace with the code you want to measure
    for _ in range(77777):
        _ = 2 * 2

# Step 5: Run the decorated function within this block
if __name__ == "__main__":
    example_function()



