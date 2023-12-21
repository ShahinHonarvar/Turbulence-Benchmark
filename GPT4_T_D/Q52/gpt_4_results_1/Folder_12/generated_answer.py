
def palindrome_of_length_n(str):
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        if i + 23 <= len(str):
            substring = str[i:i+23]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
