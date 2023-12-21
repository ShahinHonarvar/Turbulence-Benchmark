
def palindromes_of_specific_lengths(s):
    import re
    palindrome_set = set()
    sub_string = s[35:89]

    for l in range(24, 34):
        for i in range(len(sub_string) - l + 1):
            sub = sub_string[i: i + l]
            if sub == sub[::-1] and re.fullmatch(r'[A-Za-z]*', sub):
                palindrome_set.add(sub.lower())        
                
    return palindrome_set
