
def palindromes_of_specific_lengths(string):
    # Define the range of indices to consider
    start_index = 18
    end_index = 88
    # Create an empty set to store the palindromes
    palindromes = set()
    # Iterate through each index in the range
    for i in range(start_index, end_index + 1):
        # Check if the character at the current index is a letter
        if string[i].isalpha():
            # Define the palindrome by checking both sides of the current index
            left = i - 1
            right = i + 1
            while left >= start_index and right <= end_index:
                # Check if the characters on either side of the current index match
                if string[left].lower() == string[right].lower():
                    # If they do, add the palindrome to the set
                    palindromes.add(string[i - 1 : i + 2])
                # Move one character to the left and right of the current index
                left -= 1
                right += 1

    return palindromes
