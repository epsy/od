
od
==

The ``od`` package adds a shorthand syntax to create `OrderedDict
<https://docs.python.org/3/library/collections.html#collections.OrderedDict>`_s::

    >>> import od
    >>>
    >>> od["cat": "fish", "mouse": "cheese"]
    OrderedDict([('cat', 'fish'), ('mouse', 'cheese')])
    >>> od["mouse": "cheese", "cat": "fish"]
    OrderedDict([('mouse', 'cheese'), ('cat', 'fish')])

You can also use it like the regular constructor for ``OrderedDict``::

    >>> od()
    OrderedDict()
    >>> an_iterable = [("cat", "fish"), ("mouse", "cheese")]
    >>> od(an_iterable)
    OrderedDict([('cat', 'fish'), ('mouse', 'cheese')])

Install this package using `pip <https://pip.pypa.io/en/stable/installing/>`_::

    $ pip install --user od
