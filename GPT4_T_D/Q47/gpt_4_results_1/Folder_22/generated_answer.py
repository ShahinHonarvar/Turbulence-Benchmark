
def palindromes_of_specific_lengths(s):
    s = s[100:201].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+5, min(i + 11, len(s) + 1)):
            subs = s[i:j]
            if subs == subs[::-1] and subs.isalpha():
                result.add(subs)
    return result
