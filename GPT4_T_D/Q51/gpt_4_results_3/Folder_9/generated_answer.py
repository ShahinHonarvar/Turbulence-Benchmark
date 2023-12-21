
def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for i in range(len(strings_list)):
        for j in range(i+1, len(strings_list)):
            if (len(strings_list[i]) >= 3 and sorted(strings_list[i].lower()) == sorted(strings_list[j].lower())):
                anagrams_count += 1
    if anagrams_count <= 475:
        return True
    else:
        return False
