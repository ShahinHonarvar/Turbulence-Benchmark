
def palindrome_of_length_n(strings):
    palindromes = set()
    strings = strings.lower()
    length = len(strings)
    for i in range(length):
        for j in range(i+16, length+1):
            substring = strings[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
