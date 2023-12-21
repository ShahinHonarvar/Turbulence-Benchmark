
def palindrome_of_length_at_least_n(s):
    import string
    import re
    s = re.sub('['+string.punctuation+' ]', '', s).lower()
    n = 140
    pals = set()
    for i in range(len(s)):
        for j in range(i+n, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                pals.add(sub)
    return pals
