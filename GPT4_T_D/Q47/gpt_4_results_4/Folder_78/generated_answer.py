
def palindromes_of_specific_lengths(s):
    import re
    s = s[15:73]
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i+19,min(i+56,len(s)+1)):
            sub = s[i:j]
            sub_no_special = re.sub('[^A-Za-z]+', '', sub)
            if sub_no_special.lower() == sub_no_special[::-1].lower() and len(sub_no_special) == len(sub):
                set_of_palindromes.add(sub_no_special)
    return set_of_palindromes
