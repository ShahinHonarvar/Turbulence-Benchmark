
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    n = len(string)
    for i in range(n - 6):
        substring = string[i:i+7]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
