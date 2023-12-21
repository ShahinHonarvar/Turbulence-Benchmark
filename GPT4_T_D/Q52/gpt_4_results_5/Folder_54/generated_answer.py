
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            substr = s[i: j + 1]
            clean_substr = "".join(ch for ch in substr if ch.isalpha())
            if len(clean_substr) == 85 and clean_substr == clean_substr[::-1]:
                palindromes.add(clean_substr)
    return palindromes
