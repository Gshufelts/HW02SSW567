# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInputValidation1(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput', 'Values over 200 are invalid inputs')

    def testInputValidation2(self):
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','Values below zero are invalid inputs')

    def testInputValidation3(self):
        self.assertEqual(classifyTriangle("x", "y", "z"), 'InvalidInput', 'Non-integers are invalid inputs')

    def testIsATriangleExact(self):
        self.assertEqual(classifyTriangle(50,50,100), 'NotATriangle', 'Two of the side lengths total to the exact length of the final side, meaning this is not a triangle')

    def testIsATriangleLess(self):
        self.assertEqual(classifyTriangle(49,50,100), 'NotATriangle', 'Two of the side lengths total to a length less than that of the final side, meaning this is not a triangle')

    def testIsEquilateral1(self):
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral', 'All three sides of the triangle are equal meaning it is equilateral')

    def testIsEquilateral2(self):
        self.assertEqual(classifyTriangle(9,9,9),'Equilateral', 'All three sides of the triangle are equal meaning it is equilateral')

    def testIsRight1(self):
        self.assertEqual(classifyTriangle(3,4,5),'Righ', 'A 3,4,5 triangle is a right triangle')

    def testIsRight2(self):
        self.assertEqual(classifyTriangle(5,12,13),'Righ', 'A 5,12,13 triangle is a right triangle')

    def testIsScalene1(self):
        self.assertEqual(classifyTriangle(3,5,6),'Scalene', 'A triangle with no equal sides is scalene')

    def testIsScalene2(self):
        self.assertEqual(classifyTriangle(5,9,12),'Scalene', 'A triangle with no equal sides is scalene')

    def testIsIsosceles1(self):
        self.assertEqual(classifyTriangle(5,5,8),'Isosceles', 'A triangle with two equal sides is isosceles')

    def testIsIsosceles2(self):
        self.assertEqual(classifyTriangle(9,9,14),'Isosceles', 'A triangle with two equal sides is isosceles')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

