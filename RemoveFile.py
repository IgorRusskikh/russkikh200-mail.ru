import os

def RemoveFile():
    try:
        File = input("Введите имя файла, который вы хотите удалить:                                         ")
        FileLocation = input("Введите место хранения существующего файла:                                           ")

        os.remove(str(FileLocation) + "\\" + str(File))
        print("Файл успешно удален!")
    except:
        print("Введенный вами файл не существует!")