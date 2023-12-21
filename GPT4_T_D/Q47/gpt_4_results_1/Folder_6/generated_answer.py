
def palindromes_of_specific_lengths(s):
    s = s[45:99]
    palindrome_set = set()
    for l in range(40, 48):
        for i in range(len(s) - l + 1):
            substring = s[i:i+l]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindrome_set.add(substring)
    return palindrome_set
