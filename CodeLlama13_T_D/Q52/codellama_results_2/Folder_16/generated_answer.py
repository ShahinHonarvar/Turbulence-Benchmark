
def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        substr = s[i:i+255]
        if len(substr) < 255 or not all(c.isalpha() for c in substr):
            continue
        rev_substr = "".join(reversed(substr))
        if substr == rev_substr:
            palindromes.add(substr)
    return palindromes
