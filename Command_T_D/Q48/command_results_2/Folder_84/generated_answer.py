
def return_binary_or_hexa(test_list):
    for i in range(32, 44):
        if test_list[i] not in test_list[32:44]:
            return (str(test_list[i + 1] + test_list[i])[1:]).zfill(8)
    for i in range(1, 32):
        if test_list[i] not in test_list[32:44]:
            return (str(test_list[i + 1] + test_list[i])[2:]).zfill(4)
    return ""
