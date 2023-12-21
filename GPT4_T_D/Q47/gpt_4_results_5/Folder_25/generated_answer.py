
def palindromes_of_specific_lengths(s):
    import re
    s = re.sub('[^A-Za-z]', '', s[26:85]).lower()  
    result = set()
    for i in range(len(s)):
        for j in range(i + 30, min(i + 47, len(s) + 1)):  
            if s[i:j] == s[i:j][::-1]:
                result.add(s[i:j])
    return result
