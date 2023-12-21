
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive matching
    string = string.lower()
    # Find all substrings that match the specified index range and length requirements
    substrings = [substring for substring in string[10:74] if len(substring) >= 6 and len(substring) <= 8 and all(char.isalpha() for char in substring)]
    # Return the set of palindromes found
    return set(substrings)
