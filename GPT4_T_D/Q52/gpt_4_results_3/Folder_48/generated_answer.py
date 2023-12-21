
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalpha())
    palindromes = set()
    for i in range(len(s) - 185):
        if s[i:i+186] == s[i:i+186][::-1]:
            palindromes.add(s[i:i+186])
    return palindromes
