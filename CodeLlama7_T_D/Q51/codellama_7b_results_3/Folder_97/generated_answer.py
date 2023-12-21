
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Create a list of all the letters in the string
            letter_list = [char for char in lowercase_string]

            # Sort the list of letters
            sorted_letter_list = sorted(letter_list)

            # Join the sorted list of letters into a single string
            anagram = "".join(sorted_letter_list)

            # Check if the anagram is in the dictionary of anagram counts
            if anagram in anagram_counts:
                # If it is, increment its count
                anagram_counts[anagram] += 1
            else:
                # If it's not, add it to the dictionary with a count of one
                anagram_counts[anagram] = 1

    # Loop through each pair of anagrams in the dictionary
    for (anagram1, count1), (anagram2, count2) in zip(anagram_counts.items(), anagram_counts.items()):
        # Check if the two anagrams are not equal and have at least one letter in common
        if anagram1 != anagram2 and len(set(anagram1).intersection(anagram2)) > 0:
            # If they are not equal and have at least one letter in common, return false
            return False

    # If no pair of anagrams was found that were not equal and had at least one letter in common, return true
    return True
