
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    possible_letters = [letter for letter in letters if 0 <= ord(letter.lower()) - ord('a') <= 7]

    palindromes = set()
    for comb in itertools.combinations(possible_letters, 4):
        permutations = set(itertools.permutations(comb))
        for perm in permutations:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)

    return palindromes
