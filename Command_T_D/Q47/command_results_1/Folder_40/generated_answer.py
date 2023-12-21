def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(3, 6):
        res |= set(re.findall(r'[a-z]{i}(?=([a-z]{i}){2}'.lower(), s[0:6]))
    return res
