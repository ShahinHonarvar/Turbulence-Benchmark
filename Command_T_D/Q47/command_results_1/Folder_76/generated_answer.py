def palindromes_of_specific_lengths(s):
    return set(map(str.lower, (s[101:], s[101:].replace(' ',''), s[101:].replace(' ','')[::-1], s[101:].replace(' ','')[:::-1])))
