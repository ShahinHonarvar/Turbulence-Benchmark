
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    s_len = len(s)
    for i in range(s_len):
        for j in range(i+60, min(s_len+1, i+121)):
            subs = s[i:j]
            if subs == subs[::-1] and subs.isalpha():
                palindromes.add(subs)
    return palindromes
