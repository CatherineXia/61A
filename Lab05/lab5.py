
from math import sqrt


def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer `this`.
    For each element in `i_list`, print the element if it is larger than `this`;
    otherwise, print the word "that".
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for i in range(len(i_list)):
        if i_list[i] <= this:
            print("that")
        else:
            print(i_list[i])


def couple(s1, s2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> s1 = [1, 2, 3]
    >>> s2 = [4, 5, 6]
    >>> couple(s1, s2)
    [[1, 4], [2, 5], [3, 6]]
    >>> s3 = ['c', 6]
    >>> s4 = ['s', '1']
    >>> couple(s3, s4)
    [['c', 's'], [6, '1']]
    """
    assert len(s1) == len(s2)
    return [[s1[i], s2[i]] for i in range(len(s1))]


def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.
    >>> enumerate([6, 1, 'a'])
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    new_s = []
    for i in range(len(s)):
        if start == 0:
            new_s.append([i, s[i]])
        else:
            new_s.append([start + i, s[i]])
    return new_s


def squares(s):
    """Returns a new list containing square roots of the elements of the original list
    that are perfect squares.
    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [int(sqrt(s[i])) for i in range(len(s)) if sqrt(s[i]).is_integer()]


def key_of_min_value(d):
    """Returns the key in a dict d that corresponds to the minimum value of d.
    >>> letters = {'a': 6, 'b': 5, 'c': 4, 'd': 5}
    >>> min(letters)
    'a'
    >>> key_of_min_value(letters)
    'c'
    """
    return min(d, key=lambda k: d[k])


def flatten(lst):
    """Returns a flattened version of lst.
    >>> flatten([1, 2, 3])  # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]  # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    new_list = []
    for item in lst:
        new_list += flatten(item) if type(item) is list else [item]
    return new_list


def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.
    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """
    if len(w1) == 0:
        return w2
    index = w2.find(w1[0])
    w2 = w2[0:index] + w2[index+1:]
    return add_chars(w1[1:], w2)


def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]


def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    return city[0]


def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]


def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]


def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    return sqrt((get_lat(city1) - get_lat(city2)) ** 2 + (get_lon(city1) - get_lon(city2)) ** 2)


def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    location = make_city("My location", lat, lon)
    distance1 = distance(location, city1)
    distance2 = distance(location, city2)
    if distance1 > distance2:
        return get_name(city2)
    else:
        return get_name(city1)

