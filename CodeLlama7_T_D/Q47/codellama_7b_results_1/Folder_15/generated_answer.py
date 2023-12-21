
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index 6 (both inclusive)
        substring = string[i:i+7]
        # Loop through each palindrome of length between 3 and 6 in the substring
        for j in range(3, 7):
            # Check if the palindrome is a valid one
            if (substring[0:j] == substring[0:j][::-1]) and (len(substring[0:j]) >= 3) and (len(substring[0:j]) <= 6):
                # Add the palindrome to the set of palindromes
                palindromes.add(substring[0:j])
    return palindromes
