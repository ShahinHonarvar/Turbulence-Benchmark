
def palindrome_of_length_n(s):
    s = s.lower()
    result = []
    for i in range(len(s)):
        for j in range(i+66, len(s)+1):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.append(substr)
    return set(result)
