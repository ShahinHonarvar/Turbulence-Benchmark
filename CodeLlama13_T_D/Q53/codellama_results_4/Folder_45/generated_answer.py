
def palindrome_of_length_at_least_n(string, n):
    palindromes = set()
    for i in range(len(string)):
        substr = string[i:i+n]
        if len(substr) < n:
            continue
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
