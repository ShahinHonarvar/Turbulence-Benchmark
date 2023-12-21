
def palindromes_between_indices(string):
    import itertools
    from itertools import permutations
    
    letters = []
    for char in string[:6]:
        if char.isalpha():
            letters.append(char.lower())
    
    letter_combinations = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for combination in letter_combinations:
        word = ''.join(combination)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    
    return palindromes
