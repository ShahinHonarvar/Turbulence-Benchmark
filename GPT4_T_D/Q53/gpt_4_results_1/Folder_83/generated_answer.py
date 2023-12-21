
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 60, len(s) + 1):
            segment = s[i:j]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes
