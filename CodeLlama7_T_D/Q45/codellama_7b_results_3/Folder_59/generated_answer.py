
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(8, 9 + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a copy of the current character and its reverse
            forward = string[i]
            backward = string[i]
            # Loop through each character in the rest of the string
            for j in range(i + 1, len(string)):
                # Check if the current character is a letter
                if string[j].isalpha():
                    # Add the current character and its reverse to the forward and backward variables
                    forward += string[j]
                    backward = string[j] + backward
            # If the length of the palindrome is at least 3, add it to the set of palindromes
            if len(forward) >= 3:
                palindromes.add(forward.lower())
            if len(backward) >= 3:
                palindromes.add(backward.lower())
    # Return the set of palindromes
    return palindromes
