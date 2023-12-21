 def palindromes_of_specific_lengths(string):
    # Find the start and end indices of the substring we want to search in
    start_index = 33
    end_index = 85
    # Create a list to store all the palindromes we find
    palindromes = []
    # Iterate through each character in the string, starting from the start index
    for i in range(start_index, end_index + 1):
        # Check if the current character is the same as the previous character
        if string[i] == string[i - 1]:
            # If it is, then we need to check if the next character is the same as the previous character
            if string[i + 1] == string[i - 2]:
                # If the next character is the same as the previous character, then we have found a palindrome
                palindromes.append(string[i - 2:i + 1])
    return palindromes
