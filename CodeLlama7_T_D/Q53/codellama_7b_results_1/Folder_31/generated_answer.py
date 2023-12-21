
import re

def palindrome_of_length_at_least_n(s, n):
    # Use regular expressions to find all palindromes of length greater than or equal to n
    pattern = r"([a-z])(\1){2,}"
    return {word for word in re.findall(pattern, s, flags=re.IGNORECASE) if len(word) >= n}
