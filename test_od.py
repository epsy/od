# od -- Copyright (C) 2016-2022 Yann Kaiser. See LICENSE.txt

from collections import OrderedDict

from repeated_test import Fixtures

import od


class OdTests(Fixtures):
    def _test(self, make_value, expected):
        self.assertEqual(make_value(), expected)

    empty = lambda: od(), OrderedDict()
    iterable = lambda: od([
        ('element', 'value'),
    ]), OrderedDict([
        ('element', 'value'),
    ])

    one_element = lambda: od[
        'first': 'v1',
    ], OrderedDict([
        ('first', 'v1'),
    ])

    one_element_nocommadangle = lambda: od[
        'first': 'v1'
    ], OrderedDict([
        ('first', 'v1'),
    ])

    two_elements = lambda: od[
        'first': 'v1',
        'second': 'v2',
    ], OrderedDict([
        ('first', 'v1'),
        ('second', 'v2'),
    ])


class OdFailureTests(Fixtures):
    def _test(self, make_value, exc):
        with self.assertRaises(ValueError, msg=exc):
            make_value()

    number = lambda: od[4], None
    key = lambda: od['key'], None

    full_slice = lambda: od[1:2:3], None
    full_slice_amidst_correct = lambda: od[
        "thisis": "fine",
        "thisis": "not": "fine",
    ], None

    number_slices = lambda: od[1,2], None
