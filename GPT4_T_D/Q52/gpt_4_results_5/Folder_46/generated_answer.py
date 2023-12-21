
def palindrome_of_length_n(s):
    s = s.lower()
    n = 464
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + n, min(i + 2 * n, len(s) + 1)):
            segment = s[i:j]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)

    return palindromes
