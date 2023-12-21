
import itertools

def palindromes_between_indices(string):
    english_letters = [x for x in string if x.isalpha()]
    arrangements = set(itertools.permutations(english_letters, 8))
    palindromes = set()

    for arrangement in arrangements:
        if arrangement == tuple(reversed(arrangement)):
            palindromes.add(''.join(arrangement).lower())

    return palindromes
