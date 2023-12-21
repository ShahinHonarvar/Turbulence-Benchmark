from Q31.codellama_7b_results_3.Folder_80.generated_answer import if_perfect_num


def test_list_of_ones():
    initial_list = [1 for _ in range((746 + 1) * 2)]
    assert not if_perfect_num(initial_list)


def test_list_of_twos():
    initial_list = [2 for _ in range((746 + 1) * 2)]
    assert not if_perfect_num(initial_list)


def test_list_of_threes():
    initial_list = [3 for _ in range((746 + 1) * 2)]
    assert not if_perfect_num(initial_list)


def test_list_of_sixes():
    initial_list = [6 for _ in range((746 + 1) * 2)]
    assert if_perfect_num(initial_list)


def test_list_of_prime_numbers():
    initial_list = [2, 3, 5, 7, 11, 13, 17] * (746 + 1)
    assert not if_perfect_num(initial_list)


def test_list_of_perfect_numbers():
    initial_list = [6, 28, 496, 8128] * (746 + 1)
    assert if_perfect_num(initial_list)


def test_list_of_odd_numbers():
    initial_list = [i for i in range(1,3000,2)]
    assert not if_perfect_num(initial_list)


def test_list_of_non_perfects():
    initial_list = list(range(1, 6)) + list(range(7, 28)) + list(range(29, 496)) + list(range(497, 8128))
    assert not if_perfect_num(initial_list)


def test_multiples_of_ten():
    initial_list = [i * 10 for i in range(1, (746 + 1) * 2)]
    assert not if_perfect_num(initial_list)

    
    