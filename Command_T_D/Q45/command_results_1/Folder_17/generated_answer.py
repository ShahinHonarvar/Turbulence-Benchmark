import re
def palindromes_between_indices(s):
    str_lower = s.lower()
    for i in range(3, 7):
        for j in range(i, i + i):
            str_lower = re.sub(str_lower[i:j], str_lower[j:i], str_lower)
            if str_lower == str_lower[::-1]:
                return set(str_lower[2:i+1])
    return set()
