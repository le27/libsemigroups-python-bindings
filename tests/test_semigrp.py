import unittest
import sys
import os
from semigroups import (Semigroup, Transformation, Bipartition,
                        FullTransformationMonoid, CayleyGraph, bar,
                        bar_dict, index_dict_function,
                        hit, stabiliser, TransDirectProduct, TCom)

path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if path not in sys.path:
    sys.path.insert(1, path)
del path


class TestSemigroup(unittest.TestCase):
    def test_init(self):
        Semigroup(-1)
        Semigroup(Transformation([1, 0, 1]), Transformation([0, 0, 0]))

        with self.assertRaises(ValueError):
            Semigroup()

        with self.assertRaises(TypeError):
            Semigroup(Bipartition([1, -1], [2], [-2]), Transformation([0, 1]))

        with self.assertRaises(TypeError):
            Semigroup({2, 3})

    def test_right_cayley_graph(self):
        Semigroup(-1).right_cayley_graph()
        self.assertTrue(isinstance(Semigroup(-1).right_cayley_graph(),
                                   CayleyGraph))

    def test_left_cayley_graph(self):
        Semigroup(Transformation([0, 1])).right_cayley_graph()
        self.assertTrue(isinstance(Semigroup(-1).left_cayley_graph(),
                                   CayleyGraph))

