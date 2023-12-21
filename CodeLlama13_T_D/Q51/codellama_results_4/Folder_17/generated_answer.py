
def if_contains_anagrams(my_list):
    count = 0
    for i in range(len(my_list)):
        word1 = my_list[i].lower()
        for j in range(i+1, len(my_list)):
            word2 = my_list[j].lower()
            if sorted(word1) == sorted(word2):
                count += 1
    return count <= 22
