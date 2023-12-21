
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 84, len(s) + 1):
            if j - i == 84:
                substr = s[i:j]
                if substr == substr[::-1] and substr.isalpha():
                    result.add(substr)
    return result
