
def palindrome_of_length_n(str):
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        for j in range(i+66, len(str)+1):
            substring = str[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
