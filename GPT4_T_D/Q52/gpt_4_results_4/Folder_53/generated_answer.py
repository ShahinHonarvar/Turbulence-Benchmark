
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+68, len(s)+1):
            if not any(c.isdigit() for c in s[i:j]):
                if s[i:j] == s[i:j][::-1]:
                    result.add(s[i:j])
    return result
