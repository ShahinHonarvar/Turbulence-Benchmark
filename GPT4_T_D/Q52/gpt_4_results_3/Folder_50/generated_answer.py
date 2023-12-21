
def palindrome_of_length_n(s):
    result_set = set()
    s = s.lower()
    for i in range(len(s) - 39):
        substring = s[i:i+40]
        if substring == substring[::-1] and substring.isalpha():
            result_set.add(substring)
    return result_set
