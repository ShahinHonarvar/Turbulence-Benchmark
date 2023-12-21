
def palindromes_of_specific_lengths(s):
    s = s[10:60]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 18, min(i + 37, n + 1)):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result
