

if __name__ == "__main__":
    print("Python")
    deletemode = False
    fileOutput = open("control-char-output-Python.txt", "w")
    with open("control-char.txt", "r", encoding="ascii") as fileInput:
        while True:
            c = fileInput.read(1)
            if not c:
                print("End of File")
                break
            if ord(c) == 3:
                deletemode = True

            if not deletemode:
                fileOutput.write(c)
                # fileOutput.write("a")
            if ord(c) == 2:
                deletemode = False
            # print("Character: {}". format(ord(c)))
