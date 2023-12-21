
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 39):
        substring = string[i:i+40]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
