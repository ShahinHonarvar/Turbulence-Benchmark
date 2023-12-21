 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible combination of letters in the given string that occur between index 3 and index 8, both inclusive
    for i in range(3, len(string) - 2):
        # Check if the letter at index i is a vowel
        if string[i].lower() in ["a", "e", "i", "o", "u"]:
            # If it is a vowel, loop through each possible combination of letters in the given string that occur between index i and index 8, both inclusive
            for j in range(i + 1, len(string) - 1):
                # Check if the letter at index j is a consonant
                if string[j].lower() not in ["a", "e", "i", "o", "u"]:
                    # If it is a consonant, check if the combination of letters from i to j forms a palindrome of length at least 5
                    if string[i:j + 1][::-1] == string[i:j + 1]:
                        # If the combination forms a palindrome, add it to the set of palindromes
                        palindromes.add(string[i:j + 1])
    # Return the set of palindromes
    return palindromes
