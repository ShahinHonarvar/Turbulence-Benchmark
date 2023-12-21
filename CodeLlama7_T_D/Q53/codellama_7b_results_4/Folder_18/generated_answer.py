 def palindrome_of_length_at_least_n(string, n):
    # create a set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(len(string)):
        # get the character at index i
        char = string[i]
        # check if the character is an English letter
        if char.isalpha():
            # create a variable to store the palindrome
            palindrome = ""
            # loop through each character in the string starting from index i
            for j in range(i, len(string)):
                # get the character at index j
                char2 = string[j]
                # check if the character is an English letter
                if char2.isalpha():
                    # add the character to the palindrome
                    palindrome += char2
            # check if the palindrome has a length greater than or equal to n
            if len(palindrome) >= n:
                # check if the palindrome is a palindrome in a case-insensitive manner
                if palindrome == palindrome[::-1]:
                    # add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # return the set of palindromes
    return palindromes
