
import itertools

def palindromes_between_indices(string):
    english_letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    
    for n in range(4, len(english_letters)+1):
        for combination in itertools.combinations(english_letters, n):
            permutation = list(itertools.permutations(combination))
            
            for word in permutation:
                word = ''.join(word).lower()
                if word == word[::-1]:
                    palindromes.add(word)
    
    return palindromes
