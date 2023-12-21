
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length - 8):
        substring = string[i:i+9]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
