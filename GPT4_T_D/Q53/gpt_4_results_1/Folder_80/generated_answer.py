
def palindrome_of_length_at_least_n(s):
    # Remove non-letter characters and convert to lower case
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    palindromes = set()

    # Check for palindromes of length n or more
    for i in range(len(s)):
        for j in range(i + 30, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:  # is palindrome
                palindromes.add(substring)

    return palindromes 
