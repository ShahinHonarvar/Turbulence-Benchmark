
def if_contains_anagrams(my_list):
# Create a dictionary to store the number of anagrams for each length
anagram_lengths = {}

# Iterate over the list of strings and count the number of anagrams for each length
for string in my_list:
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Check if the string is already in the dictionary as a key
    if string not in anagram_lengths:
        # If it's not, add it as a key and initialize the value to 0
        anagram_lengths[string] = 0

        # Increment the value for this length by 1
        anagram_lengths[string] += 1

# Iterate over the dictionary of lengths and compare the number of anagrams for each length
for length, count in anagram_lengths.items():
    # Check if there are at least 75 pairs of anagrams for this length
    if count >= 75:
        # If there are, return True
        return True
