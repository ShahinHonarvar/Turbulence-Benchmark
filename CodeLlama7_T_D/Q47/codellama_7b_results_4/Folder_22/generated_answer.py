
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start = 100
    end = 200
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate through each character in the substring
    for i in range(start, end + 1):
        # Check if the current character is a letter (a-z or A-Z)
        if string[i].isalpha():
            # Define the left and right sides of the palindrome
            left = i - 1
            right = i + 1
            # Iterate through each character in the substring for the left and right sides of the palindrome
            while left >= start and string[left].isalpha():
                if string[left] != string[right]:
                    break
                left -= 1
                right += 1
            # If the left and right sides of the palindrome are not equal, add it to the set of palindromes
            if left < start or string[left] != string[right]:
                palindromes.add(string[i])
    return palindromes
