
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start_index = 11
    end_index = 83
    substring = string[start_index:end_index+1]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its index in the substring
        char = substring[i]
        index = i + start_index
        # Check if the current character is a letter (a-zA-Z)
        if char.isalpha():
            # Get the reverse of the current character
            reverse = char[::-1]
            # Check if the reverse of the current character is also a letter
            if reverse.isalpha():
                # Get the length of the current palindrome
                length = index - (index+1)//2
                # Check if the length of the current palindrome is within the specified range
                if 37 <= length <= 60:
                    # Add the current palindrome to the set of palindromes
                    palindromes.add(substring[index-length+1:index+1])
    # Return the set of palindromes in a case-insensitive manner
    return frozenset([x.lower() for x in palindromes])
