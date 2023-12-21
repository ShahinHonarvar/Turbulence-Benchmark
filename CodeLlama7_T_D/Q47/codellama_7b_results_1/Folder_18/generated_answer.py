 def palindromes_of_specific_lengths(string):
    # Define the index range for which we want to find palindromes
    start_index = 11
    end_index = 83
    # Create a list to store all the palindromes
    palindromes = []
    # Iterate through each character in the string within the specified index range
    for i in range(start_index, end_index + 1):
        # Check if the current character is a palindrome of length between 13 to 66 (both inclusive)
        if len(string[i:i+1]) >= 13 and len(string[i:i+1]) <= 66:
            # Check if the current character is a palindrome in a case-insensitive manner
            if string[i:i+1].lower() == string[i:i+1][::-1].lower():
                # Add the current palindrome to the list of palindromes
                palindromes.append(string[i:i+1])
    return set(palindromes)
