"""
Jeffrey Lansford
11/2/2020
Program 7
Python version of removing content from file when seeing a Control-C and stopping when seeing a Control-B
"""

if __name__ == "__main__":
    print("Python")
    # set to to write input to output file
    deletemode = False
    # open output file for writing
    fileOutput = open("control-char-output-Python.txt", "w")
    # open corrupted file
    with open("control-char.txt", "r", encoding="ascii") as fileInput:
        while True:
            # read in one character at a time
            c = fileInput.read(1)
            # reached End of File
            if not c:
                print("End of File")
                break
            # see Control-C character acsii value and start not writing input to output file
            if ord(c) == 3:
                deletemode = True

            # write input to output if we are not in delete mode
            if not deletemode:
                fileOutput.write(c)
            # when seeing a Control-B character ascii value, start writing to ouptut file
            if ord(c) == 2:
                deletemode = False

        # close files
        fileInput.close()
        fileOutput.close()
        print("Successfully wrote to control-char-output-Python.txt")