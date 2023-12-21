
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring
    start_index = 41
    end_index = 89

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character is a letter
        if string[i].isalpha():
            # Define the length of the palindrome
            length = 38

            # Iterate over the possible lengths of the palindrome
            while length >= 23:
                # Define the center index of the palindrome
                center_index = i - (length // 2)

                # Check if the palindrome is within the bounds of the substring
                if center_index >= start_index and center_index <= end_index:
                    # Define the left and right indices of the palindrome
                    left_index = center_index - (length % 2)
                    right_index = center_index + (length % 2)

                    # Check if the palindrome is a valid one
                    if string[left_index:right_index] == string[left_index:right_index][::-1]:
                        # Add the palindrome to the set of palindromes
                        palindromes.add(string[left_index:right_index])
                length -= 1

    # Return the set of palindromes
    return palindromes
