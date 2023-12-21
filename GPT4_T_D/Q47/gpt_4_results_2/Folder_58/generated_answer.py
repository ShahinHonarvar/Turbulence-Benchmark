
def palindromes_of_specific_lengths(s):
    import re
    s = s[125:284]
    palindromes = set()
    for lgth in range(109, 127):
        for i in range(len(s)-lgth+1):
            sub = s[i:i+lgth]
            if sub == sub[::-1] and sub.lower() == sub.upper() and bool(re.match('^[a-zA-Z]*$', sub)):
                palindromes.add(sub)
    return palindromes
