
def palindrome_of_length_n(string):
    string = string.lower()
    string = ''.join(filter(str.isalpha, string))
    n = 181
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
