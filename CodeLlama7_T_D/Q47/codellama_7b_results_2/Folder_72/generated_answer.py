
def palindromes_of_specific_lengths(string):
    # Define the range of indices for the substring search
    start_index = 26
    end_index = 90
    # Create a set to store all found palindromes
    palindromes = set()
    # Iterate over each index in the specified range
    for i in range(start_index, end_index + 1):
        # Check if the character at the current index is not a letter
        if not string[i].isalpha():
            continue

        # Check if the character at the current index is uppercase or lowercase
        if string[i].isupper() or string[i].islower():
            # Initialize variables to store the starting and ending indices of the current palindrome
            start = i
            end = i

            # Iterate over each index in the specified range
            for j in range(start_index, end_index + 1):
                # Check if the character at the current index is not a letter or the current index is before the starting index of the current palindrome
                if not string[j].isalpha() or j < start:
                    continue

                # Check if the character at the current index is uppercase or lowercase
                if string[j].isupper() or string[j].islower():
                    # Update the starting and ending indices of the current palindrome
                    start = min(start, j)
                    end = max(end, j)

            # Check if the length of the current palindrome is between 27 and 58 (both inclusive)
            if end - start + 1 >= 27 and end - start + 1 <= 58:
                # Add the current palindrome to the set of all found palindromes
                palindromes.add(string[start : end + 1])

    # Return the set of all found palindromes
    return palindromes
