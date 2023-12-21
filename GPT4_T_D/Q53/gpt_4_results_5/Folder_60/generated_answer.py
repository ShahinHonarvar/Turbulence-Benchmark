
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    output = set()
    s_length = len(s)
    for i in range(s_length):
        for j in range(i + 80, s_length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                output.add(substring)
    return output
