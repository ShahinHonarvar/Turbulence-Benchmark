
def palindromes_of_specific_lengths(string):
    import re
    palindrome_set = set()
    for length in range(26, 30):
        for i in range(13, 100 - length + 1):
            substring = string[i:i+length]
            if re.match("^[A-Za-z]*$", substring) and substring.lower() == substring[::-1].lower():
                palindrome_set.add(substring)
    return palindrome_set
