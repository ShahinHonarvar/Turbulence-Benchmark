
def palindrome_of_length_at_least_n(input_string, n=7):
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each character in the input string
    for i in range(len(input_string)):
        # Check if the current character is a letter (a-z or A-Z)
        if input_string[i].isalpha():
            # Convert the current character to lowercase
            current_character = input_string[i].lower()
            # Loop through each character in the rest of the input string
            for j in range(i+1, len(input_string)):
                # Check if the next character is a letter (a-z or A-Z)
                if input_string[j].isalpha():
                    # Convert the next character to lowercase
                    next_character = input_string[j].lower()
                    # Check if the current character and the next character form a palindrome of length greater than or equal to n
                    if current_character == next_character:
                        # Add the palindrome to the set
                        palindromes.add(current_character + next_character)
    return palindromes
