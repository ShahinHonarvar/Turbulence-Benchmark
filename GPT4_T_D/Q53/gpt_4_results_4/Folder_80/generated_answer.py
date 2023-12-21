
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + 30, len(s) + 1):
            chunk = s[i:j]
            if chunk == chunk[::-1]:
                palindromes.add(chunk)

    return palindromes
