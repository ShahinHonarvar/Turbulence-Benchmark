
import itertools

def palindromes_between_indices(s):
    s = s[4:7].lower()
    characters_set = set(s)
    permutations = set()
    palindromes = set()

    for char_set in itertools.combinations(characters_set, 4):
        permutations.update(itertools.permutations(char_set))

    for perm in permutations:
        possible_string = ''.join(perm)
        if possible_string == possible_string[::-1]:
            palindromes.add(possible_string)

    return palindromes
