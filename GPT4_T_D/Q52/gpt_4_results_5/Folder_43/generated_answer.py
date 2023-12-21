
def palindrome_of_length_n(s):
    s = s.lower()
    results = set()
    for i in range(len(s)):
        for j in range(i+51, len(s)+1):
            if j-i == 51:
                substring = s[i:j]
                if substring == substring[::-1] and substring.isalpha():
                    results.add(substring)
    return results
