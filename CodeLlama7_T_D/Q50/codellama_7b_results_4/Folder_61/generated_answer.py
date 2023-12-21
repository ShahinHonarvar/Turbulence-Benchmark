
def if_contains_anagrams(wordlist):
    # Count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(wordlist)):
        for j in range(i + 1, len(wordlist))):
            if sorted(wordlist[i]) == sorted(wordlist[j])):
                anagram_count += 1

    # Return true if there are at least 8 pairs of anagrams in the list; otherwise, return false
    return anagram_count >= 8
