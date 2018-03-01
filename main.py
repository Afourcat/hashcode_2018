#!/bin/python3
import sys
from input_parser import *


class Application(object):

    def __init__(self, file):
        data = Input(file)
        self.map = data.get_map()
        self.vehicles = data.get_vehicles()
        self.rides = data.get_rides()
        self.max_steps = data.get_steps()
        self.step = 0

    def main():
        while self.step < self.max_steps:
            update()

    def update(self):
        if self.step < self.max_steps:
            for i in self.vehicles:
                i._update()
            for r, i in zip(self.rides, range(len(self.rides))):
                if self.step == i.get_time_end():
                    self.rides.pop(i)
            self.step = self.step + 1

if __name__ == "__main__":
    app = Application(sys.argv[1])