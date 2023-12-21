
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 9):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a list of all possible palindromes of length at least 3
            palindromes_list = [string[i] + string[i - 1] + string[i - 2], string[i - 1] + string[i] + string[i - 1], string[i - 2] + string[i - 1] + string[i]]
            # Loop through each palindrome in the list
            for j in range(3):
                # Check if the current palindrome is a valid palindrome of length at least 3
                if len(palindromes_list[j]) >= 3 and palindromes_list[j].lower() == palindromes_list[j][::-1].lower():
                    # Add the current palindrome to the set of palindromes
                    palindromes.add(palindromes_list[j])
    # Return the set of all palindromes of length at least 3 that can be created from the English letters of the given string that occur between index 4 to index 8, both inclusive
    return palindromes
