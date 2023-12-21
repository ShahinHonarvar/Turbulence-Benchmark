
def palindromes_of_specific_lengths(s):
    s = s[1:9].lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+3, i+5):
            if j <= len(s) and s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes
