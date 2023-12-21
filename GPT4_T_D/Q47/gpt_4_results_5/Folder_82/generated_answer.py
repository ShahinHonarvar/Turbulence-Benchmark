
def palindromes_of_specific_lengths(s):
    s = s[3:301].lower()
    palindromes = set()
    for len_p in range(30, 301):
        for i in range(len(s) - len_p + 1):
            substring = s[i:i+len_p]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
