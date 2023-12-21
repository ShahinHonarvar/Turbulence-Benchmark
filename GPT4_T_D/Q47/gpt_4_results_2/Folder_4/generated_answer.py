
def palindromes_of_specific_lengths(s):
    s = s[12:93]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 17, min(i + 67, len(s) + 1)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
