
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i+23, len(string)+1):
            substring = string[i:j]
            if len(substring) == 23 and substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
