"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


class Observation:
    def __init__(self, day, value):
        self.day = day
        self.value = value

    def __str__(self):
        return str(self.value)

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Patient(Person):
    """A patient in an inflammation study."""
    def __init__(self, name):
        super().__init__(name)
        self.observations = []

    def add_observation(self, value, day=None):
        if day is None:
            try:
                day = self.observations[-1].day + 1

            except IndexError:
                day = 0

        new_observation = Observation(day, value)

        self.observations.append(new_observation)
        return new_observation


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.
    data: input the whole 2D data array, 60 patients by 40 days
    return: an array with a daily mean (row)
    exceptions: none"""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.
    data: input the whole 2D data array, 60 patients by 40 days
    return: an array with a daily max (row)
    exceptions: non"""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.
    data: input the whole 2D data array, 60 patients by 40 days
    return: an array with a daily min (row)
    exceptions: non"""
    return np.min(data, axis=0)


def daily_add_std(data):
    """Calculate the daily min of a 2D inflammation data array.
    data: input the whole 2D data array, 60 patients by 40 days
    return: an array with a daily min (row)
    exceptions: non"""
    return np.std(data, axis=0)





#alice = Patient('Alice')
#print(alice)

#obs = alice.add_observation(3)
#print(obs)

#bob = Person('Bob')
#print(bob)

#obs = bob.add_observation(4)
#print(obs)


