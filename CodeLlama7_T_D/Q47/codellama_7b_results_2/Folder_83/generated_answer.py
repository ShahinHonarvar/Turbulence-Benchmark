 def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start_index = 75
    end_index = 95
    substring = string[start_index:end_index + 1]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its mirrored version
        char = substring[i]
        mirrored_char = substring[len(substring) - i - 1]
        # Check if the current character is a letter and its mirrored version is also a letter
        if char.isalpha() and mirrored_char.isalpha():
            # Get the length of the palindrome
            length = (i + 1) * 2 - 1
            # Check if the length is within the specified range
            if length >= 7 and length <= 9:
                # Add the palindrome to the set
                palindromes.add(substring[i:length])
    return palindromes
