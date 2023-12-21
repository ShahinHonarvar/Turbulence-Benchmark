import re
def palindromes_of_specific_lengths(s):
    i = 0
    j = 10
    while i < j:
        if s[i] == s[j]:
            if s[i] in 'aeiouAEIOU':
                if re.match(r'(.)\1', s[i:j+1]):
                    return {s[i:j+1]}
            i += 1
            j -= 1
        elif s[i] < s[j]:
            i += 1
        else:
            j -= 1
    return set()
