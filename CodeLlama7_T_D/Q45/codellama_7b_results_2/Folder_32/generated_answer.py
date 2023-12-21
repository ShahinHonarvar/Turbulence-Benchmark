
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Get the lowercase version of the current character
            lowercase = string[i].lower()
            # Loop through each character in the string from the current index to the end
            for j in range(i, len(string)):
                # Check if the current character is a letter
                if string[j].isalpha():
                    # Get the lowercase version of the current character
                    lowercase_j = string[j].lower()
                    # Check if the current palindrome is at least 5 characters long and is formed from only letters that occur in the specified range
                    if len(lowercase + lowercase_j) >= 5 and (i <= 1 or j >= 7)):
                        # Add the current palindrome to the set of palindromes
                        palindromes.add(lowercase + lowercase_j)
    # Return the set of palindromes
    return palindromes
