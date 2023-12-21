
def palindrome_of_length_n(string):
    palindromes = set()
    n = 401
    for i in range(len(string) - n + 1):
        substring = string[i:i+n].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
