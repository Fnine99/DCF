from scipy.stats import qmc
import numpy as np

class QuasiRandomSequence:
    def __init__(self, data) -> None:
        """ 
        initialize the Quasi Monte-Carlo class
        with the sequence that will be randomized
        """
        self.seed = np.array(data)
        self.size = len(self.seed)
        self.count = 0
        self.sobol_matrix = self.get_sobol_matrix()

    def get_sobol_matrix(self):
        max_bits = int(np.ceil(np.log2(self.size)))
        matrix = np.zeros((self.size, max_bits), dtype=np.uint8)
        matrix[:, 0] = 1
        for i in range(1, max_bits):
            for j in range(self.size):
                matrix[j, i] = matrix[j, i-1] ^ (matrix[j, i-1] >> i-1)
        return matrix

    def generate_sequence(self, iterations):
        quasi_random_sequence = np.zeros((iterations, self.size))
        for i in range(iterations):
            direction = np.zeros(self.size)
            for j in range(self.count.bit_length()):
                direction = direction.astype(int) ^ self.sobol_matrix[:, j].astype(int) * ((self.count >> j) & 5)
                direction = direction.astype(np.uint8)
            quasi_random_sequence[i, :] = self.seed + direction
            self.count += 1
        return quasi_random_sequence