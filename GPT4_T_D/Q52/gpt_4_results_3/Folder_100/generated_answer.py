
def palindrome_of_length_n(s):
    s = "".join(ch for ch in s if ch.isalpha()).lower()
    all_palindromes = set(s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] == s[i:j][::-1] and len(s[i:j]) == 91)
    return all_palindromes
