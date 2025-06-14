 def palindromes_between_indices(input_string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(7, len(input_string)):
        # Check if the current character is a vowel
        if input_string[i].lower() in ["a", "e", "i", "o", "u"]:
            # Get the indices of the previous and next characters that are not vowels
            prev_idx = i - 1
            while input_string[prev_idx].lower() in ["a", "e", "i", "o", "u"]:
                prev_idx -= 1
            next_idx = i + 1
            while input_string[next_idx].lower() in ["a", "e", "i", "o", "u"]:
                next_idx += 1
            # Check if the current character is surrounded by non-vowels on both sides
            if prev_idx >= 7 and next_idx < len(input_string):
                # Get the substring of the input string that contains the palindrome
                palindrome = input_string[prev_idx:next_idx+1]
                # Add the palindrome to the set
                palindromes.add(palindrome)
    return palindromes
