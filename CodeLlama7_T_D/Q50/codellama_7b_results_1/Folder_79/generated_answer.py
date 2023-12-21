
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            # Check if the strings are anagrams by sorting their characters
            if sorted(my_list[i]) == sorted(my_list[j])):
                # Increment pair count if the strings are anagrams of length at least three
                if len(my_list[i]) >= 3 and len(my_list[j]) >= 3:
                    pair_count += 1
                    if pair_count >= 40:
                        return True
    return False
