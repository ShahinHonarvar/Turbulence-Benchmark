
def palindromes_of_specific_lengths(s):
    import re
    s = s[70:141]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+2, len(s)):
            if 3 <= j-i+1 <= 60:
                substring = s[i:j+1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes
