
def palindromes_of_specific_lengths(s):
    s = s[11:94]
    palindromes_set = set()
    for i in range(len(s)):
        for j in range(i+34, min(i+55, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes_set.add(substring.lower())
    return palindromes_set
