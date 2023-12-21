
def palindromes_of_specific_lengths(s):
    s = s[31:92]
    set_palindromes = set()
    s = ''.join(c for c in s if c.isalnum()).lower()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 54, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1]:
                set_palindromes.add(substr)
    return set_palindromes
