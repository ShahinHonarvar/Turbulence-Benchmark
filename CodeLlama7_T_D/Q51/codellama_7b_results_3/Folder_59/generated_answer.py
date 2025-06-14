
def if_contains_anagrams(string_list):
    # Create a dictionary to store the counts of each letter
    letter_counts = {}

    for string in string_list:
        # Convert the string to lowercase
        string = string.lower()

        # Iterate through each character in the string
        for char in string:
            # If the character is a letter, increment its count in the dictionary
            if char.isalpha():
                if char not in letter_counts:
                    letter_counts[char] = 1
                else:
                    letter_counts[char] += 1

    # Iterate through each pair of anagrams and compare them case-insensitively
    for i in range(len(string_list) - 1):
        string1 = string_list[i]
        for j in range(i + 1, len(string_list))):
            string2 = string_list[j]
            if sorted(string1.lower()) == sorted(string2.lower()):
                return True

    # If no anagrams are found, return False
    return False
