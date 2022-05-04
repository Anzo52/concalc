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

# TODO cast to doubles
def curb_gutter():
    base_width = float(input("Enter base width (inches): "))
    gutter_width = float(input("Enter gutter width (inches): "))
    curb_width = float(input("Enter curb width (inches): "))
    toe_height = float(input("Enter toe height (inches): "))
    face_height = float(input("Enter face height (inches): "))
    back_height = float(input("Enter back height (inches): "))
    length = float(input("Enter length (feet): "))
    
    # calculate volume
    volume_cube_ft = (((base_width / 12) * (toe_height / 12)) + ((curb_width / 12) * (face_height / 12))) * length
    volume_cube_yrd = volume_cube_ft / 27
    print("You need: ", volume_cube_yrd, " yards.")


# FIXME math is wrong, need cubic yards
def sidewalk():
    # get user input
    thickness = float(input("Enter thickness (inches): "))
    width = float(input("Enter width (feet): "))
    length = float(input("Enter length (feet): "))

    # calculate volume
    vol_cube_ft = (thickness * 12) * width * length
    vol_cube_yrd = vol_cube_ft / 27
    print("You need: ", vol_cube_yrd, " yards.")


def patio():
    thickness = float(input("Enter thickness (inches): "))
    width = float(input("Enter width (feet): "))
    length = float(input("Enter length (feet): "))

    # calculate volume
    vol_cube_ft = (thickness * 12) * width * length
    vol_cube_yrd = vol_cube_ft / 27
    print("You need: ", vol_cube_yrd, " yards.")


if __name__ == "__main__":
    main()


# end of file
