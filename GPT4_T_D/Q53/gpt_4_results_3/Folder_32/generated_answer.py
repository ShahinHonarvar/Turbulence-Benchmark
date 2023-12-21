
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 70
    result = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result
