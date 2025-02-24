#poject  countdown 
import time

def print_large_digit(digit):
    """
    Prints the large digit passed as an argument.
    
    Args:
        digit (int): The digit to be printed as a large character.
    """
    digit_patterns = [
        [" === ",
         "*   *",
         "*   *",
         "*   *",
         " === "],
        ["  *  ",
         " **  ",
         "  *  ",
         "  *  ",
         " *** "],
        [" *** ",
         "    *",
         " *** ",
         "*    ",
         " *** "],
        [" *** ",
         "    *",
         " *** ",
         "    *",
         " *** "],
        ["*   *",
         "*   *",
         " *** ",
         "    *",
         "    *"],
        [" *** ",
         "*    ",
         " *** ",
         "    *",
         " *** "],
        [" *** ",
         "*    ",
         " *** ",
         "*   *",
         " *** "],
        [" *** ",
         "    *",
         "    *",
         "    *",
         "    *"],
        [" *** ",
         "*   *",
         " *** ",
         "*   *",
         " *** "],
        [" *** ",
         "*   *",
         " *** ",
         "    *",
         " *** "]
    ]

    for line in digit_patterns[digit]:
        print(line)

for i in range(5, -1, -1):
    print_large_digit(i)
    time.sleep(1) 

