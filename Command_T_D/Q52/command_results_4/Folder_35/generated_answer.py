def palindrome_of_length_n(s):
    result = set()
    for i in range(1, len(s) + 1):
        str1 = s[i - 1:i + 116]
        str2 = s[i:i + 116]
        if str1[::-1] == str1:
            result.add(str1)
        if str2[::-1] == str2:
            result.add(str2)
    return result
