
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    arrangements = set(itertools.permutations(letters, 4))
    palindromes = set()
    
    for arrangement in arrangements:
        word = ''.join(arrangement)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
