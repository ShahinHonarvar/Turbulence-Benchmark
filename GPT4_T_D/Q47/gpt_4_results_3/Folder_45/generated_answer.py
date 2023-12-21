
def palindromes_of_specific_lengths(s):
    substring = s[70:141]
    palindromes = set()
    for l in range(60, 2, -1):
        for i in range(len(substring) - l + 1):
            sub = substring[i:i+l]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes
