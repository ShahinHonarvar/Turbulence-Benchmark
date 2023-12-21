
def palindrome_of_length_at_least_n(string, n):
    # Find all palindromes of length greater than or equal to n in the given string
    palindromes = set()
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
