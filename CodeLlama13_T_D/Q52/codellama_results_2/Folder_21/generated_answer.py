
def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 407 + 1):
        substr = string[i:i+407]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes
