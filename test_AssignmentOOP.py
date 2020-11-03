import unittest
from AssignmentOOP import CodePegs
from AssignmentOOP import Board


class TestClasses (unittest.TestCase):
    def test_list(self):
        self.assertListEqual(CodePegs().codePegs, ["R", "G", "L", "Y", "B", "W"])
    
    def test_feedback(self):
        pass

unittest.main()