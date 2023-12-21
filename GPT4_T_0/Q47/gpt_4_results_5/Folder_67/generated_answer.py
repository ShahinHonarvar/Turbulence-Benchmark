
def palindromes_of_specific_lengths(s):
    s = s[65:100].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+26, min(i+34, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
