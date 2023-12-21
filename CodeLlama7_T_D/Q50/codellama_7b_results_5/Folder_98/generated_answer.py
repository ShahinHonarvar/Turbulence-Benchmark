
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize variables
    count = 0
    anagram_length = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]

        # Check if the current string is a palindrome
        if is_palindrome(curr_string):
            # Increment the count by one
            count += 1

    # Check if the count is greater than or equal to seven
    if count >= 7:
        return True

    else:
        return False

def is_palindrome(string):

    # Convert the string to lowercase
    string = string.lower()

    # Check if the string is a palindrome
    if string == string[::-1]:
        return True

    else:
        return False
