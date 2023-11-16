import unittest
from DNA_sequence import Sequence, DNA
''' starts test case for DNA_sequence.py '''
class TestSequence(unittest.TestCase):
    def setUp(self): #setting up initial DNA sequence
        self.sequence = Sequence('ATGCA')
        self.empty_sequence = Sequence('')

    def test_get_sequence(self):
        self.assertEqual(self.sequence.get_sequence(), 'ATGCA')
        self.assertEqual(self.empty_sequence.get_sequence(), '')

    def test_calculate_length(self):
        self.assertEqual(self.sequence.calculate_length(), 5)
        self.assertEqual(self.empty_sequence.calculate_length(), 0)

    def test_count_nucleotides(self):
        self.assertEqual(self.sequence.count_nucleotides(), {'A': 2, 'T': 1, 'C': 1, 'G': 1})
        self.assertEqual(self.empty_sequence.count_nucleotides(), {'A': 0, 'T': 0, 'C': 0, 'G': 0})

class TestDNA(unittest.TestCase):
    def setUp(self):
        self.dna = DNA('ATGCAAGG')
        self.empty_dna = DNA('')

    def test_reverse_complement(self):
        self.assertEqual(self.dna.reverse_complement(), 'CCTTGCAT')
        self.assertEqual(self.empty_dna.reverse_complement(), '')

    def test_find_pattern(self):
        self.assertEqual(self.dna.find_pattern('GG'), [6])
        self.assertEqual(self.dna.find_pattern('AA'), [1, 4])
        self.assertEqual(self.empty_dna.find_pattern('CG'), [])

    def test_calculate_gc_content(self):
        self.assertEqual(self.dna.calculate_gc_content(), 25.0)
        self.assertEqual(self.empty_dna.calculate_gc_content(), 0.0)

    unittest.main() #running the unit tests