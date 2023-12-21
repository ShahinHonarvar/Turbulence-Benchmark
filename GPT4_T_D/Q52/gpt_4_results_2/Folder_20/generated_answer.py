
def palindrome_of_length_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = 53
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + length, min(len(s) + 1, i + length + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
