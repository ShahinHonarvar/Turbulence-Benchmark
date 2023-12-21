
def palindromes_of_specific_lengths(s):
    s = s[200:301]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(10, 51):
            substring = s[i:i+j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
