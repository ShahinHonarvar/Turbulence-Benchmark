
def if_contains_anagrams(word_list):
    # Initialize variables for counting anagrams
    anagram_count = 0
    # Iterate over each word in the list
    for i in range(len(word_list)):
        # Get the current word and its length
        word = word_list[i]
        length = len(word)
        # Check if the word has at least three letters
        if length >= 3:
            # Convert the word to lowercase
            word = word.lower()
            # Create a list of all possible anagrams of the word
            anagram_list = []
            for j in range(length):
                # Get the first letter of the word
                letter = word[j]
                # Remove the first letter from the word
                new_word = word[:j] + word[j+1:]
                # Create a list of all possible anagrams of the new word
                new_anagram_list = []
                for k in range(length):
                    # Get the first letter of the new word
                    new_letter = new_word[k]
                    # Remove the first letter from the new word
                    new_new_word = new_word[:k] + new_word[k+1:]
                    # Add the anagram to the list
                    new_anagram_list.append(new_new_word)
                # Combine the two lists of anagrams
                anagram_list.extend(new_anagram_list)
            # Remove duplicates from the list of anagrams
            unique_anagram_list = set(anagram_list)
            # Count the number of anagrams in the list
            anagram_count += len(unique_anagram_list)
    # Return True if there are at most 86 pairs of anagrams in the given list, otherwise return False
    if anagram_count <= 86:
        return True
    else:
        return False
