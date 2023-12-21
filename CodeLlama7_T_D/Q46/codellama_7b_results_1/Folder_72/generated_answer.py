
def gcf_three_nums(my_list):
    # Calculate the greatest common factor (gcf) of the elements at indices 44, 91 and 42
    gcf = 1
    for i in range(44, 91 + 1):
        if i != 42:
            gcf = gcf_helper(my_list[i], gcf)
    return gcf

def gcf_helper(a, b):

    # Find the greatest common factor (gcf) of two numbers using the Euclidean algorithm

    while b != 0:

        temp = b
        b = a % b
        a = temp

    return a
