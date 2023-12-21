
def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+42, min(i+78, len(s)+1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes
