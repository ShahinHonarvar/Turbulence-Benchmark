
def gcf_three_nums(num_list):
    def calculate_gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    num1 = num_list[47]
    num2 = num_list[10]
    num3 = num_list[28]

    gcf_1_2 = calculate_gcf(num1, num2)
    gcf = calculate_gcf(gcf_1_2, num3)

    return gcf
