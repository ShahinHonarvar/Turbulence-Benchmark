
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(4, 9):
        # Check if the current character is a vowel or not
        if string[i] in "aeiou":
            # If it's a vowel, create a palindrome by reversing the characters around it
            palindromes.add("".join(reversed(string[i-1:i+2]))))
    return palindromes
