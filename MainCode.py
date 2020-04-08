import os , Paste , CreateNew , EditFile , RenameFile , RemoveFile , Functions 

def SuperMainCode():
    while True:
        OperationChoice = input("Выберите операцию. Если вы не прочитали инструкции, введите \'--help \'. Если хотите выйти, введите \'exit\':\t\t")

        if OperationChoice == "--help":
            Functions.Info()
        elif OperationChoice == "cls":
            Functions.ClearConsole()
        elif OperationChoice == "exit":
            Functions.Exit()
            break
            
        elif OperationChoice == "1" or OperationChoice == "copy":
            Paste.CopyPaste()

        elif OperationChoice == "2" or OperationChoice == "create":
            CreateNew.CreateNewFile()

        elif OperationChoice == "3" or OperationChoice == "edit":
            EditFile.EditFile()

        elif OperationChoice == "4" or OperationChoice == "rename":
            RenameFile.RenameFile()

        elif OperationChoice == "5" or OperationChoice == "remove":
            RemoveFile.RemoveFile()