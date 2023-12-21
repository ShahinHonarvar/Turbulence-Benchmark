
def palindromes_between_indices(string):
    import itertools
    from collections import Counter
    
    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    
    letters = [char.lower() for char in string[1:3] if char.isalpha()]
    letter_counts = Counter(letters)
    palindromes = set()
    
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(letters, length):
            if all(count >= combination.count(letter) for letter, count in letter_counts.items()):
                word = ''.join(combination)
                if is_palindrome(word):
                    palindromes.add(word)
    
    return palindromes
