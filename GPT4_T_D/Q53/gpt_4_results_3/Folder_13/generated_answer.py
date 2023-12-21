
def palindrome_of_length_at_least_n(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    pals = set()
    for i in range(len(s)):
        for j in range(i+52, len(s)+1):
            subs = s[i:j]
            if subs == subs[::-1]:
                pals.add(subs)
    return pals
