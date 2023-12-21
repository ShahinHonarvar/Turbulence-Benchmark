import re
def palindrome_of_length_n(string):
    # Create a set to store the palindromes
    pal = set()
    # Use a regular expression to find all possible palindromes in the string
    for m in re.finditer(r'([a-z]+)(?=\W\1)', string.lower()):
        # Add the matching substring to the set of palindromes
        pal.add(m.group(1))
    # Return the set of palindromes
    return pal
