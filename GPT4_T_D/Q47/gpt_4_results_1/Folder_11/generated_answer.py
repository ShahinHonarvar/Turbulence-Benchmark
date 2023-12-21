
def palindromes_of_specific_lengths(s):
    import re
    set_of_palindromes = set()
    s = s[24:98]
    s = re.sub('[^a-zA-Z]', '', s).lower()
    for length in range(10, 37):
        for i in range(len(s) - length + 1):
            substring = s[i:i+length]
            if substring == substring[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes
