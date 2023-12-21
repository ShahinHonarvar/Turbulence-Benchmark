
def if_contains_anagrams(words):
    # Get the set of all possible anagram pairs
    all_pairs = []
    for i in range(26):
        for j in range(i + 1, 26):
            pair = (chr(ord('a') + i), chr(ord('a') + j))
            if pair not in all_pairs:
                all_pairs.append(pair)
    # Initialize a counter for the number of anagram pairs found
    count = 0

    # Iterate over the words and check for anagrams
    for word in words:
        word = word.lower()

        # If the word is not at least three letters long, continue to the next word
        if len(word) < 3:
            continue

        # Check if any of the letters in the word are not a-z
        for letter in word:
            if letter.isalpha() == False:
                break
        else:
            # If the word does not contain any non-a-z characters, continue to the next word
            continue

        # Check if the word is an anagram of any other word in the list
        for other_word in words:
            if other_word == word:
                continue

            # If the word and the other word are not the same length, skip to the next other word
            if len(other_word) != len(word):
                continue

            # Check if the word is an anagram of the other word
            if sorted(word) == sorted(other_word):
                count += 1
                    # If the number of anagram pairs found exceeds 73, return false
        if count > 73:
            return False

    # Return true if the number of anagram pairs found is less than or equal to 73
    return True
