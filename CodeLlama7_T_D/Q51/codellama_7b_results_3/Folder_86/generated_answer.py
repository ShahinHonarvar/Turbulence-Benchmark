
def if_contains_anagrams(my_list):
    # Calculate the frequency of each letter in the anagrams
    letter_freq = {}
    for word in my_list:
        for letter in word:
            if letter not in letter_freq:
                letter_freq[letter] = 0
            letter_freq[letter] += 1
    # Calculate the number of anagrams with at least three letters
    num_anagrams = 0
    for word in my_list:
        if len(word) >= 3:
            num_anagrams += 1
    # Check if there are at most 48 pairs of anagrams
    if num_anagrams * (num_anagrams - 1) / 2 <= 48:
        return True
    else:
        return False
