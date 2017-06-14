'''
This module contains classes for representing semigroups.
'''
# pylint: disable = no-member, protected-access, invalid-name, len-as-condition

import libsemigroups
from semigroups.elements import Transformation
from semigroups.cayley_graph import CayleyGraph
from libsemigroups import ElementABC, PythonElementNC
import networkx

class Semigroup(libsemigroups.SemigroupNC):
    r'''
    A *semigroup* is a set :math:`S`, together with a binary operation :math:`*
    :S\times S\to S`, such that :math:`S` is *associative* under :math:`*`,
    that is :math:`\forall a, b, c \in S \quad a * (b * c) = (a * b) * c`.

    Let :math:`S` is a semigroup and :math:`X\subseteq S`. The *semigroup
    generated by* :math:`X` is defined as the set of all product of elements
    of :math:`X`, together with the same operation. The elements of :math:`X`
    are called the *generators*.

    This class allows semigroups generated by sets to be represented in Python.

    Args:
        args (list):   The generators of the semigroup.

    Raises:
        ValueError: If no arguments are given.

    Examples:
        >>> from semigroups import *
        >>> S = Semigroup(Transformation([1, 2, 0]),
        ... Transformation([2, 1, 0]))
        >>> # the symmetric group
        >>> S.size()
        6
        >>> Transformation([0, 1, 2]) in S
        True
        >>> Transformation([0, 1, 0]) in S
        False
        >>> # To find the generators
        >>> S[0], S[1]
        (Transformation([1, 2, 0]), Transformation([2, 1, 0]))
    '''

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            self.__init__(*args[0])
            return
        elif len(args) == 0:
            raise ValueError('there must be at least 1 argument')
        elif not all(map(lambda elt: isinstance(elt, type(args[0])), args)):
            raise TypeError('generators must be of the same type')

        err_msg = 'generators must have a multiplication defined on them'
        x = args[0]
        if not isinstance(x, ElementABC):
            try:
                x * x
            except:
                raise TypeError(err_msg)

        gens = [g if isinstance(g, ElementABC) else PythonElementNC(g)
                for g in args]
        libsemigroups.SemigroupNC.__init__(self, gens)

    def right_cayley_graph(self):
        r"""
        Let :math:`S` be a semigroup, generated by a set :math:`X`. Let
        :math:`G` be a directed graph with node set :math:`S`, and for any
        :math:`x, y \in S`, there is an edge from :math:`x` to :math:`y` if
        :math:`y = xz` for some :math:`z \in X`. This graph is called a *right
        Cayley graph* of :math:`S`.

        This is a function for finding the right Cayley graph of a semigroup,
        using the generating set it was defined with.

        Raises:
            TypeError: If any arguments are given.

        Returns:
            semigroups.cayley_graph.CayleyGraph: The right Cayley graph.

        Examples:
            >>> from semigroups import Semigroup
            >>> S = Semigroup(complex(0, 1))
            >>> G = S.right_cayley_graph()
            >>> G.ordered_adjacencies()
            [[1], [2], [3], [0]]
            >>> G.edges()
            [(0, 1), (1, 2), (2, 3), (3, 0)]
            >>> G.nodes()
            [0, 1, 2, 3]
        """

        G = CayleyGraph()
        G._adjacencies_list = libsemigroups.SemigroupNC.right_cayley_graph(self)
        for i, adjacencies in enumerate(G._adjacencies_list):
            G._add_node(i)
        for i, adjacencies in enumerate(G._adjacencies_list):
            for j, adj in enumerate(adjacencies):
                G._add_edge_with_label(j, (i, adj))
        return G

    def left_cayley_graph(self):
        r"""
        Let :math:`S` be a semigroup, generated by a set :math:`X`. Let
        :math:`G` be a directed graph with node set :math:`S`, and for any
        :math:`x, y \in S`, there is an edge from :math:`x` to :math:`y` if
        :math:`y = zx` for some :math:`z \in X`. This graph is called a *left
        Cayley graph* of :math:`S`.

        This is a function for finding the left Cayley graph of a semigroup,
        using the generating set it was defined with.

        Raises:
            TypeError: If any arguments are given.

        Returns:
            semigroups.cayley_graph.CayleyGraph: The left Cayley graph.

        Examples:
            >>> from semigroups import Semigroup, Transformation
            >>> S = Semigroup(Transformation([0, 0, 0]),
            ... Transformation([1, 0, 1]))
            >>> G = S.left_cayley_graph()
            >>> G.edges()
            [(0, 0), (0, 0), (1, 2), (1, 3), (2, 2), (2, 2), (3, 0), (3, 1)]
            >>> G.ordered_adjacencies()
            [[0, 0], [2, 3], [2, 2], [0, 1]]
            >>> G.strongly_connected_components()
            [set([0]), set([2]), set([1, 3])]
        """
        G = CayleyGraph()
        G._adjacencies_list = libsemigroups.SemigroupNC.left_cayley_graph(self)
        for i, adjacencies in enumerate(G._adjacencies_list):
            G._add_node(i)
        for i, adjacencies in enumerate(G._adjacencies_list):
            for j, adj in enumerate(adjacencies):
                G._add_edge_with_label(j, (i, adj))
        return G

