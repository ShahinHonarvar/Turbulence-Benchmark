
def palindromes_between_indices(string):
    from itertools import permutations

    english_letters = [letter for letter in string if letter.isalpha()]
    english_letters = ''.join(english_letters)

    if len(english_letters) < 6:
        return set()

    palindromes = set()
    for i, first_letter in enumerate(english_letters[:6]):
        for j, last_letter in enumerate(english_letters[i:i+6]):
            substring = english_letters[i:j+i+1]
            if len(substring) >= 3 and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring.lower())

    return palindromes
