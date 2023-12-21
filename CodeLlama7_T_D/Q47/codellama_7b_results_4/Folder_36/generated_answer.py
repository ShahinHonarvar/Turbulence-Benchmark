
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start_index = 124
    end_index = 283
    substring = string[start_index:end_index]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(len(substring)):
        # Get the current character and its index
        char = substring[i]
        index = i


        # Check if the current character is a letter
        if char.isalpha():
            # Check if the current character is uppercase
            if char.isupper():
                # Convert the current character to lowercase
                char = char.lower()


            # Check if the current character is a palindrome of the desired length
            if len(char * 2 - 1) in range(115, 134 + 1):
                # Add the palindrome to the set
                palindromes.add(char * 2 - 1)
    return palindromes
