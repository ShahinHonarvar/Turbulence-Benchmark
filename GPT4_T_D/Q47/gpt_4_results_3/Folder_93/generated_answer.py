
def palindromes_of_specific_lengths(s):
    s = s[17:96]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for i in range(13, 50):
        for j in range(len(s) - i + 1):
            subs = s[j:j+i]
            if subs == subs[::-1]:
                result.add(subs)
    return result
