
def palindrome_of_length_at_least_n(s):
    import re
    # Removing non-letters and converting to lowercase
    s = re.sub('[^a-zA-Z]', '', s).lower()
    n = 141
    palindromes = set()

    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
