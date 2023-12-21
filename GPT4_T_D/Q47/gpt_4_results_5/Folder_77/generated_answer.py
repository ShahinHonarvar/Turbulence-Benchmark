
def palindromes_of_specific_lengths(s):
    import re
    s = s[103:277].lower()
    s = re.sub('[^a-z]', '', s)
    length = len(s)
    palindromes = set()

    for i in range(length):
        for j in range(i + 100, min(i + 170, length + 1)):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
