
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(c for c in s if c.isalpha())
    palindromes = set()
    length = len(s)
    for l in range(54, length+1):
        for i in range(length-l+1):
            segment = s[i:i+l]
            if segment == segment[::-1]:
                palindromes.add(segment)
    return palindromes
