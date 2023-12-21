
def palindromes_of_specific_lengths(string):
    # Define the substring range for searching palindromes
    start_index = 3
    end_index = 300
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character at index i is a letter
        if string[i].isalpha():
            # Define the left and right indices for the palindrome
            left = i - 1
            right = i + 1
            # Iterate over the characters in the palindrome
            while left >= start_index and right <= end_index:
                # Check if the character at index left is equal to the character at index right
                if string[left].lower() == string[right].lower():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(string[left:right])
                    # Update the indices for the next iteration
                    left -= 1
                    right += 1
                else:
                    # Break out of the loop if the characters are not equal
                    break
    return palindromes
