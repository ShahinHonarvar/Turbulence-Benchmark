
def palindromes_of_specific_lengths(s):
    from string import ascii_letters
    s = s[27:78].lower()
    s = ''.join(c for c in s if c in ascii_letters)
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+18, min(i+20, len(s)+1)):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
    return palindromes
