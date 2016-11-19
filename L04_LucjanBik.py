from time import sleep, time
import os
import copy


class LoggingTime:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        self.start_time = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.durationTime = time() - self.start_time
        with open(self.file, "w") as fileDescriptor:
            fileDescriptor.write(str(self.durationTime))


# for valid in range(6):
#     with LoggingTime('tmp.txt'):
#         sleep(valid)
#
#     with open('tmp.txt') as fh:
#         value = float(fh.read())
#         print('Took %fs, should take %ds, is it ok? %s' % (value, valid, round(value) == round(valid)))
#
#     os.remove('tmp.txt')


class Fibonnaci:
    def __init__(self):
        self.fib = 0
        self.last = -1

    def next_value(self):
        if self.last == -1:
            self.last = 0
            self.fib = 1
        else:
            self.last, self.fib = self.fib, self.fib + self.last
        return self.fib

    def current_value(self):
        return self.fib


class Shifted:
    def __init__(self, func, shift):
        self.function = copy.copy(func)
        self.shift = shift

    def __enter__(self):
        for i in range(self.shift):
            self.function.next_value()

        return self.function

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

F = Fibonnaci()
x = F.next_value()

with Shifted(F, 0) as fib:
    for i, v in zip(range(1, 10), [1, 2, 3, 5, 8, 13, 21, 34, 55]):
        f = fib.next_value()
        print("Iteration %d\t Value %d \t Valid %s" % (i, f, f == v))

# Teraz F powinno dalej wskazywac na x
print('Is F still correct? %s' % (x == F.current_value()))

with Shifted(F, 9) as fib:
    for i, v in zip(range(1, 10), [89, 144, 233, 377, 610, 987, 1597, 2584, 4181]):
        f = fib.next_value()
        print("Iteration %d\t Value %d \t Valid %s" % (i, f, f == v))


class BagOfWords:
    pass
