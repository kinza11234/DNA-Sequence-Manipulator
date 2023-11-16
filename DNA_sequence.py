class Sequence:
    ''' creates the class Sequence and defines functions '''
    def __init__(self, sequence):
        self.sequence = sequence

    def get_sequence(self):
        return self.sequence

    def calculate_length(self):
        return len(self.sequence)

    def count_nucleotides(self):
        nucleotide_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for nucleotide in self.sequence:
            if nucleotide in nucleotide_count:
                nucleotide_count[nucleotide] += 1
        return nucleotide_count

class DNA(Sequence):
    ''' now creates a new class called DNA '''
    def reverse_complement(self):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        reverse_seq = self.sequence[::-1]
        reverse_complement_seq = ''
        for nucleotide in reverse_seq:
            if nucleotide == 'A':
                reverse_complement_seq = reverse_complement_seq + 'T'
            elif nucleotide == 'T':
                reverse_complement_seq = reverse_complement_seq + 'A'
            elif nucleotide == 'C':
                reverse_complement_seq = reverse_complement_seq + 'G'
            elif nucleotide == 'G':
                reverse_complement_seq = reverse_complement_seq + 'C'

        return reverse_complement_seq

    def find_pattern(self, pattern): #each returns wherever indices and pattern occur
        indices = []
        length = len(pattern)
        for i in range(len(self.sequence) - length + 1):
            if self.sequence[i:i + length] == pattern:
                indices.append(i)
        return indices

    def calculate_gc_content(self):
        gc_count = self.sequence('GC')
        return (gc_count / len(self.sequence)) * 100 if len(self.sequence) > 0 else 0

        if __name__ == '__main__': #creating the example
            dna_sequence = 'ATGCAAGG'
            dna = DNA(dna_sequence)

        seq_length = dna.calculate_length()
        count_nucleotid = dna.count_nucleotides()
        reverse_complement = dna.reverse_complement()
        pattern_indices = dna.find_pattern('GG')
        gc_content = dna.calculate_gc_content()

        print('Original sequence:', dna.get_sequence())
        print('sequence length: ', seq_length)
        print('sequence nucleotides: ', count_nucleotid)
        print('Reverse complement:', reverse_complement)
        print('Pattern indices:', pattern_indices)
        print('GC content:', gc_content)
