
def palindrome_of_length_n(string):
    # Remove all non-letter characters from the string
    string = ''.join(c for c in string if c.isalpha())
    # Find all palindromes of length n in the string
    palindromes = []
    for i in range(len(string) - 278):
        substring = string[i:i+279]
        if substring == substring[::-1]:
            palindromes.append(substring)
    return set(palindromes)
