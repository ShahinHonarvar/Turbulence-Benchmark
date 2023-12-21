
def palindrome_of_length_n(string):
    from re import finditer

    string = string.lower()
    length = 416
    palindromes = set()

    for i in range(len(string) - length + 1):
        substring = string[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)

    return palindromes
