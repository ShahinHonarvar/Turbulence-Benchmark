
def palindrome_of_length_n(string, n):
    palindromes = []
    for i in range(len(string)):
        substr = string[i:i+n]
        if substr == substr[::-1]:
            palindromes.append(substr)
    return set(palindromes)
