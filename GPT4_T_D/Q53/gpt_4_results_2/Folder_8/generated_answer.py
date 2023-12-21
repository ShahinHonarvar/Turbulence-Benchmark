
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    for start in range(length):
        for end in range(start + 45, length+1):
            substring = s[start:end]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
