
def if_contains_anagrams(list):
    count = 0
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i].lower() == list[j].lower():
                count += 1
                break
    return count >= 39
