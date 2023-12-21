
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for length in range(52, len(s) + 1):
        for i in range(0, len(s) - length + 1):
            candidate = s[i: i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes
