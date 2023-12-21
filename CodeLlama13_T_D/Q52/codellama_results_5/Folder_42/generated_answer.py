
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 279 + 1):
        substr = string[i:i+279]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
