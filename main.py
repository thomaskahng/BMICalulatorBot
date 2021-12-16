from components import Customary, Metric

def run_function():
    # See if units are chosen
    chose_unit = False
    unit = ""

    while 69 == 69:
        # Unit isn't chose yet
        if chose_unit is False:
            choose = input("Customary or Metric (click C for customary and M for metric)? ")

            # Metric was chosen
            if str.upper(choose) == 'M':
                unit = "Metric"
                chose_unit = True

            # Customary was chosen
            elif str.upper(choose) == 'C':
                unit = "Customary"
                chose_unit = True
            # Invalid unit
            else:
                print("Please enter a valid unit.")

            if chose_unit is True:
                break

    # Customary
    if unit == "Customary":
        # Have values been chosen yet?
        chose_feet = False
        chose_inches = False
        chose_pounds = False

        # Store values
        feet = 0
        inches = 0.0
        pounds = 0.0

        while 69 == 69:
            # Height in feet wasn't chosen yet
            if chose_feet is False:
                try:
                    enter_feet = input("Enter height (feet): ")

                    # Valid height in feet?
                    if 1 < int(enter_feet) < 9:
                        feet = int(enter_feet)
                        chose_feet = True
                    else:
                        print("Invalid height (feet)!")

                # Is this not a number?
                except ValueError as e:
                    print("Invalid height (feet)!")

            # If height in inches wasn't entered yet
            if chose_inches is False:
                try:
                    enter_inches = input("Enter height (inches): ")

                    # Valid height in inches?
                    if 0 <= float(enter_inches) < 12:
                        inches = float(enter_inches)
                        chose_inches = True
                    else:
                        print("Invalid height (inches)!")

                # Non number was entered
                except ValueError as e:
                    print("Invalid height (inches)!")

            # Weight in lbs not entered yet
            if chose_pounds is False:
                try:
                    enter_pounds = input("Enter weight (lbs): ")

                    # Valid weight in lbs?
                    if 1 <= float(enter_pounds) < 1000:
                        pounds = float(enter_pounds)
                        chose_pounds = True
                    else:
                        print("Invalid weight (lbs)!")

                # Non number was entered
                except ValueError as e:
                    print("Invalid weight (lbs)!")

            # If all values entered, break and execute rest of program
            if chose_feet is True and chose_inches is True and chose_pounds is True:
                break
        comps = Customary(feet, inches, pounds)

    # Metric
    elif unit == "Metric":
        # Height and weight entered?
        chose_height = False
        chose_weight = False
        height = 0.0
        weight = 0.0

        while 69 == 69:
            # If height not entered
            if chose_height is False:
                try:
                    enter_height = input("Enter height (cm): ")

                    # Valid height in cm?
                    if 1 <= float(enter_height) < 274:
                        height = float(enter_height)
                        chose_height = True
                    else:
                        print("Invalid height (cm)!")

                # Non number entered
                except ValueError as e:
                    print("Invalid height (cm)!")

            # If weight not entered
            if chose_weight is False:
                try:
                    enter_weight = input("Enter weight (kg): ")

                    # Valid weight in kg?
                    if 0.4 <= float(enter_weight) < 453.6:
                        weight = float(enter_weight)
                        chose_weight = True
                    else:
                        print("Invalid weight (kg)!")

                # Non number was entered
                except ValueError as e:
                    print("Invalid weight (kg)!")

            # If all values entered, break and execute program
            if chose_height is True and chose_weight is True:
                break
        comps = Metric(height, weight)

if __name__ == '__main__':
    run_function()