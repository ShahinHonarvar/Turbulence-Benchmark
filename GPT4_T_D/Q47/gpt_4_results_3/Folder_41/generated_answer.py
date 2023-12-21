
def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    palin_set = set()
    for i in range(len(s)):
        for j in range(i+3, min(i+5, len(s)+1)):
            sub_s = s[i:j]
            if(sub_s == sub_s[::-1] and sub_s.isalpha()):
                palin_set.add(sub_s)
    return palin_set
