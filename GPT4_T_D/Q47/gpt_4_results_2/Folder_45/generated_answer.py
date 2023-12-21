
def palindromes_of_specific_lengths(s):
    import re
    
    s_check = s[70:141]
    
    s_check = re.sub(r'[^a-z]','', s_check.lower())
    palindromes_set = set()
    for start in range(len(s_check)):
        for end in range(start+3, min(start+61, len(s_check)+1)):
            substring = s_check[start:end]
            if substring == substring[::-1]:
                palindromes_set.add(substring)
    return palindromes_set
