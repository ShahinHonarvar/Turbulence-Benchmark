def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 1, -1, -1):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                result.add(s[i:j + 1])
    return result
