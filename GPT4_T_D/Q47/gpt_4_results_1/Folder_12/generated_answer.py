
def palindromes_of_specific_lengths(s):
    s = s[62:89]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if 18 <= len(sub) <= 21 and sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes
