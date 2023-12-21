
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    
    english_letters = [char.lower() for char in string if char.isalpha()]
    english_letters_counter = Counter(english_letters)
    possible_combinations = set(itertools.permutations(english_letters, 4))
    palindromes = set()
    
    for combination in possible_combinations:
        letters_needed = Counter(combination)
        if all(english_letters_counter[letter] >= letters_needed[letter] for letter in letters_needed):
            word = ''.join(combination)
            if is_palindrome(word):
                palindromes.add(word)
    
    return palindromes
