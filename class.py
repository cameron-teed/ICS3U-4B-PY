#!/usr/bin/env python3

# Created by: Cameron Teed
# Created on: Oct 2019
# This is program finds out if it's a leap year


def main():
    # calculates if it is a leap year

    # input
    total_classes = input("Please enter the total amount of classes held: ")
    attendance = input("Please enter the total amount of classes attended: ")

    # process and output
    try:

        total_classes = int(total_classes)
        attendance = int(attendance)

        total = attendance/total_classes
        total = total * 100
        total = round(total)

        if total >= 75 and total <= 100:
            print("")
            print("you can attend the exam. ({}% attendance)".format(total))

        elif total >= 0 and total <= 74:
            print("")
            print("you can not attend the exam. ({}% attendance)"
                  .format(total))

        else:
            print("")
            print("please enter a valid class number and attendance")

    except Exception:
        print("")
        print("Please put in a integer.")


if __name__ == "__main__":
    main()
