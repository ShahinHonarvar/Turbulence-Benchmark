
def palindrome_of_length_n(string):
    # Case-insensitive search for palindromes of length n
    palindromes = []
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if substr == substr[::-1]:
            palindromes.append(substr)
    return set(palindromes)
