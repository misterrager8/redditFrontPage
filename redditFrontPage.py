from javax.swing import *
from java.awt import *
import sys
import csv
import webbrowser
from post import post
import subprocess
from java.text import SimpleDateFormat
from java.util import *
from datetime import datetime
from javax.swing.table import *

mouseLoc = []
postList = []

class dtm(DefaultTableModel):
  def __init__(self):
    head = "Post Title,Sub,ID".split(",")
    self.data = []
    DefaultTableModel.__init__(self, self.data, head)
    
  def isCellEditable(self, row, col):
    return False

class mainWindow(JFrame):
  def __init__(self):
    super(mainWindow, self).__init__()
    self.initComponents()
    self.refreshPosts()
    
  def initComponents(self):
    self.bgPanel = JPanel(mousePressed = self.bgPanelMousePressed,
                          mouseDragged = self.bgPanelMouseDragged)
    self.exitButton = JLabel(mouseClicked = self.exitButtonMouseClicked)
    self.jScrollPane2 = JScrollPane()
    self.postTable = JTable()
    self.commentsButton = JLabel(mouseEntered = self.commentsButtonMouseEntered,
                                 mouseExited = self.commentsButtonMouseExited,
                                 mouseClicked = self.commentsButtonMouseClicked)
    self.openButton = JLabel(mouseEntered = self.openButtonMouseEntered,
                             mouseExited = self.openButtonMouseExited,
                             mouseClicked = self.openButtonMouseClicked)
    self.refreshButton = JLabel(mouseEntered = self.refreshButtonMouseEntered,
                                mouseExited = self.refreshButtonMouseExited,
                                mouseClicked = self.refreshButtonMouseClicked)
    self.timeLabel = JLabel()
    self.subButton = JLabel(mouseEntered = self.subButtonMouseEntered,
                            mouseExited = self.subButtonMouseExited,
                            mouseClicked = self.subButtonMouseClicked)

    self.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    self.setUndecorated(True)
    
    self.bgPanel.setBackground(Color(47, 103, 149))

    self.exitButton.setText("X")
    self.exitButton.setCursor(Cursor(Cursor.HAND_CURSOR))

    self.postTable.setAutoCreateRowSorter(True)
    self.postTable.setModel(dtm())
    
    self.postTable.getColumnModel().getColumn(0).setPreferredWidth(600)
    self.postTable.getColumnModel().getColumn(1).setPreferredWidth(40)
    
    self.jScrollPane2.setViewportView(self.postTable)

    self.openButton.setBackground(Color(76, 174, 255))
    self.openButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.openButton.setText("Open Post")
    self.openButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.openButton.setOpaque(True)

    self.commentsButton.setBackground(Color(76, 174, 255))
    self.commentsButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.commentsButton.setText("Open Comments")
    self.commentsButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.commentsButton.setOpaque(True)

    self.refreshButton.setBackground(Color(76, 174, 255))
    self.refreshButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.refreshButton.setText("Refresh")
    self.refreshButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.refreshButton.setOpaque(True)
    
    self.subButton.setBackground(Color(76, 174, 255))
    self.subButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.subButton.setText("Open Sub Posts")
    self.subButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.subButton.setOpaque(True)

    bgPanelLayout = GroupLayout(self.bgPanel)
    self.bgPanel.setLayout(bgPanelLayout)
    bgPanelLayout.setHorizontalGroup(
      bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addGroup(bgPanelLayout.createSequentialGroup()
        .addContainerGap()
        .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addGap(0, 0, sys.maxint)
            .addComponent(self.exitButton))
          .addComponent(self.jScrollPane2, GroupLayout.DEFAULT_SIZE, 785, sys.maxint)
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING, False)
              .addComponent(self.subButton, GroupLayout.Alignment.LEADING, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
              .addComponent(self.openButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
              .addComponent(self.commentsButton, GroupLayout.DEFAULT_SIZE, 214, sys.maxint))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, sys.maxint)
            .addComponent(self.refreshButton, GroupLayout.PREFERRED_SIZE, 214, GroupLayout.PREFERRED_SIZE))
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addComponent(self.timeLabel, GroupLayout.PREFERRED_SIZE, 295, GroupLayout.PREFERRED_SIZE)
            .addGap(0, 0, sys.maxint)))
        .addContainerGap()))
    
    bgPanelLayout.setVerticalGroup(
      bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addGroup(bgPanelLayout.createSequentialGroup()
        .addContainerGap()
        .addComponent(self.exitButton)
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addComponent(self.jScrollPane2, GroupLayout.DEFAULT_SIZE, 288, sys.maxint)
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
          .addComponent(self.openButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE)
          .addComponent(self.refreshButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE))
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addComponent(self.commentsButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE)
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addComponent(self.subButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE)
        .addGap(22, 22, 22)
        .addComponent(self.timeLabel, GroupLayout.PREFERRED_SIZE, 27, GroupLayout.PREFERRED_SIZE)
        .addContainerGap()))

    layout = GroupLayout(self.getContentPane())
    self.getContentPane().setLayout(layout)
    layout.setHorizontalGroup(
      layout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addComponent(self.bgPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint))
    
    layout.setVerticalGroup(
      layout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addComponent(self.bgPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint))

    self.pack()
    self.setLocationRelativeTo(None)
    
  def exitButtonMouseClicked(self, evt):
    sys.exit()
  
  def commentsButtonMouseEntered(self, evt):
    self.commentsButton.setBorder(border.LineBorder(Color.black))
    
  def commentsButtonMouseExited(self, evt):
    self.commentsButton.setBorder(None)
    
  def commentsButtonMouseClicked(self, evt):
    pid = self.postTable.getValueAt(self.postTable.getSelectedRow(), 2)
    selectedPost = self.findPost(pid)
    
    sourceSub = selectedPost.subCode
    webbrowser.open("https://www.reddit.com/r/" + sourceSub + "/comments/" + pid)
    
  def openButtonMouseEntered(self, evt):
    self.openButton.setBorder(border.LineBorder(Color.black))
    
  def openButtonMouseExited(self, evt):
    self.openButton.setBorder(None)
    
  def refreshButtonMouseEntered(self, evt):
    self.refreshButton.setBorder(border.LineBorder(Color.black))
    
  def refreshButtonMouseExited(self, evt):
    self.refreshButton.setBorder(None)
    
  def subButtonMouseEntered(self, evt):
    self.subButton.setBorder(border.LineBorder(Color.black))
    
  def subButtonMouseExited(self, evt):
    self.subButton.setBorder(None)
    
  def refreshButtonMouseClicked(self, evt):
    self.refreshPosts()
    
  def subButtonMouseClicked(self, evt):
    h = self.postTable.getValueAt(self.postTable.getSelectedRow(), 1)
    print("Collecting posts...")
    subprocess.call("python3 subPosts.py " + h, shell = True)
    print("Done!")
    
    with open("hotPosts.csv", "r") as f:
      reader = csv.reader(f)
      lis = list(reader)

    del postList[:]

    for i in lis:
      postList.append(post(i[0],
                           i[1],
                           i[2],
                           i[3],
                           i[4],
                           i[5]))

    self.postTable.getModel().setRowCount(0)

    for idx, x in enumerate(postList):
      dt = datetime.utcfromtimestamp(float(x.timePosted))
      postTime = x.title + " (" + self.pretty_date(dt) + ")"
      self.postTable.getModel().addRow([postTime, x.sub, x.postID])
      
  def bgPanelMouseDragged(self, evt):
    x = evt.getXOnScreen()
    y = evt.getYOnScreen()

    self.setLocation(x - mouseLoc[0], y - mouseLoc[1])
      
  def bgPanelMousePressed(self, evt):
    del mouseLoc[:]
    mouseLoc.append(evt.getX())
    mouseLoc.append(evt.getY())
    
  def openButtonMouseClicked(self, evt):
    pid = self.postTable.getValueAt(self.postTable.getSelectedRow(), 2)
    postLink = self.findPost(pid).link
    webbrowser.open(postLink)
    
  def refreshPosts(self):
    print("Collecting posts...")
    subprocess.call("python3 getPosts.py", shell = True)
    print("Done!")

    with open("hotPosts.csv", "r") as f:
      reader = csv.reader(f)
      lis = list(reader)

    del postList[:]

    for i in lis:
      postList.append(post(i[0],
                           i[1],
                           i[2],
                           i[3],
                           i[4],
                           i[5]))

    self.postTable.getModel().setRowCount(0)

    for idx, x in enumerate(postList):
      dt = datetime.utcfromtimestamp(float(x.timePosted))
      postTime = x.title + " (" + self.pretty_date(dt) + ")"
      self.postTable.getModel().addRow([postTime, x.sub, x.postID])
      
    self.timeLabel.setText("Last Refreshed: " + SimpleDateFormat("hh:mm a z").format(Calendar.getInstance().getTime()))
    
  def findPost(self, idPost):
    for n in postList:
      if n.postID == idPost:
        return n
    
  def pretty_date(self, time=False):
    now = datetime.utcnow()
    if type(time) is int:
      diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
      diff = now - time
    elif not time:
      diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
      return ""

    if day_diff == 0:
      if second_diff < 10:
        return "just now"
      if second_diff < 60:
        return str(second_diff) + " seconds ago"
      if second_diff < 120:
        return "a minute ago"
      if second_diff < 3600:
        return str(second_diff / 60) + " minutes ago"
      if second_diff < 7200:
        return "an hour ago"
      if second_diff < 86400:
        return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
      return "Yesterday"
    if day_diff < 7:
      return str(day_diff) + " days ago"
    if day_diff < 31:
      return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
      return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"
    
if __name__ == "__main__":
  mainWindow().setVisible(True)