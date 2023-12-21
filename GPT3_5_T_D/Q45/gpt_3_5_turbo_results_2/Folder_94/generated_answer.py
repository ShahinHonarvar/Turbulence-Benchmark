
import itertools

def palindromes_between_indices(s):
    indices_range = range(3, 5)  # indices 3 to 4, inclusive
    english_letters = [c for c in s if c.isalpha()]
    palindromes = set()
  
    for length in range(3, len(english_letters)+1):
        for combination in itertools.combinations(english_letters, length):
            permutation = itertools.permutations(combination)

            for p in permutation:
                word = ''.join(p).lower()
                if word == word[::-1]:
                    palindromes.add(word)

    return palindromes
