
def palindrome_of_length_n(s):
    s = s.lower()
    length = 407
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + length, len(s) + 1):
            if j - i == length:
                subs = s[i:j]
                if subs == subs[::-1] and subs.isalpha():
                    palindromes.add(subs)
    return palindromes
