
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase
    string = string.lower()
    # Define the range of indices for the substring
    start_index = 65
    end_index = 99
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(start_index, end_index + 1):
        # Check if the character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Define the starting and ending indices of the current palindrome
            start = i
            end = i

            # Iterate over the characters in the substring, starting from the current index
            for j in range(start + 1, end_index + 1):
                # Check if the character is a letter (uppercase or lowercase)
                if string[j].isalpha():
                    # Update the ending index of the palindrome
                    end = j

            # Check if the palindrome has the required length
            if start - end + 1 >= 26 and start - end + 1 <= 33:
                # Add the palindrome to the set of palindromes
                palindromes.add(string[start:end+1])

    # Return the set of palindromes
    return palindromes
