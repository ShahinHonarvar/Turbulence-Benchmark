
from itertools import permutations

def palindromes_between_indices(string):
    letters = [letter.lower() for letter in string if letter.isalpha()]
    if len(letters) < 6 or len(letters) < 7:
        return set()
    else:
        arrangements = set(permutations(letters[2:8], 6))
        palindromes = set()
        for arrangement in arrangements:
            word = ''.join(arrangement)
            if word == word[::-1]:
                palindromes.add(word)
        return palindromes
