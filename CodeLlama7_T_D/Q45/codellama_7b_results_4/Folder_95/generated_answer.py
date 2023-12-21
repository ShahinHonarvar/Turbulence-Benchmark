 def palindromes_between_indices(string):
    # initialize an empty set to store the palindromes
    palindromes = set()
    # loop through each character in the string
    for i in range(7, 9):
        # check if the current character is a letter
        if string[i].isalpha():
            # create a list of all the letters that occur before and after the current character
            left_letters = string[:i]
            right_letters = string[i+1:]
            # loop through each combination of letters in the left and right lists
            for j in range(26):
                for k in range(26):
                    # check if the current combination of letters forms a palindrome
                    if left_letters[j].lower() == right_letters[k].lower():
                        # add the palindrome to the set
                        palindromes.add((left_letters[j] + string[i] + right_letters[k]).lower()))
    return palindromes
