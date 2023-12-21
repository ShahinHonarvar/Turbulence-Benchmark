
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string is at least three letters long
        if len(lowercase_string) >= 3:
            three_or_more_letters = True
            # Create a list of all the anagrams of the English letters in the string
            anagram_list = []
            for letter in "abcdefghijklmnopqrstuvwxyz":
                anagram_list.append(letter * len(lowercase_string)))
            # Check if there are at most 98 pairs of anagrams in the list
            for i in range(len(anagram_list) - 1):
                for j in range(i + 1, len(anagram_list)):
                    if anagram_list[i] == anagram_list[j]:
                        anagram_count += 1
            # If there are at most 98 pairs of anagrams in the list, return True
            if anagram_count <= 98:
                return True
    # If there are no three or more letter strings in the list, return False
    if not three_or_more_letters:
        return False
