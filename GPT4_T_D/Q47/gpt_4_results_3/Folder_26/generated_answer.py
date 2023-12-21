
def palindromes_of_specific_lengths(s):
    import re
    s = s[24:85]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    palindrome_set = set()

    for palindrome_length in range(21, 32):
        for start_index in range(len(s) - palindrome_length + 1):
            substring = s[start_index : start_index + palindrome_length]
            if substring == substring[::-1]:
                palindrome_set.add(substring)

    return palindrome_set
