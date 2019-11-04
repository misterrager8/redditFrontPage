import praw
from post import post
import webbrowser
import tkinter
import sys
from tkinter import messagebox

reddit = praw.Reddit()

results = []
savedResults = []

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
    
def viewSaved():
  savedResults.clear()
  postsList2.configure(state="normal")
  postsList2.delete(1.0, tkinter.END)
  
  for submission in reddit.redditor('').saved():
    current = post(submission.title,
                   submission.subreddit.display_name,
                   submission.url,
                   submission.id)
    savedResults.append(current)

  for idx, item in enumerate(savedResults):
    x = str(idx + 1) + " - " + item.title + " (" + item.sub + ")\n"
    postsList2.configure(state="normal")
    postsList2.insert(tkinter.END, x)
    postsList2.configure(state="disabled")
    
def submitButtonClicked(num):
  numField.delete(0, tkinter.END)
  webbrowser.open(results[num - 1].link)
    
def saveButtonClicked(num):
  numField2.delete(0, tkinter.END)
  selected = reddit.submission(id = results[num - 1].postID)
  selected.save()
  viewSaved()
    
def unsaveButtonClicked(num):
  numField3.delete(0, tkinter.END)
  selected = reddit.submission(id = savedResults[num - 1].postID)
  selected.unsave()
  viewSaved()
    
def openSaveButtonClicked():
  linkx = ""
  webbrowser.open(linkx)

mainWindow = tkinter.Tk()
mainWindow.title("Reddit Front Page")

refreshButton = tkinter.Button(mainWindow, text = "Refresh", command = viewPosts)
refreshButton.pack()

postsList = tkinter.Text(mainWindow, wrap="none")
postsList.pack()
  
numField = tkinter.Entry(mainWindow)
numField.pack()

submitButton = tkinter.Button(mainWindow, text = "Go To Post", command = lambda: submitButtonClicked(int(numField.get())))
submitButton.pack()
  
numField2 = tkinter.Entry(mainWindow)
numField2.pack()

saveButton = tkinter.Button(mainWindow, text = "Save Post", command = lambda: saveButtonClicked(int(numField2.get())))
saveButton.pack()
  
numField3 = tkinter.Entry(mainWindow)
numField3.pack()

unsaveButton = tkinter.Button(mainWindow, text = "Unsave Post", command = lambda: unsaveButtonClicked(int(numField3.get())))
unsaveButton.pack()

openSaveButton = tkinter.Button(mainWindow, text = "Open Saved Page", command = openSaveButtonClicked)
openSaveButton.pack()

postsList2 = tkinter.Text(mainWindow, wrap="none")
postsList2.pack()

viewPosts()
viewSaved()
mainWindow.mainloop()