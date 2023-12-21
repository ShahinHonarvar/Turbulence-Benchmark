
def palindrome_of_length_at_least_n(s):
    s = "".join(char for char in s if char.isalpha())
    s = s.lower()
    palindromes = set()
    for len_substring in range(15, len(s) + 1):
        for i in range(0, len(s) - len_substring + 1):
            substring = s[i : i + len_substring]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
