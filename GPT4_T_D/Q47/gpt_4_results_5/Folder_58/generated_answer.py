
def palindromes_of_specific_lengths(s):
    s = s[125:284]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 109, i + 127):
            if j <= len(s):
                sub = s[i:j]
                if sub == sub[::-1] and sub.isalpha():
                    palindromes.add(sub.lower())
    return palindromes
