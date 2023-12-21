
def palindrome_of_length_n(string):
    length = 88
    string = string.lower()
    palindromes = set()

    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if all(c.isalpha() for c in substring) and substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
