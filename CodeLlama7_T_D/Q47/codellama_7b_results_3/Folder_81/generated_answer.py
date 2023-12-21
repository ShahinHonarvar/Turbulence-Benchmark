
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration of palindromes
    sub_range = string[12:122]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(sub_range)):
        # Check if the current character is a palindrome
        if sub_range[i:i+1] == sub_range[i:i+1][::-1]:
            # If it is, append it to the set of palindromes
            palindromes.add(sub_range[i:i+1])
    # Return the set of palindromes that meet the specified requirements
    return palindromes
