import os

def EditFile():
    ExistingFile = input("Введите имя существующего файла:                                                  ")
    FileLocation = input("Введите место хранения исходного файла:                                           ")

    try:
        File = open(str(FileLocation) + "\\" +str(ExistingFile) , 'a')

        Text = input("Напишите текст, который вы хотите добавить в файл:")

        File.write(" " + str(Text))
        print("Информация успешно добавлена! Файл сохранен!")
        File.close()

    except FileNotFoundError:
        print("Произошла ошибка при изменении файла! Попробуйте снова")
