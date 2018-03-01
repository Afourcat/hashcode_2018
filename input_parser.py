#!/bin/python3
"""Hashcode algorithme""""

class Map(object):

    def __init__(self):
        pass

    def get_vehicles(self, x, y):
        """Get the vehicles at this intersection."""
        pass

    def get_rows(self):
        """Get the total city rows."""
        pass

    def get_columns(self):
        """Get the total city columns."""
        pass

class Ride(object):

    def __init__(self):
        pass

    def get_start(self):
        """Get the start intersection for this ride."""
        pass

    def get_end(self):
        """Get the end intersection for this ride."""
        pass

    def get_time_start(self):
        """Get the start time for this ride."""
        pass

    def get_time_end(self):
        """Get the end time step for this ride."""
        pass

    def get_remaining_time(self):
        """Get the remaining time for this ride."""
        pass

class Vehicle(object):

    def __init__(self):
        pass

    def get_intersection(self):
        """Get the current vehicle intersection."""
        pass

class Input(object):

    def __init__(self, file):
        pass

    def get_map(self):
        """Get the map object from the file."""
        pass

    def get_vehicles(self):
        """Get the list containing the Vehicles objects."""
        pass

    def get_rides(self):
        """Get the list containing the rides objects."""
        pass

    def get_steps(self):
        """Get the total number of steps."""
        pass
