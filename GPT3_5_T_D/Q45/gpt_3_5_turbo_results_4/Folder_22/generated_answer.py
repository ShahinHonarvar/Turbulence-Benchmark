
def palindromes_between_indices(string):
    letters = [c.lower() for c in string[5:7] if c.isalpha()]
    palindromes = set()
    if len(letters) > 0:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                palindrome = letters[i] + letters[j] + letters[j] + letters[i]
                palindromes.add(palindrome)
    return palindromes
