
def palindromes_of_specific_lengths(s):
    s = s[39:95]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 14, min(start + 53, len(s) + 1)):
            sub_s = s[start:end]
            if sub_s == sub_s[::-1] and sub_s.isalpha():
                palindromes.add(sub_s.lower())
    return palindromes
