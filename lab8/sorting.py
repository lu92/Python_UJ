""" Sorting algorithms """
# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
#
# modified for use in UJ python course
import random



class SelectionSort(object):
    """ The selection sort """
    def __call__(self, given_list):

        # Loop through the entire array
        for cur_pos in range(0, len(given_list)):
            # Find the position that has the smallest number
            # Start with the current position
            min_pos = cur_pos

            # Scan left to right (end of the list)
            for scan_pos in range(cur_pos + 1, len(given_list)):

                # Is this position smallest?
                if self.is_this_position_smallest(given_list, scan_pos, min_pos):
                    # It is, mark this position as the smallest
                    min_pos = scan_pos

            self.swap(given_list, min_pos, cur_pos)

    @staticmethod
    def swap(given_list, min_pos, cur_pos):
        """ Swap the two values
        :param given_list: given_list
        :param min_pos: min_pos
        :param cur_pos: cur_pos
        :return: nothing
        """
        temp = given_list[min_pos]
        given_list[min_pos] = given_list[cur_pos]
        given_list[cur_pos] = temp

    @staticmethod
    def is_this_position_smallest(given_list, scan_pos, min_pos):
        """
        :return: g
        """
        return bool(given_list[scan_pos] < given_list[min_pos])

class InsertionSort:
    """ The Insertion sort """
    def __call__(self, given_list):
        # Start at the second element (pos 1).
        # Use this element to insert into the
        # list.
        for key_pos in range(1, len(given_list)):

            # Get the value of the element to insert
            key_value = self.get_value(given_list, key_pos)

            # Scan from right to the left (start of list)
            scan_pos = key_pos - 1

            # Loop each element, moving them up until
            # we reach the position the
            scan_pos = self.inner_loop(given_list, key_value, scan_pos)

            # Everything's been moved out of the way, insert
            # the key into the correct location
            given_list[scan_pos + 1] = key_value

    @staticmethod
    def get_value(given_list, key_pos):
        """
        Get the value of the element to insert
        :param given_list:
        :param key_pos:
        :return:
        """
        return given_list[key_pos]

    @staticmethod
    def inner_loop(given_list, key_value, scan_pos):
        """
        Loop each element, moving them up until
        we reach the position the
        :param given_list:
        :param key_value:
        :param scan_pos:
        :return:
        """
        while (scan_pos >= 0) and (given_list[scan_pos] > key_value):
            given_list[scan_pos + 1] = given_list[scan_pos]
            scan_pos = scan_pos - 1
        return scan_pos



def print_list(given_list):
    """ This will point out a list """
    for item in given_list:
        print("%3d" % item)
    print()


if __name__ == '__main__':
    # Create two lists of the same random numbers
    LIST1 = []
    LIST2 = []
    LIST_SIZE = 10
    for i in range(LIST_SIZE):
        new_number = random.randrange(100)
        LIST1.append(new_number)
        LIST2.append(new_number)

    # Print the original list
    print_list(LIST1)

    # Use the selection sort and print the result
    print("Selection Sort")
    SelectionSort()(LIST1)
    print_list(LIST1)

    # Use the insertion sort and print the result
    print("Insertion Sort")
    InsertionSort()(LIST2)
    print_list(LIST2)
