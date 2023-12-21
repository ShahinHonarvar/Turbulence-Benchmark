
def palindrome_of_length_n(string):
    # Split the input string into substrings of length n
    substrings = []
    for i in range(0, len(string), n):
        substrings.append(string[i:i+n])
    # Filter out non-palindromes and return the result
    palindromes = [s for s in substrings if s == s[::-1]]
    return palindromes
