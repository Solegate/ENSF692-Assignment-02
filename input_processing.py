# input_processing.py
# Maheesha_Munasinghe, ENSF 692 P24
# A terminal-based program for processing detected obstacles in a car's vision system.

class Sensor:
    """
    Represents the status of a car's sensor system.
    """

    def __init__(self, light='green', pedestrian='no', vehicle='no'):
        """
        Initializes the Sensor object with default values.
        Parameters:
            light (str): The traffic light color ('green', 'yellow', 'red').
            pedestrian (str): Presence of a pedestrian ('yes', 'no').
            vehicle (str): Presence of another vehicle ('yes', 'no').
        """
        # Set default values for the sensor attributes
        self.light = light  # Initial state of the traffic light
        self.pedestrian = pedestrian  # Initial state of pedestrian detection
        self.vehicle = vehicle  # Initial state of vehicle detection

    def update_status(self):
        """
        Updates the sensor status based on user input.
        Returns:
            str: The type of change detected, or 'null' if the input was invalid.
        """
        print("Detecting changes in the sensor input...")  # Inform the user that the program is ready for input

        try:
            # Step 1: Prompt the user to specify the type of change
            change = input("Enter 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to exit: ")

            # Step 2: Validate the user input
            if change not in ["0", "1", "2", "3"]:
                raise ValueError  # Raise an error if the input is invalid
            else:
                # Step 3: Handle the different cases of input
                if change == "1":  # Update the traffic light status
                    light_change = input("Specify the light change (green, yellow, red): ").lower()
                    if light_change in ["green", "yellow", "red"]:
                        self.light = light_change
                    else:
                        print("Invalid light change specified.\n")
                elif change == "2":  # Update the pedestrian status
                    ped_change = input("Is there a pedestrian? (yes, no): ").lower()
                    if ped_change in ["yes", "no"]:
                        self.pedestrian = ped_change
                    else:
                        print("Invalid pedestrian status specified.\n")
                elif change == "3":  # Update the vehicle status
                    veh_change = input("Is there another vehicle? (yes, no): ").lower()
                    if veh_change in ["yes", "no"]:
                        self.vehicle = veh_change
                    else:
                        print("Invalid vehicle status specified.\n")
                elif change == "0":  # Exit the program
                    return "0"
        except ValueError:
            print("Please enter a valid option: 0, 1, 2, or 3")  # Inform the user of invalid input
            return "null"  # Return "null" if an invalid input was provided

        # Step 4: Return the change detected
        return change

def display_action(sensor):
    """
    Displays the appropriate action based on the sensor status.
    Parameters:
        sensor (Sensor): The sensor object containing current status.
    """
    # Step 5: Determine the action to take based on sensor status
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("\nAction: STOP\n")  # Stop if any critical condition is met
    elif sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\nAction: CAUTION\n")  # Proceed with caution if the light is yellow and no obstacles are detected
    elif sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no":
        print("\nAction: PROCEED\n")  # Proceed if the light is green and no obstacles are detected

def main():
    """
    Main function to execute the sensor processing program.
    """
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")  # Program title

    # Step 6: Create a Sensor object
    car_sensor = Sensor()  # Initialize the sensor object
    user_input = ""  # Variable to store user input

    while True:
        # Step 7: Update the sensor status based on user input
        user_input = car_sensor.update_status()
        if user_input == "0":
            break  # Exit the loop if the user chooses to end the program
        elif user_input != "null":
            # Step 8: Display the appropriate action based on sensor status
            display_action(car_sensor)
            # Step 9: Show the updated status
            print(f"Current Status -> Light: {car_sensor.light}, Pedestrian: {car_sensor.pedestrian}, Vehicle: {car_sensor.vehicle}\n")

if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly
