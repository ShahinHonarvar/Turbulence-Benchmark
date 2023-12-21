
import itertools

def palindromes_between_indices(string):
    string = string[3:10].lower()
    letters = [char for char in string if char.isalpha()]
    palindromes = set()

    for i in range(5, len(letters) + 1):
        for subset in itertools.combinations(letters, i):
            subset = list(subset)
            for perm in itertools.permutations(subset, len(subset)):
                word = "".join(perm)
                if word == word[::-1]:
                    palindromes.add(word)
                    
    return palindromes