def membership(f, A):
    #Ensure f has same degree as elts of A
    n = A[0].degree()
    for a in A:
        if a.degree() != n:
            raise ValueError('Degree of elements of A must be the same')

    if f.degree() != n:
        return False

    #Step 0
    for generator in A:
        if f * generator != generator * f:
            return False

    #Step 1
    X = list(range(n))

    #The SCCs of X.
    barX = bar(X, A)

    #Y is the union of the source SCCs of X
    listY = [set([t]) for t in X]
    Y = set.union(*listY)

    barA = [bar_transformation(generator, barX) for generator in A]
    barf = bar_transformation(f, barX)

    #The SCCs that elements of y lie in. Here, barx is used to represent the
    # SCC that x is in.
    barY = [barx for barx in barX if Y.intersection(set(barx)) != set([])]

    #The image of Y under barf.
    Z = [barf[barx] for barx in barY]

    barX_wo_redundencies = list(set(barX))
    barX_wo_redundencies.sort()

    #An abelian group when restricted to the elements whose SCCs lie in Z.
    IZ_set = set.intersection(*[stabiliser(barx, A, barA, X) for barx in Z])
    IZ = [Transformation(list(img_tup)) for img_tup in IZ_set]
    hatA = [hat(g, barX, Z, X) for g in IZ]

    #Step 2
    barS = Semigroup(barA_indexed(barA, barX))
    barf_indexed = Transformation(index_dict_function(barf, barX_wo_redundencies, len(barX_wo_redundencies)))
    if not barf_indexed in barS:
        return False
    g_a_gens = barS.factorisation(barf_indexed)
    g_a = Transformation(X)
    for i in g_a_gens:
        g_a *= A[i]

    #Step 3
    g_a_img_list = list(g_a)
    f_img_list = list(f)
    hat_gc_dict = {}
    for i in Y:
        hat_gc_dict[g_a_img_list[i]] = f_img_list[i]
    for i in set(X) - set(hat_gc_dict.keys()):
        hat_gc_dict[i] = i
    hat_gc = Transformation(index_dict_function(hat_gc_dict, X, len(X)))

    #Step 4
    return hat_gc in Semigroup(hatA + [Transformation(X)])

def bar(X, A):
    G = networkx.MultiDiGraph()
    for x in X:
        G.add_node(x)
    for generator in A:
        for index, image in enumerate(generator):
            G.add_edge(index, image)
    return sorted([tuple(sorted(list(x))) for x in networkx.strongly_connected_components(G)])


    #given g in a semigroup S, with a set of SCCs barX, where x in X is in
    #SCC barx, we define barg to be the transformation of barX, such that
    #bar(xg) = (barx)barg

def bar_transformation(f, barX):

    #gives transformation as dictionary, with keys as input, values as image
    d = {}
    for barx in barX:
        image = image_transformation(f, barx[0])
        for barx2 in barX:
            if image in barx2:
                d[barx] = barx2
                break
    return d

def index_dict_function(g_dict, domain, n):
    return [domain.index(g_dict[domain[i]]) for i in range(n)]

def barA_indexed(barA, barX_wo_redundencies):
    n = len(barX_wo_redundencies)
    return [Transformation(index_dict_function(a, barX_wo_redundencies, n)) for a in barA]

def image_transformation(f, x):
    for i, image in enumerate(f):
        if i == x:
            return image

def stabiliser(barx, A, barA, X):
    return set([tuple(a) for a, bara in zip(A, barA) if bara[barx] == barx]).union(set([tuple(X)]))

def hat(f, barX, Z, X):
    #Gives transformation as image list
    d = {}
    for barx in barX:
        if barx in Z:
            for x in barx:
                d[x] = image_transformation(f, x)
        else:
            for x in barx:
                d[x] = x
    return Transformation([d[i] for i in X])

def test_semilattice_memb(f, A):
    B = [a for a in A if a * f == f]
    g = f.identity()
    for a in B:
        g *= a
    return f == g

def FullTransformationMonoid(n):
    r'''
    A semigroup :math:`S` is a *moniod* if it has an *identity* element. That
    is, an element :math:`e\in S` such that :math:`ea = ae = a \quad \forall a
    \in S`.

    Let :math:`n\in\mathbb{N}`. The set of all transformations of degree
    :math:`n` forms a monoid, called the *full transformation monoid*.

    This function returns the full transformation monoid of degree :math:`n`,
    for any given :math:`n\in\mathbb{N}`.

    Args:
        n (int):    The degree of the full transformation monoid.

    Returns:
        semigroups.semigrp.Semigroup: The full transformation monoid.

    Raises:
        TypeError:  If the degree is not an int.
        ValueError: If the degree is not positive.

    Examples:
        >>> from semigroups import FullTransformationMonoid
        >>> S = FullTransformationMonoid(3)
        >>> S.size()
        27
    '''
    if not isinstance(n, int):
        raise TypeError('degree of transformation must be an int')
    if n < 1:
        raise ValueError('degree of transformation must be positive')

    if n == 1:
        return Semigroup(Transformation([0]))
    elif n == 2:
        return Semigroup(Transformation([1, 0]), Transformation([0, 0]))

    return Semigroup([Transformation([1, 0] + list(range(2, n))),
                      Transformation([0, 0] + list(range(2, n))),
                      Transformation([n - 1] + list(range(n - 1)))])
