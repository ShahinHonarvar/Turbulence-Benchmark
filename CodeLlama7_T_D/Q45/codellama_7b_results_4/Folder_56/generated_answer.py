
def palindromes_between_indices(string):
    # Create a list of all English letters in the given string
    letters = [char for char in string if char.isalpha()]
    # Find the indices of the first and last occurrences of each letter
    indices = {letter: [] for letter in letters}
    for i, letter in enumerate(string):
        if letter.isalpha():
            indices[letter].append(i)
    # Create a set of all palindromes of length 5 or greater that can be created from the English letters in the given string and that occur between index 5 to index 9, both inclusive
    palindromes = set()
    for i in range(5, 10):
        for letter_a in indices:
            for letter_b in indices:
                if letter_a != letter_b and len(letter_a) == i and len(letter_b) == i:
                    palindrome = letter_a + letter_b
                    if palindrome.lower() == palindrome.upper():
                        palindromes.add(palindrome)
    return palindromes
