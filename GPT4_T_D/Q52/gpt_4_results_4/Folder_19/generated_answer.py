
def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s)):
        for j in range(i+67, len(s)+1):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                result.add(s[i:j])
    return result
