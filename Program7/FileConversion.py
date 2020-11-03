"""
Jeffrey Lansford
11/2/2020
Program 7
Python version of removing content from file when seeing a Control-C and stopping when seeing a Control-B
"""

import sys

if __name__ == "__main__":

    # command line arguemnts for file input and output
    fileInputName = sys.argv[1]
    fileOutputName = sys.argv[2]

    # set to to write input to output file
    deletemode = False
    # open output file for writing
    fileOutput = open(fileOutputName, "w")
    # open corrupted file
    with open(fileInputName, "r", encoding="ascii") as fileInput:
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
        print(f"Successfully wrote to {fileOutputName}")
