
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 20):
        for j in range(i + 20, len(string) + 1):
            substring = string[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
