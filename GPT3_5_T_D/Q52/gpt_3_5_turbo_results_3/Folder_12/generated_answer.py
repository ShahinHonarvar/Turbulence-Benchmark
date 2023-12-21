
def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    n = 23
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
