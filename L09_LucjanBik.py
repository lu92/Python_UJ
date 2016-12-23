import numpy.random
import timeit
import math


# zad1

gen_classic_way = timeit.timeit('list1 = [random.randint(-100,100) for p in range(1000)]\nfor i in range(1000):\n\tlist1.__setitem__(i, list1.__getitem__(i)+1)', setup = 'import random', number=10)
print("#1 classic way: " + str(gen_classic_way))

gen_numpy_way = timeit.timeit('list2 = numpy.random.random_sample(1000)\nfor i in range(1000):\n\tlist2.__setitem__(i, list2.__getitem__(i)+1)', setup = 'import numpy', number=10)
print("#1 numpy way  : " + str(gen_numpy_way))


# zad2

def calculate_sin_cos_classic_way(list):
    calculated_values = []
    for x in list:
        calculated_values.append(math.sin(x) + math.cos(x))
    return calculated_values

def calculate_sin_cos_numpy_way(list):
    calculated_values = []
    for x in list:
        calculated_values.append(numpy.sin(x) + numpy.cos(x))
    return calculated_values

gen_classic_way = timeit.timeit('calculate_sin_cos_classic_way([random.randint(-10,10) for p in range(1000)])', setup = 'import random, math; from __main__ import calculate_sin_cos_classic_way', number=10)
print("#2 classic way: " + str(gen_classic_way))

gen_classic_way = timeit.timeit('calculate_sin_cos_numpy_way(numpy.random.random_sample(1000))', setup = 'import math, numpy; from __main__ import calculate_sin_cos_numpy_way', number=10)
print("#2 numpy way  : " + str(gen_classic_way))

# zad3

def cube_sum(x):
    """Zwraca sume szescianow elementow"""
    result = 0
    for i in range(len(x)):
        result += x[i] ** 3
    return result

def numpy_cube_sum(number_list):
    return numpy.sum(numpy.power(number_list, 3))


def almost_variance(x):
    """Oblicza 1/n * SUM (x_i - mean(x))^4"""
    m = sum(x) / len(x)
    result = 0
    for i in range(len(x)):
        result += (x[i] - m) ** 4
    result /= len(x)
    return result

def numpy_almost_variance(x):
    m = sum(x) / len(x)
    elems = numpy.array(x)
    elems = numpy.power(numpy.subtract(elems, m), 4)
    result = numpy.sum(elems)
    result /= len(x)
    return result

zad_3_default_cube_sum = timeit.timeit('cube_sum([x for x in range(500)])',
    setup = 'from __main__ import cube_sum', number=10)
print("#3 default sum cube: " + str(zad_3_default_cube_sum))

zad_3_numpy_cube_sum = timeit.timeit('numpy_cube_sum([x for x in range(500)])',
    setup = 'from __main__ import numpy_cube_sum', number=10)
print("#3 numpy sum cube  : " + str(zad_3_numpy_cube_sum))


zad_3_default_almost_variance = timeit.timeit('almost_variance([x for x in range(500)])',
    setup = 'from __main__ import almost_variance', number=10)
print("#3 default almost variance: " + str(zad_3_default_almost_variance))

zad_3_numpy_almost_variance = timeit.timeit('numpy_almost_variance([x for x in range(500)])',
    setup = 'from __main__ import numpy_almost_variance', number=10)
print("#3 numpy almost variance  : " + str(zad_3_numpy_almost_variance))




# zad4
print("#4 " + str((numpy.arange(100)+1).reshape((10, 10))))

# zad5

def euclidean_distance(A, B):
    return numpy.sum(numpy.power(numpy.subtract(A, B), 2))


matrix = numpy.random.random_integers(1000, size=(100,10))

print("#5 distance between\n" + str(matrix[1]) + " and \n" + str(matrix[2])+ " is: " + str(euclidean_distance(matrix[1],matrix[2])))

print("#5 euclidean distance: " + str(euclidean_distance([3, 4, 5], [1, 2, 3])))

# zad6

def white(X):
    return numpy.divide(numpy.subtract(X, numpy.mean(X, axis=0)), numpy.std(X, axis=0))

print("#6\n" + str(white(numpy.arange(0,10).reshape(5, 2))))

# zad7

# def closest(x, number_list):
#
#     if any(not isinstance(i, list) for i in number_list):
#         number_list = list(map(lambda e: [e], number_list))
#
#     vectors = numpy.power(numpy.subtract(x, number_list), 2)
#     all_distances = numpy.sqrt(numpy.sum(vectors, axis=1))
#     min_distance = numpy.min(all_distances)
#     index = numpy.argwhere(all_distances == min_distance)[0][0]
#     return number_list[index]


def closest(x, number_list):
    vectors = numpy.power(numpy.subtract(x, number_list), 2)
    all_distances = []
    for vec in vectors:
        all_distances.append(numpy.sum(vec))
    min_distance = numpy.min(all_distances)
    index = numpy.argwhere(all_distances == min_distance)[0][0]
    return number_list[index]

print("#7 " + str(closest(1.5, [1, -4, 3])))
print("#7 " + str(closest([1.5, 0], [[1, 0], [-4, 0], [3, 0]])))
