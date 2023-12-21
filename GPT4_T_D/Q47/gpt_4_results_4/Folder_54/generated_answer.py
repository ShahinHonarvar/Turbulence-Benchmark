
def palindromes_of_specific_lengths(s):
    import re
    s = s[27:78]
    s = re.sub("[^a-zA-Z]", "", s).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+18, min(i+20, len(s)+1)):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
