
def palindromes_of_specific_lengths(string):
    # Define the substring range
    start_index = 28
    end_index = 94

    # Create a list of all possible palindromes within the substring range
    palindromes = []

    for i in range(start_index, end_index + 1):
        for j in range(i, end_index + 1):
            substring = string[i:j]
            if is_palindrome(substring) and len(substring) in range(38, 50):
                palindromes.append(substring)
    return set(palindromes)

def is_palindrome(string):

    # Check if the string is equal to its reverse

    return string == string[::-1]
