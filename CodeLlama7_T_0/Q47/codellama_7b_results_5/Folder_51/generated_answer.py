
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    substring = string[2:8]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its index
        char = substring[i]
        index = i

        # Check if the current character is a letter
        if char.isalpha():
            # Get the reverse of the substring starting from the current character
            rev_substring = substring[index::-1]
            # Iterate over each character in the reverse substring
            for j in range(len(rev_substring)):
                # Get the current character and its index in the reverse substring
                char2 = rev_substring[j]
                index2 = j

                # Check if the current character is a letter
                if char2.isalpha():
                    # Check if the current character and its reverse are the same
                    if char == char2:
                        # Get the length of the palindrome
                        length = index - index2 + 1
                        # Check if the length is between 3 to 4 (both inclusive)
                        if length >= 3 and length <= 4:
                            # Add the palindrome to the set
                            palindromes.add(substring[index2:index+1])
    # Return the set of palindromes
    return palindromes
