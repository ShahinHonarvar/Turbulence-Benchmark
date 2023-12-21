
def palindromes_of_specific_lengths(s):
    s = s[41:90]
    s = s.lower()
    palindromes = set()
    for length in range(23, 39):
        for index in range(len(s) - length + 1):
            substring = s[index:index+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
