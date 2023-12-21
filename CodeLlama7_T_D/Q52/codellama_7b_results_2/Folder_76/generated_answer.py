
def palindrome_of_length_n(string, length=257):
    # Create a list of all substrings of the given string
    substrings = []
    for i in range(len(string) - length + 1):
        substrings.append(string[i:i+length])
    # Create a set of all palindromes of the specified length
    palindromes = set()
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
