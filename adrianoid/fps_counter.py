import queue


class FPSCounter:
    def __init__(self):
        self.length = 100
        self.measurements = [0] * self.length
        self.counter = 0

    def add_measurement(self, result):
        self.measurements[self.counter] = result
        self.counter = (self.counter + 1) % self.length

    def get_fps(self):
        return int (sum(self.measurements)//self.length)
