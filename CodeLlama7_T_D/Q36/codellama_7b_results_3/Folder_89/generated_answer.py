
def filter_chars(string):
    # Find the indices of the first and last characters in the range
    start = string.index('5') + 1
    end = string.index('W') - 1
    # Create a new string with all occurrences of characters within the range removed
    filtered_string = ''.join([c for c in string if not (start <= ord(c) <= end)]))
    return filtered_string
