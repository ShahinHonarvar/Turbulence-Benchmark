
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 113, len(s) + 1):
            if s[i:j] == s[i:j][::-1]: 
                sub_string = s[i:j]
                if sub_string.isalpha():
                    result.add(sub_string)
    return result
