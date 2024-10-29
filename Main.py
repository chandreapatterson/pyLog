# Python | Logistics Project | Chandrea Patterson

# Imports modules from python library to allow program to use
import csv  # Allows python to handle comma separated value files
import datetime  # Allows python to convert characters to specific time and date format

# Imports ValueError module to handle exceptions for incorrect data types
from builtins import ValueError  # Builtins library contains ValueError module for value type match exception handling

#  Allows program to  data from other created files
from HashMapFile import HashMapClass  # Allows python to refer to specified class from hashmap file

# CITATION: Python.org. (n.d.) CSV File Reading and Writing.
# Retrieved June 13, 2024, from https://docs.python.org/3/library/csv.html
# Opens and reads data from Address csv
with open("CSVFiles/CSVAddress.csv") as address_data:  # Tells which file to open and assigns it to variable with 'as'
    Address_Data = csv.reader(address_data)  # Use assigned file variable with reader csv function, stores in variable
    Address_Data = list(Address_Data)  # Reassigns read csv variable to store as list

# Opens and reads data from adjacency matrix csv
with open("CSVFiles/CSVMatrix.csv") as distance_data:  # Tells which file to open and assigns it to variable with 'as'
    Distance_Data = csv.reader(distance_data)  # Use assigned file variable with reader csv function, stores in variable
    Distance_Data = list(Distance_Data)  # Reassigns read csv variable to store as list

# Opens and reads data from csv
with open("CSVFiles/CSVPackage.csv") as package_data:  # Tells which file to open and assigns it to variable with 'as'
    Package_Data = csv.reader(package_data)  # Use assigned file variable with reader csv function, stores in variable
    Package_Data = list(Package_Data)  # Reassigns read csv variable to store as list



# CITATION: Python.org. (n.d.) Classes.
# Retrieved June 13, 2024, from https://docs.python.org/3/tutorial/classes.html
# Class for package data retrieved from CSVPackage file
class FreightDock:  # Names FreightDock , col1, col2, col3, etc. corresponds to columns in CSVPackage file
    def __init__(self,
                 col1,
                 col2,
                 col3,
                 col4,
                 col5,
                 col6,
                 col7,
                 col8,
                 col9):  # Sets attributes
        self.id = col1  # To coincide with column 1 in csv
        self.address = col2  # To coincide with column 2 in csv
        self.city = col3  # To coincide with column 3 in csv
        self.state = col4  # To coincide with column 4 in csv
        self.zipcode = col5  # To coincide with column 5 in csv
        self.goal = col6  # To coincide with column 6 in csv
        self.weight = col7  # To coincide with column 7 in csv
        self.status = col8  # To be set by update_status function
        self.time_route_start = None  # Sets starting route time to none
        self.time_route_stop = None  # Sets ending route time to none
        self.trucknum = col9

    # CITATION: Python.org. (n.d.) 3.2.4. number.Number.
    # Retrieved June 13, 2024, from https://docs.python.org/3/reference/datamodel.html
    def __str__(self):  # String type function
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id,
                                                       self.address,
                                                       self.city,
                                                       self.state,
                                                       self.zipcode,
                                                       self.goal,
                                                       self.weight,
                                                       self.time_route_stop,
                                                       self.status,
                                                       self.trucknum)  # Returns attributes as strings

    # Defines function to update data to show current status of deliveries
    def get_trip_stats(self, format_time):  # Accepts time as argument
        if self.time_route_stop < format_time:  # Checks if time_route_stop is prior to input time
            self.status = "delivered"  # Sets status to string value
        elif self.time_route_start > format_time:  # Checks if time_route_start is after input time
            self.status = "en route"  # Sets status to string value
        else:  # Determines that status is not Delivered or En route
            self.status = "at the hub"  # Sets status to string value


# Assigns variable to call function to make hashmap (from hashmap file)
getpackage = HashMapClass()


