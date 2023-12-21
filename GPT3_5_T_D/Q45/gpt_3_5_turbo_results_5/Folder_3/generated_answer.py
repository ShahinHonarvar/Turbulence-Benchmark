
def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    if len(letters) < 3 or len(letters) < 10:
        return set()
    palindromes = set()
    for i in range(7, 10):
        for j in range(i + 2, min(i + 4, len(letters) + 1)):
            sub_string = letters[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    return palindromes
