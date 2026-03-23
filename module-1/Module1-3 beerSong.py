def getBottleCount():
    ##Ask the user how many bottles of beer are on the wall. Validate input.##
    while True:
        try:
            bottles = int(input("How many bottles of beer on the wall? "))
            if bottles > 0:
                return bottles
            else:
                print("Please enter a whole number greater than zero.")
        except ValueError:
            print("Bottles of beer must be a whole number. Try again.")


def bottleS(count):
    ##Return correct pluralization.##
    return "bottle" if count == 1 else "bottles"


def printLine(current):
    ##Print one line with correct pluralization.##
    print(
        f"{current} {bottleS(current)} of beer on the wall, "
        f"{current} {bottleS(current)} of beer."
    )

    bottleFunct = current - 1

    if bottleFunct > 0:
        print(
            f"Take one down and pass it around, "
            f"{bottleFunct} {bottleS(bottleFunct)} of beer on the wall.\n"
        )
    else:
        print(
            "Take one down and pass it around, "
            "no more bottles of beer on the wall.\n"
        )


def beerSong(bottles):
    ##Print the full song.##
    for i in range(bottles, 0, -1):
        printLine(i)

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Time to buy some more.\n")


def programExit():
    ##Ask user if they want to sing again.##
    return input("Would you like to sing again? (Y/N): ").upper() == "Y"


def main():
    ##Main program loop.##
    while True:
        bottles = getBottleCount()
        beerSong(bottles)

        if not programExit():
            print("Exiting...")
            break


##Start the program##
main()