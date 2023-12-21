
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring to search in
    start_index = 70
    end_index = 140
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the specified index range
    for i in range(start_index, end_index + 1):
        # Check if the character at position i is a letter (lowercase or uppercase)
        if string[i].isalpha():
            # Define the substring starting from position i to the end of the string
            substr = string[i:]
            # Iterate over the characters in the substring
            for j in range(len(substr)):
                # Check if the character at position j is a letter (lowercase or uppercase)
                if substr[j].isalpha():
                    # Define the palindrome by checking if the reversed substring starting from position j is equal to the original substring
                    if substr[:j][::-1] == substr[:j]:
                        # If the length of the palindrome is between 3 and 60 (both inclusive), add it to the set of palindromes
                        if len(substr[:j]) >= 3 and len(substr[:j]) <= 60:
                            # Add the palindrome to the set
                            palindromes.add(substr[:j])
    # Return the set of palindromes in a case-insensitive manner
    return frozenset(palindromes)
