import os , Functions

def CopyPaste():
    FirstFile = input("Введите имя файла для копирования:                                                   ")
    if FirstFile == "back":
        Functions.Back()
    if FirstFile == "cls":
        Functions.ClearConsole() 
    FileLocation = input("Введите место хранения исходного файла:                                           ")
    if FileLocation == "back":
        Functions.Back()
    if FileLocation == "cls":
        Functions.ClearConsole() 
    SecondFile = input("Введите имя файла, в который будет передаваться информация:                          ")
    if SecondFile == "back":
        Functions.Back() 
    if SecondFile == "cls":
        Functions.ClearConsole()
    PlaceOfPreservation = input("Введите путь для сохранения файла:                                             ")

    if FirstFile == "cls" or SecondFile == "cls":
        os.system('cls')
        CopyPaste()

    try:
        CopiedFile = open(str(FileLocation) + "\\" + str(FirstFile) , 'r')
        PastedFile = open(str(PlaceOfPreservation) + "\\" + str(SecondFile) , 'w')

        CopyInformation = CopiedFile.read()
                
        if CopyInformation == 0:
            print("Исхоный файл не содержит никакой информации.                                             ")
        else:
            print("Скопированная информация:                                                            " + str(CopyInformation))
            PastedFile.write(CopyInformation)
            print("Информация успешно скопирована!")

            CopiedFile.close()
            PastedFile.close()

    except FileNotFoundError:
        print("Введенный вами файл не существует! Попробуйте снова!")