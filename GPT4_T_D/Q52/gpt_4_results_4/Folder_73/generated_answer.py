
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if (len(sub) == 41 and sub == sub[::-1] and 
                all(c.isalpha() or c.isspace() for c in sub)):
                result.add(sub)
    return result
