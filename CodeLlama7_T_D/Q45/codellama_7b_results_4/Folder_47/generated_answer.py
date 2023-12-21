
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string) - 2):
        # Check if the character at index i is a vowel
        if string[i] in "aeiou":
            # Get the indices of the letters before and after the vowel
            left_index = i - 1
            right_index = i + 1
            # Check if the letters before and after the vowel are also vowels
            if string[left_index] in "aeiou" and string[right_index] in "aeiou":
                # Get the substring that includes the vowel and its surrounding letters
                sub_string = string[left_index:right_index + 1]
                # Check if the substring is a palindrome
                if sub_string == sub_string[::-1]:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(sub_string)
    # Return the set of palindromes
    return palindromes
