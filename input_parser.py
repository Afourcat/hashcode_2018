
class Map(object):

    def __init__(self, rows, columns, vehicles):
        self.columns = columns
        self.rows = rows
        self.vehicles = vehicles

    def get_vehicles(self, x, y):
        """Get the vehicles at this intersection."""
        pass

    def get_rows(self):
        """Get the total city rows."""
        return self.rows

    def get_columns(self):
        """Get the total city columns."""
        return self.columns


class Ride(object):

    def __init__(self, start, end, time_start, time_end):
        self.step = 0
        self.remaining_time = time_end - time_start
        self.start = start
        self.end = end
        self.time_start = time_start
        self.time_end = time_end

    def get_start(self):
        """Get the start intersection for this ride."""
        return self.start

    def get_end(self):
        """Get the end intersection for this ride."""
        return self.end

    def get_time_start(self):
        """Get the start time for this ride."""
        return self.time_start

    def get_time_end(self):
        """Get the end time step for this ride."""
        return self.time_end

    def get_remaining_time(self):
        """Get the remaining time for this ride."""
        return self.remaining_time

    def _update(self):
        self.step = self.step + 1
        if self.step >= self.time_start:
            self.remaining_time = self.remaining_time - 1


class Vehicle(object):

    def __init__(self):
        self.position = [0, 0]
        self.next_position = [0, 0]

    def get_intersection(self):
        """Get the current vehicle intersection."""
        return self.position

    def move(self, x, y):
        """Move the vehicle to the corresponding case nex step."""
        if self.position[0] - x == -1  self.position[0] - x == 1:
            if self.position[0] - x == -1  self.position[0] - x == 1:
                self.next_position = [x, y]

    def _update(self):
        self.position = self.next_position


class Input(object):

    def __init__(self, file):
        self.file = file
        lines = self.file.split('\n')
        values = [int(i) for i in lines.split(' ')]
        self.map = Map(values[0], values[1])
        self.vehicles = []
        for i in range(values[2]):
            self.vehicles.append(Vehicle())
        self.rides = []
        for k, v in zip(lines, range(len(lines))):
            if v != 0 and v + 1 != len(lines):
                values = [int(i) for i in lines.split(' ')]
                self.rides.append(Ride(
                    [values[0], values[1]],
                    [values[3], values[3]],
                    values[5],
                    values[6]
                ))
        self.steps = values[5]

    def get_map(self):
        """Get the map object from the file."""
        return self.map

    def get_vehicles(self):
        """Get the list containing the Vehicles objects."""
        return self.vehicles

    def get_rides(self):
        """Get the list containing the rides objects."""
        return self.rides

    def get_steps(self):
        """Get the total number of steps."""
        return self.steps
