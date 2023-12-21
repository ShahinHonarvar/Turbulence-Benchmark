
import itertools

def palindromes_between_indices(string):
    string = string[4:10].lower()
    alpha_letters = [c for c in string if c.isalpha()]
    palindromes = set()
  
    for r in range(6, len(alpha_letters)+1):
        possible_strings= list(itertools.permutations(alpha_letters, r))

        for p in possible_strings: 
            possible_string = ''.join(p)
            if possible_string == possible_string[::-1]:
                palindromes.add(possible_string)
    
    return palindromes
