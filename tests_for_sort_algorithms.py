import random
import unittest
import sorting

class InsertionSortTestCases(unittest.TestCase):

    def test_empty_list(self):
        test_list = []
        self.assertEquals(sorting.insertion_sort()(test_list), None)

    def test_single_element(self):
        test_list = [1]
        sorting.insertion_sort()(test_list)
        self.assertEquals(test_list, [1])

    def test_sequence_of_numbers(self):
        N = 20
        test_list = []
        for i in range(N):
            test_list.append(random.randint(-100, 100))
        expected_list = sorted(test_list.copy(), key=int)
        sorting.insertion_sort()(test_list)
        self.assertEquals(test_list, expected_list)

    def test_single_literals(self):
        test_list = ['a']
        sorting.insertion_sort()(test_list)
        self.assertEquals(test_list, ['a'])

    def test_many_literals(self):
        N = 20
        test_list = []
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(N):
            test_list.append(random.choice(characters))
        expected_list = sorted(test_list)
        sorting.insertion_sort()(test_list)
        self.assertEquals(test_list, expected_list)


class SelectionSortTestCases(unittest.TestCase):

    def test_empty_list(self):
        test_list = []
        self.assertEquals(sorting.selection_sort()(test_list), None)

    def test_single_element(self):
        test_list = [1]
        sorting.selection_sort()(test_list)
        self.assertEquals(test_list, [1])

    def test_sequence_of_numbers(self):
        N = 20
        test_list = []
        for i in range(N):
            test_list.append(random.randint(-100, 100))
        expected_list = sorted(test_list.copy(), key=int)
        sorting.selection_sort()(test_list)
        self.assertEquals(test_list, expected_list)

    def test_single_literals(self):
        test_list = ['a']
        sorting.selection_sort()(test_list)
        self.assertEquals(test_list, ['a'])


    def test_many_literals(self):
        N = 20
        test_list = []
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(N):
            test_list.append(random.choice(characters))
        expected_list = sorted(test_list)
        sorting.selection_sort()(test_list)
        self.assertEquals(test_list, expected_list)
