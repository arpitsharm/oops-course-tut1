userinput = int(input('''
1.Create File
2.Read File
3.Write File 
Enter Choise :- 
'''))

class CreateFile:
    def __init__(self):
        with open(f"{filenamec}", "w") as f:
            print("File Created!!!")

class ReadFile:
    def __init__(self):
        with open(f"{filenamer}", "r") as f:
            filereadans = f.read()
            print(filereadans)


class WriteFile:
    def __init__(self):
        with open(f"{filenamew}", "a+") as f:
            f.write(text)
            print("Write File Successfully!!!")



if userinput == 1:
    filenamec = input("filename>")
    oc = CreateFile()

elif userinput == 2:
    filenamer = input("filename>")
    orf = ReadFile()

elif userinput == 3:
    filenamew = input("filename>")
    text = input("text>")
    ow = WriteFile()

else:
    print("404 Error!!!")