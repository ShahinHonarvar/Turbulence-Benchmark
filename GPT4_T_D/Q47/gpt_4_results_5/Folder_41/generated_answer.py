
def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+3, i+5):
            if j <= len(s):
                substr = s[i:j]
                if substr == substr[::-1] and substr.isalpha():
                    palindromes.add(substr)
    return palindromes
