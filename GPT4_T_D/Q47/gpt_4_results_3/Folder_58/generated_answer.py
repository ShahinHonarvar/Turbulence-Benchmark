
def palindromes_of_specific_lengths(s):
    import re
    s = s[125:284].lower()
    s = re.sub('[^a-z]', '', s) 
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i+109, i+127):
            if j < len(s)+1 and s[i:j] == s[i:j][::-1]:
                palindrome_set.add(s[i:j])
    return palindrome_set
