
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible arrangement of the English letters in the given string that occur between index 5 to index 9, both inclusive
    for i in range(5, 10):
        # Check if the current letter is a vowel or not
        if string[i].lower() in ["a", "e", "i", "o", "u"]:
            # If it is a vowel, then form a palindrome with the letter on both sides of the central letter
            palindromes.add(string[i - 2] + string[i].lower() + string[i + 2])
    return palindromes
