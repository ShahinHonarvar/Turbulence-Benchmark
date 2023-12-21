
def palindromes_of_specific_lengths(s):
    s = s[11:98]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+29, i+63):
            if j <= len(s):
                substring = s[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes.add(substring.lower())
    return palindromes
