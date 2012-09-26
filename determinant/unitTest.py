import golfed
import unittest

class KnownValues(unittest.TestCase):
    knownDeterminants = [
        ([[1,-4,9],[-6,7,3],[1,2,3]],-240),
        ([[1,-4,9,4],[-6,7,3,7],[1,2,3,-4],[8,4,76,5]],-3040),
        ([[5]],5)
        ]

    knownMinors = [
        ([[1,-4,9],[-6,7,3],[1,2,3]],0,[(7,3),(2,3)]),
        ([[1,-4,9,4],[-6,7,3,7],[1,2,3,-4],[8,4,76,5]],0,[(7,3,7),(2,3,-4),(4,76,5)]),
        ]

    def testDet(self):
        """The det function should calculate the determinant"""
        for matrix, det in self.knownDeterminants:
            result = golfed.d(matrix)
            self.assertEqual(result,det)

    def testMinor(self):
        """The minor function should calculate the minor"""
        for matrix,row,minor in self.knownMinors:
            result = golfed.m(matrix,row)
            self.assertEqual(result,minor)

if __name__ == '__main__':
    unittest.main()
