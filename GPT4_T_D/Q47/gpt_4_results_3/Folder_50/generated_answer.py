
def palindromes_of_specific_lengths(s):
    import re
    s = s.lower()
    s = re.sub("[^a-z]","",s[36:93])
    result = set()

    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i: j + 1]

            if len(substr) in range(10, 36):
                if substr == substr[::-1]:
                    result.add(substr)

    return result
