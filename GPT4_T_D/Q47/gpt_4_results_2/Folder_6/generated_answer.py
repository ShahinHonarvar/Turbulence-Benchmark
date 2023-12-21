
def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = s[45:99]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+40, i+48):
            if j <= len(s):
                substr = s[i:j]
                if substr == substr[::-1] and substr.isalpha():
                    palindromes.add(substr)
    return palindromes
