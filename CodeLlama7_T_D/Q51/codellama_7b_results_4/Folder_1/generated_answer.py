
def if_contains_anagrams(words):
    # Count the number of anagram pairs in the list
    count = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                count += 1
                    # If there are more than 30 anagram pairs in the list, return False
    if count > 30:
        return False

    else:

        return True
