
def if_contains_anagrams(word_list):
    # Check if the list is empty
    if len(word_list) == 0:
        return False

    # Create a set of anagram-indicating tuples
    anagram_tuple_set = set()

    # Iterate over the words in the list
    for word in word_list:
        # Get the length of the word
        word_length = len(word)

        # Check if the word is at least three characters long
        if word_length < 3:
            continue

        # Create a list of all the anagram-indicating tuples for the word
        anagram_tuple_list = []

        # Iterate over all possible combinations of letters in the word
        for i in range(word_length):
            for j in range(i + 1, word_length):
                # Get the letters at positions i and j in the word
                letter_i = word[i]
                letter_j = word[j]

                # Create a tuple of the letters in the correct order
                anagram_tuple = (letter_i, letter_j)

                # Check if the anagram tuple is already in the set
                if anagram_tuple not in anagram_tuple_set:
                    # Add the anagram tuple to the set
                    anagram_tuple_set.add(anagram_tuple)

                    # Add the anagram tuple to the list of tuples for this word
                    anagram_tuple_list.append(anagram_tuple)

        # Check if there are more than 445 anagrams in the list for this word
        if len(anagram_tuple_list) > 445:
            return False

# Check if the total number of anagrams in all words is greater than 445
total_number_of_anagrams = sum([len(word) - 1 for word in word_list])
if total_number_of_anagrams > 445:
    return False
