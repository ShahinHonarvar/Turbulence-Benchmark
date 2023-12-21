
def palindromes_of_specific_lengths(s):
    import re
    s = s[17:96]
    s = re.sub(r'[^a-zA-Z]', '', s)
    res = set()
    for p_len in range(13, 50):
        for i in range(len(s) - p_len + 1):
            sub_s = s[i : i + p_len]
            if sub_s.lower() == sub_s[::-1].lower():
                res.add(sub_s)
    return res
