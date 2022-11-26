class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def mprint(*txts, header=False, color=bcolors.GREEN):
    pre = ""
    if header:
        pre += bcolors.BOLD + bcolors.HEADER + bcolors.UNDERLINE + bcolors.BLUE
    else:
        pre += color

    print(pre + " ".join(txts) + bcolors.ENDC)
