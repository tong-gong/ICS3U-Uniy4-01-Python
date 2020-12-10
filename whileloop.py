#!/usr/bin/env python3

# Created by Tong Gong
# Created time December 2020
# This is a while loop program.


def main():
    # This is the function to run while loop.

    loop_counter = 0
    # Input
    user_input_str = input("How many time to repeat:")
    print("")

    # Process & output
    try:
        user_input_int = int(user_input_str)
        if user_input_int > 0:
            while loop_counter < int(user_input_int):
                print("{0} time through the loop.".format(loop_counter))
                loop_counter = loop_counter + 1
        elif user_input_int < 0:
            print("Sorry, you did not enter a positive integer!")
    except Exception:
        print("You are not type in an integer!")


if __name__ == "__main__":
    main()
