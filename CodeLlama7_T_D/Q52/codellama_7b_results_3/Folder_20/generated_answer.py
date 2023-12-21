 def palindrome_of_length_n(string):
    # Find all substrings of the given string
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    # Filter out non-palindromes and return the result
    palindromes = [s for s in substrings if s == s[::-1]]
    return set(palindromes)
