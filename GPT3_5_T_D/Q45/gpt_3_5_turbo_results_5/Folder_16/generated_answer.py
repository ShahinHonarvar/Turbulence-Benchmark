
import itertools

def palindromes_between_indices(string):
    indices = range(6, 10)
    letters = [char.lower() for char in string if char.isalpha()]
    arrangements = set(itertools.permutations(letters, 4))
    palindromes = set()
    
    for arrangement in arrangements:
        palindrome = ''.join(arrangement) + ''.join(reversed(arrangement))
        if palindrome.lower() == palindrome.lower()[::-1]:
            palindromes.add(palindrome)
    
    return palindromes
