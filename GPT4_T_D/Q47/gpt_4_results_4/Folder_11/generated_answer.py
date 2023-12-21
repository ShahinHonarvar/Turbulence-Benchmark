
def palindromes_of_specific_lengths(s):
    s = s[24:98]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+10, i+37):
            if j > len(s):
                break
            subs = s[i:j]
            if subs.lower() == subs[::-1].lower() and subs.isalpha():
                palindromes.add(subs)
    return palindromes
