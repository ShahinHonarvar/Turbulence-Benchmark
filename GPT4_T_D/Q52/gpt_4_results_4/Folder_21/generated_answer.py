
def palindrome_of_length_n(s):
    s = s.lower()
    result_set = set()
    for i in range(len(s)):
        for j in range(i + 407, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 407 and substring == substring[::-1] and substring.isalpha():
                result_set.add(substring)
    return result_set
