
def palindromes_of_specific_lengths(s):
    import re
    s = s[21:63]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+22, min(i+34, len(s)+1)):
            sub = s[i:j]
            if sub == sub[::-1] and re.match('^[a-zA-Z]*$', sub):
                palindromes.add(sub.lower())
    return palindromes
