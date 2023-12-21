
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start_index = 100
    end_index = 300
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the string
    for i in range(start_index, end_index + 1):
        # Check if the current character is a letter
        if string[i].isalpha():
            # Define the substring of length 50 to 100
            substr = string[i - 50:i + 50]
            # Iterate through each palindrome in the substring
            for j in range(len(substr) - 1):
                # Check if the current character is a letter
                if substr[j].isalpha() and substr[j + 1].isalpha():
                    # Define the palindrome
                    palindrome = substr[j:j + 50]
                    # Check if the palindrome is of length between 50 to 100 (both inclusive)
                    if len(palindrome) >= 50 and len(palindrome) <= 100:
                        # Add the palindrome to the set
                        palindromes.add(palindrome)
    # Return the set of all palindromes found in the specified index range with the length requirement
    return palindromes
