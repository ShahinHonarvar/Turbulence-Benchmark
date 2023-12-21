
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 94, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                result.add(sub)
    return result
