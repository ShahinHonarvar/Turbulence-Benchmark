
def palindrome_of_length_at_least_n(s):
    n = 49
    result = set()
    s = s.lower()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result
