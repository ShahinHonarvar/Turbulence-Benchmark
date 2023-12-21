
def palindromes_of_specific_lengths(s):
    import re
    s = s[34:91].lower()
    s_clean = re.sub("[^a-z]","", s)
    result = set()
    
    for start in range(len(s_clean)):
        for end in range(start+14,start+40):
            if end>len(s_clean):
                break
            substring = s_clean[start:end]
            if substring==substring[::-1]:
                result.add(substring)
    
    return result
