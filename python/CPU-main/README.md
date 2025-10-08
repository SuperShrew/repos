HOW TO USE:

at the start of your code file use a ! and a number to define the time it takes in seconds to do part of a cycle (this is not necassary and is automatically set to 1)

also just so you know if you have used the ! at the start, the ram address you are storing your instruction in is line number - 2, if not it is line number - 1
and a blank line is automatically set to 0 in the ram
also NO WHITESPACES AT THE END, START OR IN THE MIDDLE OF LINES IT WILL NOT WORK as of now

IMPORTANT: always use a hashtag to halt the program, if no halt is specifed, the program will just give an error

e.g. (bad code)

3

1458

4

^ no hashtag at the end (baaad)

(good code)

3

1458

4 #

^ yayyy hashtag (good)

commands

1<address_here> = store current accumulator value at address specified. e.g. 187 (stores accumulator value at address 87)
be careful not to overwrite any code you have stored whilst using this and any other commands that set an address to a value

2<address_here> = store specified address' value into the accumulator (overwriting what was previously in it) e.g. 254 (stores address 54 value in accumulator)

3<type><address> = if type = 1 then it is a string input and the value is stored from <address> and onwards, each character being encoded in ascii
if type = 0 then it is an integer input and stores value in accumulator

4 = outputs current value in accumulator

5<operator><address_here> = if operator 0 adds the value in the accumulator and the value in the specified address, and overwrites the accumulator with the answer 
if operator 1 subtracts the value in the accumulator and the value in the specified address, and overwrites the accumulator with the answer 
e.g. 5046 (adds accumulator value and value at address 46 and outputs the result to the accumulator)

6 = unused

7<mode><address_1(3 digits)><address_2><address3> = branch if zero. 
mode = 0: moves the program counter to address_2 if address_1 is 0
e.g. 713267 (if address 132's value is 0, the program counter will be set to excecute from address 67)
mode = 1: moves program counter to address 2 if address 1 = address 3

8<number> = an old thing i decided to keep (may be removed in the future) sets accumulator to number defined
e.g. 871 (sets accumulator value to 71)

9 = converts value in accumulator to the corresponding ascii character and then outputs it (does not overwrite accumulator)