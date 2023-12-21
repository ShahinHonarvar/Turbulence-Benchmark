
def palindromes_of_specific_lengths(s):
    s = s[0:8].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j-i >= 4 and j-i <= 5:
                if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                    palindromes.add(s[i:j])
    return palindromes
