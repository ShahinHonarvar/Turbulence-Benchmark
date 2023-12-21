from Q27.command_results_5.Folder_64.generated_answer import insert_after_index



def test_presence_of_inserted_element():
    initial_list = [set() for i in range((8 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert [3, 8] in returned_list


def test_index_of_inserted_element():
    initial_list = [i for i in range((8 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    indices = []
    for index, value in enumerate(returned_list):
        if value == [3, 8]:
            indices.append(index)
    assert returned_list.index([3, 8]) in indices


def test_presence_of_inserted_element_at_index_8():
    initial_list = [i for i in range((8 + 1) * 2)]
    returned_list = insert_after_index(initial_list)
    assert returned_list[8 + 1] == [3, 8]


def test_list_of_particular_size():
    if 8 == 0:
        initial_list = [1, 2]
    else:
        initial_list = [1] * (8 + 2)

    returned_list = insert_after_index(initial_list)
    assert returned_list[-2] == [3, 8]


def test_size_of_returned_list():
    initial_list = [i for i in range((8 + 1) * 2)]
    x = len(initial_list)
    returned_list = insert_after_index(initial_list)
    assert len(returned_list) == x + 1
