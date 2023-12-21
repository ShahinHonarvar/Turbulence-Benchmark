
import re

def palindrome_of_length_at_least_n(string, n):
    # Get all palindromes of length greater than or equal to n
    palindromes = re.findall(r"(?=(\w{n})+\1)", string)
    # Return the set of palindromes in a case-insensitive manner
    return set(palindromes)
