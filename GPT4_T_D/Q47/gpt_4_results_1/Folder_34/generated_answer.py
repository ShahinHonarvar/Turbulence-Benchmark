
def palindromes_of_specific_lengths(text):
    import string
    text = text[200:301]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i+10, min(i+51, len(text)+1)):
            substring = text[i:j].lower()
            if all(char in string.ascii_lowercase for char in substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
