
def if_contains_anagrams(my_list):
    # Create a set of all possible anagrams of the English letters
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    anagram_set = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters)):
            anagram_set.add((english_letters[i] + english_letters[j]).lower())
    # Initialize a counter to keep track of the number of pairs of anagrams found
    counter = 0

    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if my_list[i].lower() == my_list[j].lower():
                # If the strings are anagrams of each other, increase the counter by one
                counter += 1

    return counter <= 47
