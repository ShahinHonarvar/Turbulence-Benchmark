
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 80, len(s) + 1):
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result
