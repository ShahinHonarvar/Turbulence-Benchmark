
def palindromes_of_specific_lengths(string):
    # Define the substring range for palindromes
    sub_str = string[26:84]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(sub_str)):
        # Check if the current character is a letter (a-zA-Z)
        if sub_str[i].isalpha():
            # Define the starting and ending indices of the palindrome
            start = i
            end = i

            # Iterate over each character in the substring from the current index to the end of the substring
            for j in range(i, len(sub_str)):
                # Check if the current character is a letter (a-zA-Z)
                if sub_str[j].isalpha():
                    # Increment the ending index
                    end = j + 1

                    # Check if the palindrome has the required length
                    if end - start == 30 or end - start == 46:
                        # Define a list to store the characters of the palindrome in reverse order
                        rev_list = []

                        # Iterate over each character in the substring from the starting index to the ending index
                        for k in range(start, end):
                            # Add each character to the list in reverse order
                            rev_list.append(sub_str[k])

                        # Join the characters of the palindrome in reverse order to form a string
                        palindrome = "".join(rev_list)

                        # Check if the palindrome is case-insensitive and has the required length
                        if palindrome.lower() == palindrome and end - start >= 30 and end - start <= 46:
                            # Add the palindrome to the set of palindromes
                            palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
