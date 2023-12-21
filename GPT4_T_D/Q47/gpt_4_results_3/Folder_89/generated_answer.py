
def palindromes_of_specific_lengths(s):
    import re
    s = s[18:89].lower()
    letters_only = re.sub("[^a-z]", "", s)
    palindromes = set()
    for i in range(len(letters_only)):
        for j in range(i+12, min(i+15, len(letters_only)+1)):
            substring = letters_only[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