# Defines function to bring data from package csv file to package object in program (column to index)
def prep_delivery(getfile, getpackage):  # Parameters for retrieving package data (file, hashmap)
    with open(getfile) as package_info:  # Tells which file to open and assigns it to variable with 'as'
        package_data = csv.reader(package_info)  # Uses reader csv function, stores in variable
        for i in package_data:  # Loops through each column (index) in csv file
            id_pkg = int(i[0])  # Assigns variable to column 1 (index 0) and becomes integer type
            address_pkg = i[1]  # Assigns variable to column 2 (index 1)
            city_pkg = i[2]  # Assigns variable to column 3 (index 2)
            state_pkg = i[3]  # Assigns variable to column 4 (index 3)
            zipcode_pkg = i[4]  # Assigns variable to column 5 (index 4)
            deadline_pkg = i[5]  # Assigns variable to column 6 (index 5)
            weight_pkg = i[6]  # Assigns variable to column 7 (index 6)
            status_pkg = "at the hub"  # Sets column 8 (index 7) status
            truck_pkg = i[8]  # Assigns variable to column 9

            # Assigns variable to package object initiated in FreightDock class
            pkg_set = FreightDock(id_pkg,
                                 address_pkg,
                                 city_pkg,
                                 state_pkg,
                                 zipcode_pkg,
                                 deadline_pkg,
                                 weight_pkg,
                                 status_pkg,
                                 truck_pkg)

            # Calls function to insert hashmap with data (initiated in hashmap file)
            getpackage.insert(id_pkg, pkg_set)


# Defines function to bring data from Distance csv (adjacency matrix), save in variable and return as float type
def measure_distance(point_a, point_b):  # Sets parameters to measure distance between locations point_a, point_b
    distance = Distance_Data[point_a][point_b]  # Assigns distance variable for conditional comparison in delivery
    if distance == '':  # Checks if distance in one direction results in empty comparison condition
        distance = Distance_Data[point_b][point_a]  # Changes direction to avoid empty distance

    return float(distance)  # Returns distance value as float type


# Defines function to return data from Address csv (column 1 to integer)
def prep_dropoff(location):  # Sets address from Address csv file as argument for prep_dropoff function
    for i in Address_Data:  # Loops through rows in Address csv file
        if location in i[2]:  # Checks if argument value exists in row 3 (index 2)
            return int(i[0])  # Returns value from column 1 of matched address


class Truck:  # Names Truck class
    def __init__(self,
                 truckload,
                 trip,
                 address,
                 begin):  # Sets attributes for Truck class
        self.truckload = truckload  # Will hold list of starting packages (unordered and ordered)
        self.trip = trip  # Will track miles between deliveries
        self.address = address  # Will track delivery addresses
        self.begin = begin  # Will track beginning time for third Truck
        self.time = begin  # Will track beginning time

    def __str__(self):  # String type function
        return "%s, %s, %s, %s" % (self.truckload,
                                   self.trip,
                                   self.address,
                                   self.begin)  # Returns strings


# Assigns variable for each Truck object
# Attributes include:
#          - package selection to deliver
#          - trip total miles to start at zero
#          - address to start
#          - time to start
# Same truck 14 & 15
# Same truck 13, 16, & 20

# First Truck object
first_truck = Truck([1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40],
                    0.0,
                    "4001 South 700 East",
                    datetime.timedelta(hours=8))

# Second Truck object - Must have 3, 18, 36, & 38
second_truck = Truck([2, 3, 4, 5, 7, 8, 9, 10, 18, 21, 22, 23, 24, 33, 36, 38],
                     0.0,
                     "4001 South 700 East",
                     datetime.timedelta(hours=10, minutes=20))

# Third Truck object - Must have 6, 25, 28, & 32
third_truck = Truck([6, 11, 12, 17, 25, 26, 27, 28, 32, 35, 39],
                    0.0,
                    "4001 South 700 East",
                    datetime.timedelta(hours=9, minutes=5))

# Adds variable to output corrected address for package 9 after 10:20:00
correct_nine = "9, 410 S State St, Salt Lake City, UT, 84111, EOD, 2 Kilos, 11:02:00, delivered, Truck 2"


# Calls function to bring data from Package csv into hashmap
prep_delivery("CSVFiles/CSVPackage.csv", getpackage)


