
import re

def palindrome_of_length_at_least_n(string, n):
    # Define a regular expression that matches all palindromes of length greater than or equal to n
    pattern = r"(\w{n})|(\w{n}\W+\w{n})|(\w{n}\W+[\w\W]{n-1}\W+\w{n})"
    # Use the regular expression to find all palindromes in the given string
    return set(re.findall(pattern, string))
