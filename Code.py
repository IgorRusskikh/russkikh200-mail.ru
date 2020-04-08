import os , MainCode , Functions

os.system('cls')

Functions.ProgramStatus()

def Function():
    InitialAction = input("Пожалуйста, прочитайте инструкцию!\
Для этого напишите \'--help \' или напишите \'next \', чтобы продолжить. \
Для завершения работы программы напишите \'exit\'. Не забывайте писать расширения файлов! : ")

    if InitialAction == "--help":
        os.system('cls')
        Functions.ProgramStatus()
        Functions.Info()
        MainCode.SuperMainCode()
    elif InitialAction == "next":
        MainCode.SuperMainCode()
    elif InitialAction == "exit":
        Functions.Exit()
    elif InitialAction == "cls":
        Functions.ClearConsole()
        Functions.ProgramStatus()
        Function()

    else:
        Function()

Function()