# Defines function for trucks to deliver packages
def route_for_trucks(go):
    awaiting_route = []  # Empty array to hold undelivered packages
    for i in go.truckload:  # Loops through packages array from assigned truck objects
        package = getpackage.lookup(i)  # Gives package variable value from hashmap lookup function
        awaiting_route.append(package)  # Adds package to array
    go.truckload.clear()  # Uses clear function to remove packages from trucks to be reordered

    # While loop based on number of packages that remain undelivered
    while len(awaiting_route) > 0:  # Will continue to loop until length of undelivered array is 0
        add_stop = 2000  # Sets starting distance for next delivery address for conditional comparison
        cargo = None  # Sets starting point for package list
        for i in awaiting_route:  # Loops through undelivered array
            # Sets location and package for next delivery
            if measure_distance(prep_dropoff(go.address), prep_dropoff(i.address)) <= add_stop:
                add_stop = measure_distance(prep_dropoff(go.address), prep_dropoff(i.address))
                cargo = i
        go.truckload.append(cargo.id)  # Takes package from undelivered and adds to truck packages
        awaiting_route.remove(cargo)  # Takes package off of undelivered
        go.trip += add_stop  # Takes distance calculated from conditional comparison and adds to trip
        go.address = cargo.address  # Makes trucks current address the address most recently delivered to
        go.time += datetime.timedelta(hours=add_stop / 18)  # Calculates time driven using 18 avg mph
        cargo.time_route_stop = go.time  # Updates base for package arrival time to recent calculated time
        cargo.time_route_start = go.begin  # Updates base for departure time to most recent departure


route_for_trucks(first_truck)  # Runs first_truck through route_for_trucks function
route_for_trucks(second_truck)  # Runs second_truck through route_for_trucks function
third_truck.begin = min(first_truck.time, second_truck.time)  # Minimum departure after other trucks
route_for_trucks(third_truck)  # Run third_truck through route_for_trucks function



# Outputs messages for user input prompts to interact with program
class Main:
    # Shows total distance
    print(first_truck.trip + second_truck.trip + third_truck.trip, "total miles traveled by all trucks.")
    entered = input("Hit 'Enter' key to run program. Type 'quit' to stop program...")  # User input prompt
    if entered != "quit":  # Checks user input
        try:  # Try-except to catch unacceptable input
            entered_time = input("Enter ##:##:## to check delivery time & status...(Example: 09:05:00)")
            (HH, MM, SS) = entered_time.split(":")  # sets colon as delimiter for input from user

            # Uses datetime module to convert user input and assign to format_time variable
            format_time = datetime.timedelta(hours=int(HH),
                                             minutes=int(MM),
                                             seconds=int(SS))
            select_load = input("Enter '1' to check a single delivery or '40' to check every delivery...")  # Prompt
            if select_load == "1":  # Checks user input
                try:  # try-except to handle unacceptable user input
                    select_one = input("Enter a delivery # 1 - 40...(Example: 3)")  # Assigns variable to user input
                    pkg_stats = getpackage.lookup(int(select_one))  # Uses hashmap lookup to match to package
                    pkg_stats.get_trip_stats(format_time)  # Uses get_trip_stats function to show package status
                    if ((int(HH)) == 10
                            and (int(MM)) > 20
                            and (int(select_one)) == 9
                            or (int(HH)) >= 11 and
                            (int(select_one)) == 9):
                        pkg_stats = correct_nine
                    print(str(pkg_stats))  # Outputs status to console
                except ValueError:  # Uses python library to catch cases where stored type does not match user input
                    print("Run program again - invalid input.")  # Shows message
                    exit()  # Tells program to exit
            elif select_load == "40":  # Second option for user input to show delivery status
                try:  # try-except for showing all delivery statuses
                    for i in range(1, 41):  # Loops through all deliveries from first to last
                        pkg_stats = getpackage.lookup(i)  # Assigns package variable to hashmap lookup
                        pkg_stats.get_trip_stats(format_time)  # Show package status
                        if ((int(HH)) == 10
                                and (int(MM)) > 20
                                and (int(i)) == 9
                                or (int(HH)) >= 11 and
                                (int(i)) == 9):
                            pkg_stats = correct_nine
                        print(str(pkg_stats))  # Outputs status to console
                except ValueError:  # Uses python library to catch cases where stored type does not match user input
                    print("Run program again - invalid input.")  # Shows message
                    exit()  # Tells program to exit
            else:
                print("Run program again - invalid input.")  # Shows message
                exit()  # Tells program to exit
        except ValueError:  # Uses python library to catch cases where stored type does not match user input
            print("Run program again - invalid input.")  # Shows message
            exit()  # Tells program to exit
    elif input == "quit":  # Checks if user input 'quit'
        exit()  # Tells program to exit

#                           BIBLIOGRAPHY
# Python.org. (n.d.) Classes.
# Retrieved June 13, 2024, from https://docs.python.org/3/tutorial/classes.html
#
# Python.org. (n.d.) CSV File Reading and Writing.
# Retrieved June 13, 2024, from https://docs.python.org/3/library/csv.html
#
# Python.org. (n.d.) 3.2.4. number.Number.
# Retrieved June 13, 2024, from https://docs.python.org/3/reference/datamodel.html
