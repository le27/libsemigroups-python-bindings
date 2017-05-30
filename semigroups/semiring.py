
'''
This module contains classes for semirings.
'''
# pylint: disable = no-member, protected-access, invalid-name,
# FIXME this is only partially complete

class Semiring:
    r"""
    A semiring is a set :math:`R`, together with two binary operations,
    :math:`+, \times`, such that :math:`(R, +)` is a commutative monoid,
    with identity called 0, :math:`(R\backslash\{0\},\times)` is a
    monoid, with identity 1, :math:`(R, +, \times)` is left and right
    distributive (ie :math:`\forall a, b, c \in R \quad a(b + c) = ab + ac` and
    :math:`\forall a, b, c \in R \quad (a + b)c = ac + bc`), and multiplication
    by zero must annihilate :math:`R`, that is :math:`\forall a \in R \quad
    a \cdot 0 = 0 \cdot a = 0`.

    Args:
        None

    Returns:
        None

    Raises:
        TypeError:  If any argument is given.
    """

    def __init__(self):
        self._minus_infinity = -float('inf')
        self._plus_infinity = float('inf')

class Integers(Semiring):
    """
    The usual ring of the Integers.

    Args:
        None

    Returns:
        None

    Raises:
        TypeError:  If any argument is given.
    """

    def __init___(self):
        pass

    def plus(self, x, y):
        """
        A function to find the sum of two integers, since this is the addition
        operation of the integers

        Args:
            x (int):    One of the integers to be added.
            y (int):    The other of the integers to be added.

        Returns:
            int:    x + y

        Raises:
            TypeError:  If x and y are not both ints.
        """
        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError
        return x + y

    def prod(self, x, y):
        """
        A function to find the sum of two integers, since this is the
        multiplication operation of the integers.

        Args:
            x (int):    One of the integers to be multiplied.
            y (int):    The other of the integers to be multplied.

        Returns:
            int:    x * y

        Raises:
            TypeError:  If x and y are not both ints.
        """

        if not (isinstance(x, int) and isinstance(y, int)):
            raise TypeError

        return x * y

    def zero(self):
        """
        A function to find the additive identity of the integers, which
        is 0.

        Args:
            None

        Returns:
            int:    0

        Raises:
            TypeError:  If any argument is given.
        """
        return 0

    def one(self):
        """
        A function to find the multiplicative identity of the integers, which
        is 1.

        Args:
            None

        Returns:
            int:    1

        Raises:
            TypeError:  If any argument is given.
        """

        return 1


class MaxPlusSemiring(Semiring):
    r"""
    The max plus semiring is a semiring comprising the set
    :math:`\mathbb{Z}\cup\{-\infty\}`, together with an operation which
    returns the maximum of two elements, as the additive operation and addition
    as the multiplicative operation.

    Minus infinity is a defined as smaller than all integers, and the integer
    sum of minus infinity and any element of the max plus semiring is minus
    infinity.

    Args:
        None

    Returns:
        None

    Raises:
        TypeError:  If any argument is given.
    """

    def __init___(self):
        pass

    def plus(self, x, y):
        """
        A function to find the maximum of two elements of the max plus
        semiring, since this is the addition operation of the max plus
        semiring.

        Args:
            x (int or float):    One of the elements to be added.
            y (int or float):    The other of the elements to be added.

        Returns:
            int float:    The maximum of x and y.

        Raises:
            TypeError:  If x and y are not both ints or minus infinity.
        """

        if not ((isinstance(x, int) or x == -float('inf'))
                and (isinstance(y, int) or y == -float('inf'))):
            raise TypeError

        return max(x, y)

    def prod(self, x, y):
        """
        A function to find the integer sum of two elements of the max plus
        semiring, since this is the addition operation of the max plus
        semiring.

        Args:
            x (int or float):    One of the elements to be multiplied.
            y (int or float):    The other of the elements to be multplied.

        Returns:
            int or float:    x + y

        Raises:
            TypeError:  If x and y are not both ints or minus infinity.
        """

        if not ((isinstance(x, int) or x == -float('inf'))
                and (isinstance(y, int) or y == -float('inf'))):
            raise TypeError

        return x + y

    def zero(self):
        """
        A function to find the additive identity of the max plus
        semiring, which is minus infinity.

        Args:
            None

        Returns:
            float:   -inf

        Raises:
            TypeError:  If any argument is given.
        """

        return self._minus_infinity

    def one(self):
        """
        A function to find the multiplicative identity of the max plus
        semiring, which is 0.

        Args:
            None

        Returns:
            int:    0

        Raises:
            TypeError:  If any argument is given.
        """

        return 0

