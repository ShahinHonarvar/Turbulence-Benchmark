
def palindrome_of_length_n(s):
    s = s.lower()
    n = 33
    s_len = len(s)
    result = set()
    for i in range(s_len):
        for j in range(i + n, min(s_len + 1, i + n + 1)):
            sub_string = s[i:j]
            if sub_string == sub_string[::-1] and sub_string.isalpha():
                result.add(sub_string)
    return result
