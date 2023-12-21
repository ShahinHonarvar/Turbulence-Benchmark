
def palindromes_of_specific_lengths(s):
    import re
    s = s[36:93].lower()
    s = re.sub('[^a-z]', '', s)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+10, min(i+36, len(s)+1)):
            temp = s[i:j]
            if temp == temp[::-1]:
                palindromes.add(temp)
    return palindromes
