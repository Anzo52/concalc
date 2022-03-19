# concrete calculator - calculate concrete volume based on user input
# Curb and gutter - in: base (inches), back height (inches), curb width (inches), toe height (inches), gutter width (inches), face height (inches)
# Sidewalk - in: thickness (inches), width (feet), length (feet)
# Patio/other - in: dimension1 (feet), dimension2 (feet), thickness (inches)
# Program will take input from command line and output volume in cubic feet


import sys  # for command line arguments
import math  # for math functions


def main():
    # check if user input is correct
    if len(sys.argv) != 2:
        print("Usage: python3 concalc.py <concrete type>")
        sys.exit()

    # get user input
    user_input = sys.argv[1]

    # check if user input is valid
    if user_input not in ["curb-gutter", "sidewalk", "patio"]:
        print("Invalid input. Please enter curb-gutter, sidewalk, or patio.")
        sys.exit()

    # get user input
    user_input = sys.argv[1]


    # curb-gutter
    if user_input == "curb-gutter":
        curb_gutter()

    # sidewalk
    elif user_input == "sidewalk":
        sidewalk()

    # patio
    elif user_input == "patio":
        patio()


def curb_gutter():
    # get user input
    base = float(input("Enter base (inches): "))
    back_height = float(input("Enter back height (inches): "))
    curb_width = float(input("Enter curb width (inches): "))
    toe_height = float(input("Enter toe height (inches): "))
    gutter_width = float(input("Enter gutter width (inches): "))
    face_height = float(input("Enter face height (inches): "))

    # calculate volume
    volume = ((base * back_height) + (curb_width * toe_height) + (gutter_width * face_height)) * 12
    print("Volume:", volume, "cubic feet")


def sidewalk():
    # get user input
    thickness = float(input("Enter thickness (inches): "))
    width = float(input("Enter width (feet): "))
    length = float(input("Enter length (feet): "))

    # calculate volume
    volume = (thickness * width * length) * 27
    print("Volume:", volume, "cubic feet")


def patio():
    # get user input
    dimension1 = float(input("Enter dimension1 (feet): "))
    dimension2 = float(input("Enter dimension2 (feet): "))
    thickness = float(input("Enter thickness (inches): "))

    # calculate volume
    volume = (dimension1 * dimension2 * thickness) * 27
    print("Volume:", volume, "cubic feet")


if __name__ == "__main__":
    main()


# end of file