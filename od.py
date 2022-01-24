# od -- Copyright (C) 2016-2022 Yann Kaiser. See LICENSE.txt

import sys
from collections import OrderedDict


_USE_PAIRS = "od[...] must be used with pairs of `key: value,` items"


class OrderedDictBuilder(object):
    def __init__(self, cls):
        self.cls = cls

    def __getitem__(self, slices):
        if isinstance(slices, slice):
            slices = slices,
        elif not isinstance(slices, tuple):
            raise ValueError(_USE_PAIRS)
        return self.cls(
            (sl.start, sl.stop)
            if isinstance(sl, slice) and sl.step is None
                else self.__throw(_USE_PAIRS)
            for sl in slices
        )

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)

    def __throw(self, msg):
        raise ValueError(msg)


sys.modules['od'] = od = OrderedDictBuilder(OrderedDict)
od.OrderedDictBuilder = OrderedDictBuilder
