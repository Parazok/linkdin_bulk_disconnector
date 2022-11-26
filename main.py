from colors import mprint, bcolors
from utils import clrscr
from utils import pars_curl, write_session_files, read_session_files
from pprint import pp

def main():
    mprint(
        """
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠁⠀⠀⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠉⠉⠉⣿⣿⣿⠉⠉⠉⠟⠉⠉⠉⠻⣿⣿⣿⣿
⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⠀⠀⠀⣠⣤⡀⠀⠀⢹⣿⣿⣿
⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣀⣀⣀⣿⣿⣿⣀⣀⣀⣿⣿⣇⣀⣀⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
           """,
        color=bcolors.BLUE,
    )

    mprint("welcome to parazok linkedin helper!\n\n\n", header=True)
    cookies, headers = read_session_files()
    # pp(cookies)
    # pp(headers)
    mprint('press "ENTER" to continue..')
    input()

    while True:
        clrscr()
        mprint("what do you want to do?\n", header=True)
        mprint("""
1 process curl.txt file.
2 go to bulk unconnector menu.
3 go to follower evener menu.
0 to close program.
           """)
        raw_i = input("action: ")
        if raw_i == '1':
            r = pars_curl("./curl.txt")
            if not r:
                mprint("bad curl or no curl.txt file! make sure of it and try again.",
                       color=bcolors.FAIL)
            else:
                write_session_files(*r)
                
            input('press "ENTER" to continue!')

        elif raw_i == '2':
            pass
        elif raw_i == '3':
            pass
        elif raw_i == '0':
            clrscr()
            mprint("\n\nBye Bye..!\n\n")
            return 1
        else:
            clrscr()
            print("wrong input, try again!")
            input('press "ENTER" to continue!')

    clrscr()


if __name__ == "__main__":
    main()
