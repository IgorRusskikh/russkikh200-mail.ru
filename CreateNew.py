import os , Functions

def CreateNewFile():
    CreatedFile = input("Введите имя файла, который будет создан:                                           ")
    PlaceOfPreservation = input("Введите место сохранение файла:                                                ")

    try:
        File = open(str(PlaceOfPreservation) + "\\" + str(CreatedFile) , 'w+')

        Text = input("Введите текст, который вы хотите поместить в файл:                                    ")

        File.write(Text)
        print("Информация успешно записана!")
        File.close()

    except FileNotFoundError:
        print("Ошибка записи в файл! Попробуйте снова!")
