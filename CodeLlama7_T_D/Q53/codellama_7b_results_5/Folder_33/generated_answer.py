 def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Loop through each character in the reversed substring starting from the current index
            for j in range(len(string)-i, -1, -1):
                # Check if the current character and the previous character are not the same
                if string[i] != string[j]:
                    # If the current character and the previous character are not the same, break out of the inner loop
                    break
                # If the current character and the previous character are the same, add the palindrome to the set
                else:
                    palindromes.add(string[i:j+1])
    # Return the set of palindromes that meet the criteria
    return palindromes
