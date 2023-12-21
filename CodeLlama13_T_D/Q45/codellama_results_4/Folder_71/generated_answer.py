
def palindromes_between_indices(string):
    indices = range(1, 4)
    letters = set("".join(string[i] for i in indices))
    palindromes = set()
    for letter in letters:
        for _ in range(len(letter)):
            if string[i].lower() == letter.lower():
                palindromes.add(letter)
    return palindromes