class MinPlusSemiring(Semiring):
    r"""
    The min plus semiring is a semiring comprising the set
    :math:`\mathbb{Z}\cup\{\infty\}`, together with an operation which
    returns the maximum of two elements, as the additive operation and addition
    as the multiplicative operation.

    Plus infinity is a defined as greater than all integers, and the integer
    sum of plus infinity and any element of the max plus semiring is plus
    infinity.

    Args:
        None

    Returns:
        None

    Raises:
        TypeError:  If any argument is given.
    """

    def __init___(self):
        pass

    def plus(self, x, y):
        """
        A function to find the minimum of two elements of the min plus
        semiring, since this is the addition operation of the min plus
        semiring.

        Args:
            x (int or float):    One of the elements to be added.
            y (int or float):    The other of the elements to be added.

        Returns:
            int float:    The minimum of x and y.

        Raises:
            TypeError:  If x and y are not both ints or plus infinity.
        """

        if not ((isinstance(x, int) or x == float('inf'))
                and (isinstance(y, int) or y == float('inf'))):
            raise TypeError

        return min(x, y)

    def prod(self, x, y):
        """
        A function to find the integer sum of two elements of the min plus
        semiring, since this is the addition operation of the min plus
        semiring.

        Args:
            x (int or float):    One of the elements to be multiplied.
            y (int or float):    The other of the elements to be multplied.

        Returns:
            int or float:    x + y

        Raises:
            TypeError:  If x and y are not both ints or plus infinity.
        """

        if not ((isinstance(x, int) or x == float('inf'))
                and (isinstance(y, int) or y == float('inf'))):
            raise TypeError

        return x + y

    def zero(self):
        """
        A function to find the additive identity of the min plus
        semiring, which is plus infinity.

        Args:
            None

        Returns:
            float:   inf

        Raises:
            TypeError:  If any argument is given.
        """

        return self._plus_infinity

    def one(self):
        """
        A function to find the multiplicative identity of the min plus
        semiring, which is 0.

        Args:
            None

        Returns:
            int:    0

        Raises:
            TypeError:  If any argument is given.
        """

        return 0

class BooleanSemiring(Semiring):
    r"""
    The boolean semiring is a semiring comprising the set :math:`\{\text{True},
    \text{False} \}`, together with the operations 'or' and 'and'.

    Args:
        None

    Returns:
        None

    Raises:
        TypeError:  If any argument is given.
    """

    def __init__(self):
        pass

    def plus(self, x, y):
        """
        A function which returns True if either element is True (the boolean
        'or' function), since this is the additive operation.

        Args:
            x (bool):    One of the elements to be added.
            y (bool):    The other of the elements to be added.

        Returns:
            bool:    The result of x or y.

        Raises:
            TypeError:  If x and y are not both bools.
        """

        if not (isinstance(x, type(True)) and isinstance(y, type(True))):
            raise TypeError

        return x | y

    def prod(self, x, y):
        """
        A function which returns False if either element is False (the boolean
        'and' function), since this is the additive operation.

        Args:
            x (bool):    One of the elements to be multiplied.
            y (bool):    The other of the elements to be multiplied.

        Returns:
            bool:    The result of x and y.

        Raises:
            TypeError:  If x and y are not both bools.
        """

        if not (isinstance(x, type(True)) and isinstance(y, type(True))):
            raise TypeError

        return x & y

    def zero(self):
        """
        A function to find the additive identity of the boolean semiring, which
        is False.

        Args:
            None

        Returns:
            bool:   False

        Raises:
            TypeError:  If any argument is given.
        """
        return False

    def one(self):
        """
        A function to find the mutliplicative identity of the boolean semiring,
        which is True.

        Args:
            None

        Returns:
            bool:   True

        Raises:
            TypeError:  If any argument is given.
        """

        return True

