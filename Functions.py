import os , MainCode

def Exit():
    print("Программа завершена! До свидания!")


ListOfOperations = ["Copy/Paste\t\t-- Enter the name of the start and end files." ,
                    "Create new file\t-- Enter the name of the file to be created." , 
                    "Edit file\t\t-- Enter the name of the file to be changed." , 
                    "Rename file\t\t-- Enter the name of the file to be renamed." , 
                    "Remove file\t\t-- Deletes the file you entered" , 
                   #"Create directory\t-- Enter the name of the directory to be created:" ,
                    "cls\t\t\t-- Очистить текущую консоль." ,
                    "back\t\t\t-- Вернуться к предыдущей операции." ,
                    "--help\t\t-- Помощь. Список команд."]

def Info():
    OperationIndex = 1
    print("Hello! Here is a list of what I can do:")
    for i in ListOfOperations:
        print("\t" + str(OperationIndex) + ". "  + str(i))
        OperationIndex += 1

def ProgramStatus():
    print("\t\t\t\tThe program is running!" , end = '\n\n')

def Back():
    return MainCode.SuperMainCode()

def ClearConsole():
    os.system('cls')
    ProgramStatus()