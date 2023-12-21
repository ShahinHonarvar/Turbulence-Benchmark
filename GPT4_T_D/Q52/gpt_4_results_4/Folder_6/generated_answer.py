
def palindrome_of_length_n(str):
    str = str.lower()
    palindromes = set()
    length = len(str)
    for i in range(length):
        for j in range(i + 474, length + 1):
            substring = str[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
