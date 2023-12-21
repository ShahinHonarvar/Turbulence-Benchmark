
def palindromes_of_specific_lengths(s):
    import re
    s_sub = s[12:57]
    palindromes_set = set()
    
    for start in range(len(s_sub)):
        for end in range(start + 20, min(start + 22, len(s_sub) + 1)):
            substring = s_sub[start:end]
            substring_alpha = re.sub(r'[^a-z]', '', substring.lower())
            if substring_alpha == substring_alpha[::-1]:
                palindromes_set.add(substring)

    return palindromes_set
