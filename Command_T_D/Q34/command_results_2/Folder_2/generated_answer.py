import functools
@functools.lru_cache(maxsize=685)
def find_original_set(x):
    # Create an empty set to store the result
    result = set()
    # Iterate through all the elements in the set
    for element in x:
        # Add all the elements to the result set
        result.update(element)
    # Return the result set
    return result
