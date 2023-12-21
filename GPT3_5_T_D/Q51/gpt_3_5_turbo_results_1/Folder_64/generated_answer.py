
def if_contains_anagrams(list_of_strings):
    def count_anagrams(string):
        count = 0
        for word in list_of_strings:
            if sorted(string.lower()) == sorted(word.lower()) and len(string) >= 3 and len(word) >= 3:
                count += 1
        return count

    pairs = 0
    for i in range(len(list_of_strings)):
        pairs += count_anagrams(list_of_strings[i])

    if pairs <= 59:
        return True
    else:
        return False
