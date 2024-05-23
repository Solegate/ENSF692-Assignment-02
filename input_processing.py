# input_processing.py
# Maheesha_Munasinghe, ENSF 692 P24
# A terminal-based program for processing detected obstacles in a car's vision system.

# No global variables are permitted
# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        # Initialize attributes with their default values.
        self.traffic_light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # Method to update and store the status based on user input.
    def update_status(self, first_input, second_input):
        if first_input == 1:
            self.traffic_light = second_input
        if first_input == 2:
            self.pedestrian = second_input
        if first_input == 3:
            self.vehicle = second_input


# Function to print the current action message and current status of the sensor.
def print_message(sensor):
    # Default message for initial and default status ("green" + "no" + "no").
    message = "Proceed"

    # Determine the action message based on sensor's current status.
    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        message = "STOP"
    elif sensor.traffic_light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        message = "Caution"

    # Display the action message and current status of three attributes.
    print(f"\n{message}")
    print(f"\nLight = {sensor.traffic_light} , Pedestrian = {sensor.pedestrian} , Vehicle = {sensor.vehicle} .")


# Main function for the program execution. Takes user inputs and responds based on logic.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()  # Create an object from Sensor class
    valid_inputs = {"red", "green", "yellow", "yes", "no"}  # Define a set of valid input values

    # Loop to keep asking for user input until the user enters 0 to exit the program.
    while True:
        try:
            print("\nAre changes detected in the vision input?")
            first_input = int(input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: "))
            if first_input == 0:
                break
            elif first_input in [1, 2, 3]:
                second_input = input("What change has been identified?: ")
                if second_input not in valid_inputs:
                    print("Invalid vision change.")
                    print_message(sensor)
                    continue  # Skip the rest of the loop and prompt again
                else:
                    sensor.update_status(first_input, second_input)
                    print_message(sensor)
        except ValueError:
            # Handle case where user input is not an integer.
            print("You must select either 1, 2, 3, or 0.")
            continue


if __name__ == '__main__':
    main()
