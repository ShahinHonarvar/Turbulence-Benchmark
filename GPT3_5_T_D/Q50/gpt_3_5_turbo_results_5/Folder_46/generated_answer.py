
def if_contains_anagrams(strings_list):
    count = 0
    for i in range(len(strings_list)):
        for j in range(i+1, len(strings_list)):
            if sorted(strings_list[i].lower()) == sorted(strings_list[j].lower()) and len(strings_list[i]) >= 3:
                count += 1
    return count >= 38
