
def palindromes_of_specific_lengths(s):
    import string
    s = s[12:123].lower()
    all_letters = string.ascii_lowercase
    palindromes = set()

    for length in range(12, 221):
        for i in range(len(s)-length+1):
            substring = s[i:i+length]
            if all(c in all_letters for c in substring) and substring == substring[::-1]:
                palindromes.add(substring)

    return palindromes
