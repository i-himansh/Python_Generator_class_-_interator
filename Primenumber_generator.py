class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.number = 2

    def __next__(self):
        if self.number < self.stop:
            self.number += 1
            for x in range(2, self.number):
                if self.number % x == 0:
                    self.number += 1
            return self.number
        else:
            raise StopIteration()


g = PrimeGenerator(50)
while True:
    print(next(g))


