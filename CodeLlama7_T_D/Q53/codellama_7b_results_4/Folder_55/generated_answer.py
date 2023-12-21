
def palindrome_of_length_at_least_n(s, n):
    # Find all substrings of length greater than or equal to n in the given string s
    substrings = [s[i:j+1] for i in range(len(s)) for j in range(i, len(s))]
    # Filter out substrings that are not palindromes
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
