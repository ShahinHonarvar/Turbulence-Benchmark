
import re

def palindrome_of_length_at_least_n(string, n):
    # Use regular expressions to find all palindromes
    # in the given string that have a length of at least n.
    pattern = r"(?i)(?=[\w\W]{%d})[\w]*[\w][\w]*" % (n)
    matches = re.findall(pattern, string)
    # Return an empty set if no palindromes were found.
    return set(matches) or set()
