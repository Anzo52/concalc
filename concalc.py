# Python program to calculate the volume of concrete needed for curb/gutter, sidewalk, and patio
# returns cubic yards


def sidewalk(thickness_in, width_ft, length_ft):
    thickness_yd = thickness_in / 36
    width_yd = width_ft / 3
    length_yd = length_ft / 3
    sidewalk_vol = (width_yd * length_yd * thickness_yd)
    return sidewalk_vol


def patio(thickness_in, width_ft, length_ft):
    thickness_yd = thickness_in / 36
    width_yd = width_ft / 3
    length_yd = length_ft / 3
    patio_vol = (width_yd * length_yd * thickness_yd)
    return patio_vol


def curb(toe_in, base_ft, curb_in, face_in, length_ft):
    toe_yd = toe_in / 36
    base_yd = base_ft / 3
    curb_yd = curb_in / 36
    face_yd = face_in / 36
    length_yd = length_ft / 3
    curb_vol = ((base_yd * toe_yd) + (curb_yd * face_yd)) * length_yd
    return curb_vol


def main():
    print("Curb, Sidewalk, or Patio?")
    if input() == "Curb" or "curb":
        print("Enter the toe of the curb in inches:")
        toe_in = int(input())
        print("Enter the base of the curb in feet:")
        base_ft = int(input())
        print("Enter the length of the curb in feet:")
        length_ft = int(input())
        print("Enter the thickness of the curb in inches:")
        int(input())
        print("Enter the face of the curb in inches:")
        face_in = int(input())
        print("Enter the curb in inches:")
        curb_in = int(input())
        print("The volume of the curb is:", curb(toe_in, base_ft, curb_in, face_in, length_ft))
    elif input() == "Sidewalk" or "sidewalk":
        print("Enter the thickness of the sidewalk in inches:")
        thickness_in = int(input())
        print("Enter the width of the sidewalk in feet:")
        width_ft = int(input())
        print("Enter the length of the sidewalk in feet:")
        length_ft = int(input())
        print("The volume of the sidewalk is:", sidewalk(thickness_in, width_ft, length_ft))
    elif input() == "Patio" or "patio":
        print("Enter the thickness of the patio in inches:")
        thickness_in = int(input())
        print("Enter the width of the patio in feet:")
        width_ft = int(input())
        print("Enter the length of the patio in feet:")
        length_ft = int(input())
        print("The volume of the patio is:", patio(thickness_in, width_ft, length_ft))
    else:
        print("Please enter either 'Curb', 'Sidewalk', or 'Patio'")
        main()


main()
