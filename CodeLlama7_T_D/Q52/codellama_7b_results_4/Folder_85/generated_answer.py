
import re

def palindrome_of_length_n(string):
    # Convert the string to lowercase for case-insensitive search
    string = string.lower()

    # Use regular expressions to find all occurrences of palindromes in the given string
    pattern = r"([a-z]*?)\1"
    matches = re.findall(pattern, string)

    # Filter out any matches that are not of the specified length
    filtered_matches = [match for match in matches if len(match[0]) == 46]

    # Return the set of all palindromes of the specified length as substrings of the given string
    return set(filtered_matches)
