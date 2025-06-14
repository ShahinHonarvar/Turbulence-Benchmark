
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 36
    end = 92
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(start, end + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Create a variable to store the lowercase version of the current character
            lower_case = string[i].lower()
            # Iterate through each character in the substring starting from the current index
            for j in range(i, end + 1):
                # Check if the current character is a letter
                if string[j].isalpha():
                    # Create a variable to store the lowercase version of the current character
                    lower_case_2 = string[j].lower()
                    # Check if the current character is the same as the previous character in reverse order
                    if lower_case == lower_case_2:
                        # Add the palindrome to the set
                        palindromes.add(string[i:j+1])
    # Return the set of palindromes
    return palindromes
