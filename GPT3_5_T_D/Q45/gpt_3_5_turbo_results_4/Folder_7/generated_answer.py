
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string if char.isalpha()]
    indices = range(1, 10)
    arrangements = set(itertools.combinations(letters, len(indices)))
    palindromes = set()
    
    for arrangement in arrangements:
        if arrangement == arrangement[::-1]:
            palindrome = ''.join(arrangement)
            palindromes.add(palindrome)
    
    return palindromes
