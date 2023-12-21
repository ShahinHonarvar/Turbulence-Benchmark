
def palindromes_of_specific_lengths(s):
    import re
    s = s[43:96]
    string = re.sub("[^a-z]", "", s.lower())
    results = set()
    for i in range(len(string)):
        for j in range(18, 48):
            palindrome = string[i:i+j]
            if len(palindrome) == j and palindrome == palindrome[::-1]:
                results.add(palindrome)
    return results
