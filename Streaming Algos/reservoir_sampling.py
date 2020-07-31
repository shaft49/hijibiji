import random

class ReservoirSampling:
    def __init__(self, max_size): # max_size is no of random samples that we want to save
        self.samples = []
        self.max_size = max_size
        self.n = 0
    
    def add(self, element):
        size = len(self.samples)
        if size >= self.max_size:
            spot = random.randint(0, self.n - 1)
            if spot < size:
                self.samples[spot] = element
        else:
            self.samples.append(element)
        self.n += 1;
    
    def get(self, index):
        size = len(self.samples)
        if index >= size:
            return "Invalid Index"
        else:
            return self.samples[index]

if __name__ == '__main__':
    rs = ReservoirSampling(2)
    rs.add(1)
    rs.add(2)
    print(rs.get(0))
    print(rs.get(1))
    rs.add(3)
    rs.add(4)
    print(rs.get(0))
    print(rs.get(1))
    #All the four elements should be selected
    