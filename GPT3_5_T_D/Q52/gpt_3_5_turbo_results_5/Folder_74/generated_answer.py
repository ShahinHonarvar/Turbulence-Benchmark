
def palindrome_of_length_n(string):
    length = 96
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        substring = string[i:i+length]
        if len(substring) == length and substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
