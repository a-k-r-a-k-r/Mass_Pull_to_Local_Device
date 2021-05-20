import tkinter
from tkinter import filedialog
import os


root=tkinter.Tk()
root.title("Mass pull")
root.geometry("300x400")

def git_pull():
    path=filedialog.askdirectory(initialdir="./")
    print("Selected folder path: ",path)
    os.chdir(path)
    repos=os.listdir(path)
    print("Repositories found: ",repos)
    no_of_repo = len(repos)
    completed = 0
    successful_count = 0
    unsuccessful_count = 0


    for repo in repos:
        os.chdir(repo)
        operation_status = os.system("git pull")
        if(operation_status == 1):
            print("Error!!")
            unsuccessful_count+=1
        else:
            print("Pulled {}".format(repo))
            completed+=1
            percentage_completion = (completed/no_of_repo)*100
            print("{} % Completed".format(percentage_completion))
            successful_count+=1
        os.chdir(path)
    
    print("Success Rate: {} %\nFailure Rate: {} %".format((successful_count/no_of_repo)*100,(unsuccessful_count/no_of_repo)*100))
        




getbutton=tkinter.Button(root,bg="green",text="Mass Pull",command=git_pull)
getbutton.pack()

root.mainloop()