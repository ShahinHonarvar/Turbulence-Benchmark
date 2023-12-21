
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start+5, len(s)+1):
            chunk = s[start:end]
            if chunk == chunk[::-1] and chunk.isalpha():
                palindromes.add(chunk)
    return palindromes
