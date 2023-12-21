
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 79):
        sub_string = s[i:i+80]
        if sub_string == sub_string[::-1] and sub_string.isalpha():
            result.add(sub_string)
    return result
