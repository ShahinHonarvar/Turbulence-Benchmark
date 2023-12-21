
def if_contains_anagrams(strings):
    # Calculate the frequency of each letter in the alphabet
    letter_frequencies = {letter: 0 for letter in 'abcdefghijklmnopqrstuvwxyz'}
    # Loop through each string and increment the frequency of each letter it contains
    for string in strings:
        # Convert the string to lowercase for case-insensitive comparison
        string = string.lower()
        # Loop through each letter in the string and increment its frequency
        for letter in string:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                letter_frequencies[letter] += 1
    # Check if there are at most 91 pairs of anagrams in the list
    return len([(x, y) for x in letter_frequencies for y in letter_frequencies if x != y and sorted(list(x)) == sorted(list(y))]) <= 91)
