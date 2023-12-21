
def palindrome_of_length_at_least_n(string, n):
    # Create a list of all palindromes in the string
    palindromes = []
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr == substr[::-1]:
            palindromes.append(substr)
    return set(palindromes)
