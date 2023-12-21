
def palindromes_of_specific_lengths(s):
    import re
    palindromes = set()
    s = s[127:289].lower()
    s = re.sub('[^a-z]', '', s)
    for i in range(len(s)):
        for l in range(119, 142):
            if i + l > len(s):
                break
            substr = s[i:i+l]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
