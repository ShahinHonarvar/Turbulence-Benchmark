
def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string = ''.join(filter(str.isalpha, string))
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+13, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
