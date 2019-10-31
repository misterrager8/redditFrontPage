import praw
from post import post
import webbrowser
import tkinter

reddit = praw.Reddit()

results = []

for submission in reddit.front.hot(limit=50):
  current = post(submission.title, submission.subreddit.display_name, submission.url)
  results.append(current)

def submitButtonClicked(num):
  numField.delete(0, tkinter.END)
  webbrowser.open(results[num - 1].link)

#def saveButtonClicked(num):
#  numField2.delete(0, tkinter.END)

mainWindow = tkinter.Tk()
mainWindow.title("Reddit Front Page")

lis = tkinter.Text(mainWindow, wrap="none")
lis.pack()
  
numField = tkinter.Entry(mainWindow)
numField.pack()

submitButton = tkinter.Button(mainWindow, text = "Submit", command = lambda: submitButtonClicked(int(numField.get())))
submitButton.pack()
  
#numField2 = tkinter.Entry(mainWindow)
#numField2.pack()
#
#saveButton = tkinter.Button(mainWindow, text = "Submit", command = lambda: submitButtonClicked(int(numField.get())))
#saveButton.pack()

for idx, i in enumerate(results):
  x = str(idx + 1) + " - " + i.title + " (" + i.sub + ")\n"
  lis.configure(state="normal")
  lis.insert(tkinter.END, x)
  lis.configure(state="disabled")

mainWindow.mainloop()