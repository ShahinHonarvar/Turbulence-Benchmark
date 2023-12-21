
def palindromes_of_specific_lengths(s):
    import re
    s = s[32:80]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+35, min(i+42, len(s)+1)):
            sub = s[i:j]
            if re.match("^[A-Za-z]*$", sub):
                if sub.lower() == sub[::-1].lower():
                    palindromes.add(sub)
    return palindromes
