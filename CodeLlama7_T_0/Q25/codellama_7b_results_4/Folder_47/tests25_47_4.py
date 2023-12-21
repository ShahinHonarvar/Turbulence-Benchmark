from Q25.codellama_7b_results_4.Folder_47.generated_answer import insert_at_index


def test_presence_of_inserted_element():
    initial_list = [set() for i in range((64 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert 520.11 in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((64 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == 520.11:
            indices.append(index)
    assert returned_list.index(520.11) in indices


def test_presence_of_inserted_element_at_index_64():
    initial_list = [i for i in range((64 + 1) * 2)]
    returned_list = insert_at_index(initial_list)
    assert returned_list[64] == 520.11


def test_list_of_particular_size():
    if 64 == 0:
        initial_list = [1]
    else:
        initial_list = [1] * (64 + 1)

    returned_list = insert_at_index(initial_list)
    assert returned_list[-2] == 520.11


def test_size_of_returned_list():
    initial_list = [i for i in range((64 + 1) * 2)]
    initial_list_copy = initial_list.copy()
    returned_list = insert_at_index(initial_list)
    assert len(returned_list) == len(initial_list_copy) + 1

        

