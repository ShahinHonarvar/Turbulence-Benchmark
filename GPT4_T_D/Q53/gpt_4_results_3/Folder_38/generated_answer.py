
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string = ''.join(c for c in string if c.isalpha())
    palindromes = set()
    length = len(string)

    for i in range(length):
        for j in range(i + 56, length + 1):
            sub = string[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)

    return palindromes
