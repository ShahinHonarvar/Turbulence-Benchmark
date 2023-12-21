
import itertools

def palindromes_between_indices(string):
    english_letters = [c.lower() for c in string if c.isalpha()]
    arrangements = set(itertools.permutations(english_letters, 6))
    palindromes = set()
    
    for arr in arrangements:
        word = ''.join(arr)
        if word == word[::-1]:
            palindromes.add(word)
    
    return palindromes
