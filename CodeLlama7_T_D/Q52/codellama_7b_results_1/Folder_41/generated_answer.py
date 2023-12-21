
def palindrome_of_length_n(string):
    # Split the string into individual characters
    chars = list(string)

    # Create a set to store all palindromes of length n
    palindromes = set()

    # Loop through each substring of length n in the input string
    for i in range(len(chars) - 59):
        substring = "".join(chars[i:i+60])

        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            palindromes.add(substring)

    return palindromes
