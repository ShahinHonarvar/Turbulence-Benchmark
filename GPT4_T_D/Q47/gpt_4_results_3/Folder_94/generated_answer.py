
def palindromes_of_specific_lengths(s):
    s = s[40:95]
    s = s.lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + 45, min(len(s), i + 52)):
            substring = s[i:j]
            if not substring.isalpha():
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
