import re
def palindromes_between_indices(text):
    text = text.lower()
    letters = set(re.findall(r'[a-z]', text))
    return set(map(str.lower, filter(lambda p: p[0] == p[-1], (p for p in (''.join(sorted(text))[3:-3], 
                                                          ''.join(sorted(text))[4:-4], 
                                                          ''.join(sorted(text))[5:-5], 
                                                          ''.join(sorted(text))[6:-6], 
                                                          ''.join(sorted(text))[7:-7])))))
