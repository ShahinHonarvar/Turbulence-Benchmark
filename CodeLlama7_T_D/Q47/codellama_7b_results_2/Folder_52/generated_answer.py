
def palindromes_of_specific_lengths(string, start=44, end=99):
    # Create a list of all substrings in the specified range
    substrings = []
    for i in range(start, end + 1):
        substring = string[i]
        if substring.isalpha():
            substrings.append(substring)
    # Create a set of all palindromes found in the list of substrings
    palindromes = set()
    for substring in substrings:
        if len(substring) >= 13 and len(substring) <= 42:
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