class SemiringWithThreshold(Semiring):
    """
    A semiring with a threshold is a semiring is a semiring with a largest
    finite value, the threshold.

    This abstract class provides common methods for its subclasses.

    Returns:
        None

    Raises:
        TypeError:  If any argument is given.
    """

    def __init__(self):
        pass

    def threshold(self):
        """
        A function to find the threshold of a semiring.

        Returns:
            The threshold of the semiring.

        Raises:
            TypeError:  If any argument is given.
        """

        return self._threshold

class TropicalMaxPlusSemiring(SemiringWithThreshold):
    r"""
    The tropical max plus semiring is a semiring comprising the set :math:`\{0,
    \ldots, t\} \cup\{-\infty\}`, for some value :math:`t\in\mathbb{N}_0`, the
    threshold of the semiring, together with an operation which returns the
    maximum of two elements, as the additive operation and addition of integers
    as the multiplicative operation.

    Minus infinity is a defined as smaller than all integers, and the integer
    sum of minus infinity and any element of the max plus semiring is minus
    infinity.

    If the integer sum of any two elements is greater than the threshold, then
    the product is the threshold.

    Args:
        threshold (int):    The threshold of the semiring.

    Returns:
        None

    Raises:
        TypeError:  If threshold is not an int.
        ValueError: If threshold is negative.
    """

    def __init___(self, threshold):
        if not isinstance(threshold, int):
            raise TypeError

        if threshold < 0:
            raise ValueError

        self._threshold = threshold

    def plus(self, x, y):
        """
        A function to find the maximum of two elements of the tropical max plus
        semiring, since this is the addition operation of the tropical max plus
        semiring.

        Args:
            x (int or float):    One of the elements to be added.
            y (int or float):    The other of the elements to be added.

        Returns:
            int or float:   The maximum of x and y.

        Raises:
            TypeError:  If x and y are not both ints or minus infinity.
            ValueError: If either x or y is negative and not minus infinity, or
                        if x or y is greater than the threshold.
        """

        if not ((isinstance(x, int) or x == self._minus_infinity)
                and (isinstance(y, int) or y == self._minus_infinity)):
            raise TypeError

        if (x < 0 and x != self._minus_infinity) or (y < 0 and y != self._minus_infinity):
            raise ValueError

        if (x > self._threshold) or (y > self._threshold):
            raise ValueError

        return max(x, y)

    def prod(self, x, y):
        """
        A function to find the integer sum of two elements of the tropical max
        plus semiring, since this is the addition operation of the max plus
        semiring. If the integer sum is greater than :math:`t`, then the result
        is :math:`t`.

        Args:
            x (int or float):    One of the elements to be multiplied.
            y (int or float):    The other of the elements to be multplied.

        Returns:
            int or float:    x + y

        Raises:
            TypeError:  If x and y are not both ints or minus infinity.
            ValueError: If either x or y is negative and not minus infinity, or
                        if x or y is greater than the threshold.
        """

        if not ((isinstance(x, int) or x == self._minus_infinity)
                and (isinstance(y, int) or y == self._minus_infinity)):
            raise TypeError

        if (x < 0 and x != self._minus_infinity) or (y < 0 and y != self._minus_infinity):
            raise ValueError

        if (x > self._threshold) or (y > self._threshold):
            raise ValueError

        return min(self._threshold, x + y)

    def zero(self):
        """
        A function to find the additive identity of the tropical max plus
        semiring, which is minus infinity.

        Args:
            None

        Returns:
            float:   -inf

        Raises:
            TypeError:  If any argument is given.
        """

        return self._minus_infinity

    def one(self):
        """
        A function to find the multiplicative identity of the tropical max plus
        semiring, which is 0.

        Args:
            None

        Returns:
            int:    0

        Raises:
            TypeError:  If any argument is given.
        """

        return 0
