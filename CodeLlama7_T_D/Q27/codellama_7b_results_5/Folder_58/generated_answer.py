
def insert_after_index(my_list):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if i == 598:
            new_list.insert(i + 1, [385, 999])
            break

    return new_list
