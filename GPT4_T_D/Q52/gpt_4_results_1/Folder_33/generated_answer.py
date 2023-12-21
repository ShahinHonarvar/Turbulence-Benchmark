
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(0, len(string) - 474):
        substring = string[i:i+475]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
