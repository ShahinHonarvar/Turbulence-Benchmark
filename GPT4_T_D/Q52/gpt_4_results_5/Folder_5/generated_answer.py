
def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = 17
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
