
def palindromes_of_specific_lengths(string):
    # Extract the substring from index 70 to index 140, both inclusive
    substr = string[70:141]
    
    # Initialize an empty set to store the palindromes
    palindromes = set()
    
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Check if the current character is a letter
        if substr[i].isalpha():
            # If it is, check if there is a palindrome of length 3 to 60 starting from that index
            for j in range(2, 61):
                if substr[i:i+j] == substr[i:i+j][::-1]:
                    # If there is, add it to the set of palindromes
                    palindromes.add(substr[i:i+j])
    
    return palindromes
