 def palindromes_between_indices(input_string):
    # Create a list of all the English letters in the input string
    letter_list = []
    for char in input_string:
        if char.isalpha():
            letter_list.append(char)
    # Initialize an empty set to store the palindromes

    palindromes = set()
    # Loop through each possible length of palindrome

    for length in range(5, len(letter_list) + 1):
        # Loop through each possible starting index for the palindrome

        for start in range(3, len(letter_list) - length + 1):
            # Check if the substring starting at start and of length length is a palindrome

            substr = "".join(reversed(letter_list[start:start+length]))
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
