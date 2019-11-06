#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program finds the HFC


def main():
    # this function finds the HCF
    smaller = 0
    hfc = 0

    print("Welcome to the HCF calculator.")
    print("")
    first_num_as_string = input("First number: ")

    # process & output
    try:
        first_num = int(first_num_as_string)
        second_num_as_string = input("Second number: ")
        try:
            second_num = int(second_num_as_string)
            # choose the smaller number
            if first_num > second_num:
                smaller = second_num
            else:
                smaller = first_num
            # Use loop to find HCF
            for counter in range(1, smaller + 1):
                if (first_num % counter == 0) and (second_num % counter == 0):
                    hcf = counter
            print("")
            print("The H.C.F. of {0} and {1} is {2}."
                  .format(first_num, second_num, hcf))
        except Exception:
            print("Wrong input. Try again.")
    except Exception:
        print("Wrong input. Try again.")


if __name__ == "__main__":
    main()
