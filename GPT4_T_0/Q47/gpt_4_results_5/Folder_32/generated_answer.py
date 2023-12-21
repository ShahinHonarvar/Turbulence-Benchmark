
def palindromes_of_specific_lengths(s):
    import re
    s = s[16:78]
    s = re.sub('[^a-zA-Z]', '', s)
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+43, min(i+48, len(s)+1)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
