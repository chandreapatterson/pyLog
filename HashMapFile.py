
# CITATION: Geeksforgeeks.org. August 20, 2023. Hash Map in Python.
# Retrieved June 13, 2024, from https://www.geeksforgeeks.org/hash-map-in-python/
# CITATION: Python.org (n.d.). Data Structures.
# Retrieved June 13, 2024, from https://docs.python.org/3.12/tutorial/datastructures.html#
# CITATION: W3schools.com. (n.d.). DSA Hash Maps.
# Retrieved June 13, 2024, from https://www.w3schools.com/dsa/dsa_data_hashmaps.php
class HashMapClass:  # Names hashmap class
    def __init__(self, load=15):  # Initiates class with 15-item load as attribute
        self.list = []  # Makes an empty list
        for i in range(load):  # Loops through capacity from 1 to 15
            self.list.append([])  # Adds 20 spots to list

    #  Defines function to insert delivery data
    def insert(self, a, b):  # Accepts arguments to insert delivery data as key-value pair
        placeholder = hash(a) % len(self.list)  # Determines index spot for key-value to go into hashmap
        rearrange = self.list[placeholder]  # Sets index spot for key-value to go into hashmap

        # Checks if key exists and updates
        for i in rearrange:  # Loops through rearrange
            if i[0] == a:  # Checks if key-value key is equal to current key
                i[1] = b  # Sets value of item if current key-value key matches
                return True  # Returns true boolean value

        pair = [a, b]  # Assigns variable to key-value
        rearrange.append(pair)  # Adds key-value pair to insert function list
        return True  # Returns true boolean value

    # Defines function to lookup delivery data in hashmap
    def lookup(self, a):  # Accepts a as argument
        placeholder = hash(a) % len(self.list)  # Determines index spot for key-value to check hashmap
        rearrange = self.list[placeholder]  # Sets index spot for key-value to check hashmap
        for i in rearrange:  # Loops through rearrange
            if a == i[0]:  # Checks if a matches existing key
                return i[1]  # Returns matched value from checked key
        return None  # Returns none if no match found

    # Defines function to remove key-value from hashmap
    def hash_remove(self, a):  # Accepts a as argument
        placeholder = hash(a) % len(self.list)   # Determines index spot for key-value to check hashmap
        will_remove = self.list[placeholder]  # Sets index spot to remove key-value from hashmap
        if a in will_remove:  # Checks if a from index spot exists
            will_remove.remove(a)  # Removes key-value

#                           BIBLIOGRAPHY
# CITATION: Geeksforgeeks.org. August 20, 2023. Hash Map in Python.
# Retrieved June 13, 2024, from https://www.geeksforgeeks.org/hash-map-in-python/
#
# CITATION: Python.org (n.d.). Data Structures.
# Retrieved June 13, 2024, from https://docs.python.org/3.12/tutorial/datastructures.html#
#
# CITATION: W3schools.com. (n.d.). DSA Hash Maps.
# Retrieved June 13, 2024, from https://www.w3schools.com/dsa/dsa_data_hashmaps.php
