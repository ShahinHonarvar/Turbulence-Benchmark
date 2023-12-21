
import re

def palindrome_of_length_at_least_n(string, n):
    # Check if the input string is valid
    if not isinstance(string, str) or len(string) == 0:
        raise ValueError("Invalid input string")

    # Check if the input length is valid
    if not isinstance(n, int) or n < 1:
        raise ValueError("Invalid input length")

    # Create a regular expression to match palindromes of length at least n
    pattern = r"(?i)(?=(.{" + str(n) + r"}))"

    # Use the re module to find all matches in the input string
    matches = re.findall(pattern, string)

    # Return the set of palindromes found
    return set(matches)
