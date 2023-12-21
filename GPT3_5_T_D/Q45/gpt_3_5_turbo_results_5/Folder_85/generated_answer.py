
def palindromes_between_indices(string):
    import itertools
    from string import ascii_letters

    palindromes = set()
    english_letters = [char.lower() for char in string if char in ascii_letters]
  
    for sequence in itertools.permutations(english_letters[2:9], 7):
        if sequence == sequence[::-1]:
            palindromes.add(''.join(sequence).lower())
    
    return palindromes
