 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(1, len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the index of the previous letter
            prev_index = i - 1
            # Check if the previous letter is also a letter
            while prev_index >= 0 and not string[prev_index].isalpha():
                # Decrement the previous index by one
                prev_index -= 1
            # If the previous letter is also a letter, add it to the current palindrome
            if prev_index >= 0:
                current_palindrome = string[prev_index].lower() + string[i].lower()
                # Check if the current palindrome is at least 6 characters long and if it is a palindrome
                if len(current_palindrome) >= 6 and current_palindrome == current_palindrome[::-1]:
                    # Add the current palindrome to the set of palindromes
                    palindromes.add(current_palindrome)
    # Return the set of palindromes
    return palindromes
