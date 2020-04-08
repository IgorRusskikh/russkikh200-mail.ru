import os

def RenameFile():
    try:
        File = input("Введите имя существующего файла:                                                      ")
        FileLocation = input("Введите место хранения файла:                                                         ")
        NewFileName = input("Введите новое имя файла:                                                               ")

        os.rename(str(FileLocation) + "\\" + str(File) , NewFileName)
        print("Файл успешно переименован! Его имя место хранения:                                       " + str(FileLocation) + "\\" + str(NewFileName))
    except FileNotFoundError:
        print("Введенный вами файл не существует!")