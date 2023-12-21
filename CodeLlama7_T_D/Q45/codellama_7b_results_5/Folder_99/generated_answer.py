
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each index of the string
    for i in range(4, 9):
        # Get the character at the current index
        char = string[i]
        # If the character is a letter (a-z or A-Z)
        if char.isalpha():
            # Convert the character to lowercase
            char_lower = char.lower()
            # Check if the character appears in the string at least three times, starting from index 4 and ending at index 8
            if string[4:].count(char_lower) >= 3:
                # Get a list of all indices where the character appears in the string between index 4 and index 8
                char_indices = [i for i, x in enumerate(string[4:]) if x == char_lower]
                # Loop through each index of the character in the string
                for j in char_indices:
                    # If the current index is between index 4 and index 8 (inclusive)
                    if 4 <= j <= 8:
                        # Get a list of all indices where the character appears in the string before the current index
                        char_indices_before = [i for i, x in enumerate(string[:j]) if x == char_lower]
                        # If there are at least three indices where the character appears in the string before the current index
                        if len(char_indices_before) >= 3:
                            # Get a list of all indices where the character appears in the string after the current index
                            char_indices_after = [i for i, x in enumerate(string[j+1:]) if x == char_lower]
                            # If there are at least three indices where the character appears in the string after the current index
                            if len(char_indices_after) >= 3:
                                # Get a list of all palindromes of length at least 3 that can be formed using the character at the current index and the characters before and after it
                                palindromes.update([string[k:j+1][::-1] for k in range(j-2, -1, -1) if string[k:j+1].isalnum()])
    return palindromes
