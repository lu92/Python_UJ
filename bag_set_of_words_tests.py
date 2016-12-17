import unittest
from bag_set_of_words import SetOfWords
from bag_set_of_words import BagOfWords


class BagOfWordsTests(unittest.TestCase):

    def test_iter_empty_bow(self):
        bow = BagOfWords("")
        iterations = list(bow.__iter__())
        self.assertEquals(iterations, [''])

    def test_iter_doubled_word(self):
        bow = BagOfWords("ala ala")
        iterations = list(bow.__iter__())
        self.assertEquals(iterations, ['ala'])

    def test_iter_proper_data(self):
        bow = BagOfWords("ala ma kota ala ma ala")
        iterations = list(bow.__iter__())
        self.assertEquals(iterations, ['ala', 'ma', 'kota'])

    def test_get_item_which_does_not_exist(self):
        bow = BagOfWords("")
        self.assertIsNone(bow.__getitem__('ala'))

    def test_get_item_which_does_exist(self):
        bow = BagOfWords("ala")
        self.assertEquals(1, bow.__getitem__('ala'))

    def test_get_item_which_is_tripled(self):
        bow = BagOfWords("ala ala ala")
        self.assertEquals(3, bow.__getitem__('ala'))

    def test_set_item_when_item_does_not_exist(self):
        bow = BagOfWords("")
        bow.__setitem__('ala', 10)
        self.assertIsNone(bow.__getitem__('ala'))

    def test_set_item_when_item_is_single(self):
        bow = BagOfWords("ala")
        bow.__setitem__('ala', 10)
        self.assertEquals(10, bow.__getitem__('ala'))

    def test_set_item_when_item_is_tripled(self):
        bow = BagOfWords("ala ala ala")
        bow.__setitem__('ala', 10)
        self.assertEquals(10, bow.__getitem__('ala'))

    def test_add_two_empty_bows(self):
        empty_bow1 = BagOfWords("")
        empty_bow2 = BagOfWords("")
        merged_bow = empty_bow1.__add__(empty_bow2)
        self.assertEquals([''], list(merged_bow.__iter__()))

    def test_add_empty_and_filled_bow(self):
        empty_bow = BagOfWords("")
        filled_bow = BagOfWords("ala ala ala")
        merged_bow = empty_bow.__add__(filled_bow)
        self.assertEquals(3, merged_bow.__getitem__('ala'))

    def test_add_two_filled_bows(self):
        filled_bow1 = BagOfWords("ala ma kota ala ma ala")
        filled_bow2 = BagOfWords("ala ala ala")
        merged_bow = filled_bow1.__add__(filled_bow2)
        self.assertEquals(6, merged_bow.__getitem__('ala'))
        self.assertEquals(2, merged_bow.__getitem__('ma'))
        self.assertEquals(1, merged_bow.__getitem__('kota'))

    def test_str_empty_bow(self):
        bow = BagOfWords('')
        self.assertEquals(':1', bow.__str__())

    def test_str_filled_bow_tripled_word(self):
        bow = BagOfWords("ala ala ala")
        self.assertEquals("ala:3", bow.__str__())

    def test_str_filled_bow(self):
        bow = BagOfWords("ala ma kota ala ma ala")
        self.assertEquals("ala:3, ma:2, kota:1", bow.__str__())

    def test_init_by_text(self):
        bow = BagOfWords("ala ma kota ala ma ala")
        self.assertEquals("ala:3, ma:2, kota:1", bow.__str__())

    def test_init_by_file(self):
        bow = BagOfWords(open("plik.txt"))
        self.assertEquals("ala:3, ma:2, kota:1", bow.__str__())

    def test_init_by_empty_file(self):
        bow = BagOfWords(open("empty_plik.txt"))
        self.assertEquals(":1", bow.__str__())


class SetOfWordsTests(unittest.TestCase):

    def test_str_empty_bow(self):
        sow = SetOfWords('')
        self.assertEquals('', sow.__str__())

    def test_str_filled_bow_tripled_word(self):
        sow = SetOfWords("ala ala ala")
        self.assertEquals("ala", sow.__str__())

    def test_str_filled_bow(self):
        sow = SetOfWords("ala ma kota ala ma ala")
        self.assertEquals("ala, ma, kota", sow.__str__())

    def test_init_by_text(self):
        sow = SetOfWords("ala ma kota ala ma ala")
        self.assertEquals("ala, ma, kota", sow.__str__())

    def test_init_by_file(self):
        bow = SetOfWords(open("plik.txt"))
        self.assertEquals("ala, ma, kota", bow.__str__())

    def test_init_by_empty_file(self):
        sow = SetOfWords(open("empty_plik.txt"))
        self.assertEquals("", sow.__str__())
