
def palindrome_of_length_n(s):
    s = s.lower()
    n = 46
    alpha_s = ''.join(ch for ch in s if ch.isalpha())

    palindromes = set()
    for i in range(len(alpha_s) - n + 1):
        substring = alpha_s[i:i+n]
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
