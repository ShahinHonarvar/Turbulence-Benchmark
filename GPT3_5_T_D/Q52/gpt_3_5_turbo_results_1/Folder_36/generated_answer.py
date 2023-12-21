
def palindrome_of_length_n(string):
    s = string.lower()
    length = len(s)
    palindromes = set()
    for i in range(length - 337):
        substring = s[i:i + 338]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
