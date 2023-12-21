 def palindromes_of_specific_lengths(string):
    # Find the substring from index 1 to index 7, both inclusive
    substr = string[1:8]
    # Create a set to store all palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(len(substr)):
        # Get the substring starting from the current character and ending at index 7
        sub_str = substr[i:8]
        # Check if the substring is a palindrome
        if sub_str == sub_str[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(sub_str)
    # Return an empty set if no palindromes were found in the specified index range
    if len(palindromes) == 0:
        return set()
    # Otherwise, return the set of all palindromes that meet the specified requirements
    else:
        return palindromes
