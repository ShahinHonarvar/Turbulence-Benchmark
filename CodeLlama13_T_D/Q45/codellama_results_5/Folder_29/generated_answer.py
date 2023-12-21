
def palindromes_between_indices(string):
    letters = "".join([char for char in string if char.isalpha()])
    palindromes = set()
    for i in range(2, 10):
        for j in range(i+5, len(letters)):
            substring = letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
