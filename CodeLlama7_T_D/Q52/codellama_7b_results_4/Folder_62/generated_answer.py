
def palindrome_of_length_n(string):
    # Case-insensitive search for palindromes of length n in the given string
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
