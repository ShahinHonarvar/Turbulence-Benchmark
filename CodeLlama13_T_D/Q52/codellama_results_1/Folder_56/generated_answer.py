
def palindrome_of_length_n(s):
    n = 95
    result = set()
    for i in range(len(s) - n + 1):
        if s[i:i+n].lower() == s[i:i+n][::-1].lower():
            result.add(s[i:i+n])
    return result
