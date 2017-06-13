import unittest
import sys
import os
from semigroups import (Semigroup, Transformation, Bipartition,
                        FullTransformationMonoid, CayleyGraph, bar, bar_transformation, membership, index_dict_function, image_transformation, stabiliser)

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

    def test_membership(self):
        self.assertTrue(membership(Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16]),[Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),
        Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16]), Transformation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8, 9, 10])]))
        self.assertFalse(membership(Transformation(list(range(17))), [Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),
        Transformation([2, 3, 4, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 15, 16, 15, 16]), Transformation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8, 9, 10])]))
        

    def test_image_transformation(self):
        self.assertEqual(image_transformation(Transformation([2,3,4,2,2]),3),2)

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

        barA = [bar_transformation(generator, barX) for generator in A]
        barf = bar_transformation(f, barX)
        barY = [barx for barx in barX if Y.intersection(set(barx)) != set([])]
        Z = [barf[barx] for barx in barY]
        barX_wo_redundencies = list(set(barX))
        [stabiliser(barx, A, barA, X) for barx in Z]
        self.assertEqual(stabiliser( (1,),A ,barA, X ), set([tuple(X)]))


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

    def test_bar_transformation(self):
        barX= bar([0, 1, 2, 3], [Transformation([1, 2, 2, 3])])
        self.assertEqual(bar_transformation(Transformation([1, 2, 2, 3]),barX),{(0,):(1,),(1,):(2,),(2,):(2,),(3,):(3,)})
        self.assertEqual(bar_transformation(Transformation([3, 0, 2, 1]),barX),{(0,):(3,),(1,):(0,),(2,):(2,),(3,):(1,)})
        
        barX = bar([0, 1, 2, 3, 4], [Transformation([1, 0, 3, 4, 3]), Transformation([3, 4, 2, 3, 4])])
        self.assertEqual(bar_transformation(Transformation([1,0,3,4,3]),barX),{(0,1):(0,1),(2,):(3,4),(3,4):(3,4)})

        barX = bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),
        Transformation([2, 3, 3, 3, 4, 7, 8, 9, 10, 9, 10, 13, 14, 16, 16, 15, 16]), Transformation([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 5, 6, 7, 8, 9, 10])])
        self.assertEqual(bar_transformation(Transformation([0, 2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12, 14, 14, 16, 16]),barX),
        {(0,):(0,), (1,):(2,), (2,):(2,), (3,):(4,), (4,):(4,), (5, 11):(6, 12), (6, 12):(6, 12), (7, 13):(8, 14), (8, 14):(8, 14), (9, 15):(10, 16), (10, 16):(10, 16)})

    def barA_indexed(self):
        pass


if __name__ == "__main__":
    unittest.main()
