import os


def pause(message="Press enter to continue...\n", end=False):
    if end:
        input("To be continued...")
    else:
        input(message)


def prompt(string="What do you do?"):
    print(string)
    x = input(">> ")
    return x.lower()


def clear():
    os.system("cls")


def borderpr(text):
    # text should be split on newline chars
    x = text.split("\n")

    # variables for formatting
    align = "<"
    length = 0
    tablength = 0
    newText = ""
    flags = ("<", "^", ">")

    # loop over data to get relevant lengths for formatting
    for line in x:
        f = line[1:].split("\t")
        if len(f) > 1:
            tablength = len(f[0]) if len(f[0]) > tablength else tablength
        length = len(line) if len(line) > length else length

    # create dividers for output
    border = f"=={'':=<{length}}==\n"
    dotline = f"= {'...':^{length}} =\n"

    # format the output
    newText += border
    newText += dotline
    for line in x:
        # fixes issue with blank lines being skipped
        if line == "":
            newText += f"= {'':{length}} =\n"
        else:
            # if first char is alingment flag, remove it and store for formatting use
            if line[0] in flags:
                align = line[0]
                line = line[1:]
            f = line.split("\t")
            if len(f) > 1:
                newText += f"= {f[0]:{tablength}} {f[1]:{length - tablength - 1}} =\n"
            else:
                newText += f"= {line:{align}{length}} =\n"
    newText += dotline
    newText += border

    print(newText)
