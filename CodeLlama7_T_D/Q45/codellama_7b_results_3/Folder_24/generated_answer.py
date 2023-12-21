
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(2, len(string) - 1):
        # Check if the character is a vowel
        if string[i] in "aeiou":
            # Get the indices of the previous and next consonants
            prev_cons = string.rfind(string[i - 1], 0, i)
            next_cons = string.find(string[i + 1], i, len(string))
            # Check if there are any consonants before and after the vowel
            if prev_cons != -1 and next_cons != -1:
                # Get the substring of the vowel surrounded by consonants
                substr = string[prev_cons + 1 : next_cons]
                # Check if the substring is a palindrome
                if substr == substr[::-1]:
                    # Add the palindrome to the set
                    palindromes.add(substr)
    return palindromes