class TestOtherFunctions(unittest.TestCase):
    def test_FullTransformationMonoid(self):
        self.assertEqual(FullTransformationMonoid(3)[7],
                         Semigroup(Transformation([1, 0, 2]),
                                   Transformation([0, 0, 2]),
                                   Transformation([2, 0, 1]))[7])
        self.assertEqual(FullTransformationMonoid(2)[5],
                         Semigroup(Transformation([0, 0]),
                                   Transformation([0, 1]))[5])
        self.assertEqual(FullTransformationMonoid(1)[0],
                         Semigroup(Transformation([0]))[0])

        with self.assertRaises(TypeError):
            FullTransformationMonoid(2.5)

        with self.assertRaises(ValueError):
            FullTransformationMonoid(-7)

    def test_commutative_semilattice(self):
        S = Semigroup(Transformation([0,0,2,2]))
        S1 = TransDirectProduct(*[S]*5)
        self.assertTrue(S1.commutative_semilattice_memb(S1[3] * S1[4]**3 * S1[2]))
        self.assertFalse(S1.commutative_semilattice_memb(Transformation([1]*S1[0].degree())))
        self.assertFalse(S1.commutative_semilattice_memb(Transformation([0]*S1[0].degree())))
        self.assertFalse(S1.commutative_semilattice_memb(Transformation([2]*S1[0].degree())))
        self.assertFalse(S1.commutative_semilattice_memb(Transformation([2]*S1[0].degree())))
        self.assertFalse(S1.commutative_semilattice_memb(Transformation([0])))
        S1.enumerate()
        self.assertTrue(S1.commutative_semilattice_memb(S1[3] * S1[4]**3 * S1[2]))

    def test_commutative_membership(self):
        bigfreesemi = Semigroup(Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),
                                Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16]), 
                                Transformation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8, 9, 10]))
        self.assertTrue(bigfreesemi.commutative_membership(
                        Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16])))
        self.assertFalse(bigfreesemi.commutative_membership(
                        Transformation([0])))
        
        S1 = Semigroup(Transformation([8, 11, 6, 12, 17, 17, 2, 4, 11, 8, 6, 17, 16, 6, 10, 9, 9, 11, 2, 5]))
        S = TransDirectProduct(*[S1] * 10)
        t1 = S[5] * S[5] * S[2] * S[8] * S[9] * S[9]
        t2 = S[7] * S[3] * S[2] * S[8] * S[0] * S[4]
        t3 = S[1] * S[4] * S[2] * S[8] * S[5] * S[7]
        self.assertTrue(S.commutative_membership(t1))
        self.assertTrue(S.commutative_membership(t2))
        self.assertTrue(S.commutative_membership(t3))
        self.assertFalse(S.commutative_membership(Transformation([0] * S[0].degree())))
        self.assertFalse(S.commutative_membership(Transformation([0])))
        S1.enumerate()
        self.assertFalse(S1.commutative_membership(t3))
        S2 = Semigroup(Transformation(list(range(S1[0].degree()))))
        S = TransDirectProduct(*[S2,S1] * 5)
        l = list(range(S[0].degree()))
        l[3] = 8
        self.assertFalse(S.commutative_membership(Transformation(l)))

    def test_TCom(self):
        a = Transformation([0, 1])
        b = Transformation([1, 0])
        c = Transformation([0, 0, 0])
        d = Transformation([1, 2, 2])
        self.assertTrue(TCom(b, b))
        self.assertTrue(TCom(a, a))
        self.assertTrue(TCom(a, b))
        self.assertFalse(TCom(a, c))
        self.assertFalse(TCom(d, c))

    def test_hit(self):
        self.assertEqual(hit(Transformation([2,3,4,2,2]),3),2)

    def test_stabiliser(self):
        f = Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16])
        A = [Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),
        Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16]), Transformation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8, 9, 10])]
        for generator in A:
            if f * generator != generator * f:
                return False
        X = list(range(A[0].degree()))
        barX = bar(X, A)
        listY = [set([t]) for t in X]
        Y = set.union(*listY)

        barA = [bar_dict(generator, barX) for generator in A]
        barf = bar_dict(f, barX)
        barY = [barx for barx in barX if Y.intersection(set(barx)) != set([])]
        Z = [barf[barx] for barx in barY]
        barX_wo_redundencies = list(set(barX))
        [stabiliser(barx, A, barA, X) for barx in Z]
        self.assertEqual(stabiliser((1,) ,A ,barA, X ), set([tuple(X)]))


    def test_bar(self):
        x = set([tuple(sorted(x)) for x in (bar([0, 1, 2, 3], [Transformation([1, 2, 2, 3])]))])
        y = {(1,), (2,), (3,), (0,)}
        self.assertEqual(x, y)
        x = set([tuple(sorted(x)) for x in bar([0, 1, 2, 3], [Transformation([1, 2, 3, 2])])])
        y = {(1,), (2,3), (0,)}
        self.assertEqual(x, y)
        x = set([tuple(sorted(x)) for x in bar([0, 1, 2, 3, 4], [Transformation([1, 0, 3, 4, 3]), Transformation([3, 4, 2, 3, 4])])])
        y = {(0,1), (2,), (3,4)}
        self.assertEqual(x, y)
        x = set([tuple(sorted(x)) for x in bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),
        Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16]), Transformation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8, 9, 10])])])
        y = {(0,), (1,), (2,), (3,), (4,), (5, 11), (6, 12), (7, 13), (8, 14), (9, 15), (10, 16)}
        self.assertEqual(x, y)

    def test_index_dict_function(self):
        d = {1:2,4:1,2:3,3:4}
        self.assertEqual(index_dict_function(d,[1,2,3,4],4),[1,2,3,0])
        d = {1:2,4:1,2:3,3:4,5:1}
        self.assertEqual(index_dict_function(d,[1,2,5,4,3],5),[1,4,0,0,3])

    def test_bar_dict(self):
        barX= bar([0, 1, 2, 3], [Transformation([1, 2, 2, 3])])
        self.assertEqual(bar_dict(Transformation([1, 2, 2, 3]),barX),{(0,):(1,),(1,):(2,),(2,):(2,),(3,):(3,)})
        self.assertEqual(bar_dict(Transformation([3, 0, 2, 1]),barX),{(0,):(3,),(1,):(0,),(2,):(2,),(3,):(1,)})
        
        barX = bar([0, 1, 2, 3, 4], [Transformation([1, 0, 3, 4, 3]), Transformation([3, 4, 2, 3, 4])])
        self.assertEqual(bar_dict(Transformation([1,0,3,4,3]),barX),{(0,1):(0,1),(2,):(3,4),(3,4):(3,4)})

        barX = bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),
        Transformation([2, 3, 3, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 16, 16, 15, 16]), Transformation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8, 9, 10])])
        self.assertEqual(bar_dict(Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),barX),
        {(0,):(0,), (1,):(2,), (2,):(2,), (3,):(4,), (4,):(4,), (5, 11):(6, 12), (6, 12):(6, 12), (7, 13):(8, 14), (8, 14):(8, 14), (9, 15):(10, 16), (10, 16):(10, 16)})

    def barA_indexed(self):
        pass


if __name__ == "__main__":
    unittest.main()
