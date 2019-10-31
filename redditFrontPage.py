import praw
from post import post
import webbrowser
import tkinter
import sys
from tkinter import messagebox

reddit = praw.Reddit()

results = []

def viewPosts():
  results.clear()
  postsList.configure(state="normal")
  postsList.delete(1.0, tkinter.END)
  
  for submission in reddit.front.hot(limit=50):
    current = post(submission.title,
                   submission.subreddit.display_name,
                   submission.url,
                   submission.id)
    results.append(current)

  for idx, item in enumerate(results):
    x = str(idx + 1) + " - " + item.title + " (" + item.sub + ")\n"
    postsList.configure(state="normal")
    postsList.insert(tkinter.END, x)
    postsList.configure(state="disabled")
    
def submitButtonClicked(num):
  numField.delete(0, tkinter.END)
  webbrowser.open(results[num - 1].link)
    
def saveButtonClicked(num):
  numField2.delete(0, tkinter.END)
  selected = reddit.submission(id = results[num - 1].postID)
  selected.save()
  messagebox.showinfo("Saved", "Post Saved")

mainWindow = tkinter.Tk()
mainWindow.title("Reddit Front Page")

exitButton = tkinter.Button(mainWindow, text = "Exit", command = sys.exit)
exitButton.pack()

refreshButton = tkinter.Button(mainWindow, text = "Refresh", command = viewPosts)
refreshButton.pack()

postsList = tkinter.Text(mainWindow, wrap="none")
postsList.pack()
  
numField = tkinter.Entry(mainWindow)
numField.pack()

submitButton = tkinter.Button(mainWindow, text = "Submit", command = lambda: submitButtonClicked(int(numField.get())))
submitButton.pack()
  
numField2 = tkinter.Entry(mainWindow)
numField2.pack()

saveButton = tkinter.Button(mainWindow, text = "Save", command = lambda: saveButtonClicked(int(numField2.get())))
saveButton.pack()

viewPosts()
mainWindow.mainloop()