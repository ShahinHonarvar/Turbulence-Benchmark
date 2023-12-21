
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    palindrome_length = 72
    for i in range(len(string) - palindrome_length + 1):
        substring = string[i:i+palindrome_length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
