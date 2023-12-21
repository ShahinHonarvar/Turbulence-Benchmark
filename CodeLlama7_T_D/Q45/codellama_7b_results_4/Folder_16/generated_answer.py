
def palindromes_between_indices(string):
    # Find the indices where the first and last letter appear in the string
    first_letter = string[0]
    last_letter = string[-1]
    first_index = string.find(first_letter)
    last_index = string.rfind(last_letter)
    # Create a set to store all palindromes
    palindromes = set()
    # Iterate over the letters in the given range
    for i in range(first_index + 1, last_index):
        # Check if the letter at index i is a vowel or a consonant
        if string[i].lower() in "aeiou":
            # If it is a vowel, check if there are any vowels before and after it in the string
            previous_vowel = string[:i].rfind("aeiou")
            next_vowel = string[i:].find("aeiou")
            # If there are no vowels before or after, skip to the next iteration
            if previous_vowel == -1 and next_vowel == -1:
                continue

        # If it is a consonant, check if there are any consonants before and after it in the string
        else:
            previous_consonant = string[:i].rfind(string[i])
            next_consonant = string[i:].find(string[i])
            # If there are no consonants before or after, skip to the next iteration
            if previous_consonant == -1 and next_consonant == -1:
                continue

        # Create a palindrome by reversing the string from index i to the end of the string
        palindrome = string[i:]

        # If the palindrome has at least 5 characters, add it to the set of palindromes
        if len(palindrome) >= 5:
            palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
