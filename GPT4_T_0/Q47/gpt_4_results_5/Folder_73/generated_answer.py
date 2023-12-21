
def palindromes_of_specific_lengths(s):
    s = s[21:63]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+22, min(i+34, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
