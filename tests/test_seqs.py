from collections import Iterator
from whatever import _

from funcy.seqs import *


def test_repeatedly():
    c = count().next
    assert take(2, repeatedly(c)) == [0, 1]

def test_iterate():
    assert take(4, iterate(_ * 2, 1)) == [1, 2, 4, 8]


def test_take():
    assert take(2, [3, 2, 1]) == [3, 2]
    assert take(2, count(7)) == [7, 8]

def test_drop():
    dropped = drop(2, [5, 4, 3, 2])
    assert isinstance(dropped, Iterator)
    assert list(dropped) == [3, 2]

    assert take(2, drop(2, count())) == [2, 3]

def test_first():
    assert first('xyz') == 'x'
    assert first(count(7)) == 7
    assert first([]) is None


def test_remove():
    assert remove(_ > 3, range(10)) == [0, 1, 2, 3]

def test_keep():
    assert keep(_ % 3, range(5)) == [1, 2, 1]

def test_concat():
    assert concat('ab', 'cd') == list('abcd')
    assert concat() == []

def test_cat():
    assert cat('abcd') == list('abcd')
    assert cat(range(x) for x in range(3)) == [0, 0, 1]

def test_mapcat():
    assert mapcat(lambda x: [x, x], 'abc') == list('aabbcc')

def test_interleave():
    assert list(interleave('ab', 'cd')) == list('acbd')
    assert list(interleave('ab_', 'cd')) == list('acbd')

def test_iterpose():
    assert list(interpose('.', 'abc')) == list('a.b.c')


def test_distinct():
    assert distinct('abcbad') == list('abcd')

def test_split():
    assert split(2, range(5)) == [[0, 1], [2, 3, 4]]
    assert split(_ % 2, range(5)) == [[1, 3], [0, 2, 4]]

def test_groupby():
    assert groupby(_ % 2, range(5)) == {0: [0, 2, 4], 1: [1, 3]}

def test_partition():
    assert partition(2, range(5)) == [[0, 1], [2, 3]]
    assert partition(2, 1, range(4)) == [[0, 1], [1, 2], [2, 3]]

def test_chunks():
    assert chunks(2, range(5)) == [[0, 1], [2, 3], [4]]
    assert chunks(2, 1, range(4)) == [[0, 1], [1, 2], [2, 3], [3]]