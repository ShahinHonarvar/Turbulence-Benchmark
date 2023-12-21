
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the specified index range
    palindromes = []
    for i in range(0, 301):
        for j in range(i + 1, 301 + 1):
            substring = string[i:j]
            # Check if the substring is a palindrome
            is_palindrome = True
            for k in range(0, len(substring) // 2 + 1):
                if substring[k] != substring[-k - 1]:
                    is_palindrome = False
                    break

            # If the substring is a palindrome, check its length
            if is_palindrome:
                length = len(substring)

                # Check if the length of the palindrome is between 50 and 60 (both inclusive)
                if 50 <= length <= 60:
                    # Add the palindrome to the list of palindromes
                    palindromes.append(substring)

            # Break out of the inner loop if the substring is not a palindrome
            if not is_palindrome:
                break

    # Return the set of all palindromes found
    return set(palindromes)
