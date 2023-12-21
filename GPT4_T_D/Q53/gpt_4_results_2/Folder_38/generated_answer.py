
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+56, len(s) + 1):
            subs = s[i:j]
            if subs == subs[::-1] and subs.isalpha():
                palindromes.add(subs)
    return palindromes
