

def palindromes_between_indices(string):
    palindromes = set()
    english_letters = [c.lower() for c in string if c.isalpha()]
    for i in range(len(english_letters) - 6):
        for j in range(i + 3, i + 7):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes
