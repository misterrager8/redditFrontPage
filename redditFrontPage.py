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

mouseLoc = []
postList = []

class mainWindow(JFrame):
  def __init__(self):
    super(mainWindow, self).__init__()
    self.initComponents()
    
  def initComponents(self):
    self.bgPanel = JPanel(mousePressed = self.bgPanelMousePressed,
                          mouseDragged = self.bgPanelMouseDragged
                         )
    self.exitButton = JLabel(mouseClicked = self.exitButtonMouseClicked)
    self.jScrollPane2 = JScrollPane()
    self.postTable = JTable()
    self.commentsButton = JLabel(mouseEntered = self.commentsButtonMouseEntered,
                                 mouseExited = self.commentsButtonMouseExited,
                                 mouseClicked = self.commentsButtonMouseClicked
                                )
    self.openButton = JLabel(mouseEntered = self.openButtonMouseEntered,
                             mouseExited = self.openButtonMouseExited,
                             mouseClicked = self.openButtonMouseClicked
                            )
    self.unSaveButton = JLabel(mouseEntered = self.unSaveButtonMouseEntered,
                               mouseExited = self.unSaveButtonMouseExited
                            )
    self.refreshButton = JLabel(mouseEntered = self.refreshButtonMouseEntered,
                                mouseExited = self.refreshButtonMouseExited,
                                mouseClicked = self.refreshButtonMouseClicked
                               )
    self.timeLabel = JLabel()

    self.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    self.setUndecorated(True)
    
    self.bgPanel.setBackground(Color(47, 103, 149))

    self.exitButton.setText("X")
    self.exitButton.setCursor(Cursor(Cursor.HAND_CURSOR))

    self.postTable.setModel(table.DefaultTableModel(
      [],
      ["Post Title", "Sub"]
    ))
    
    self.postTable.getColumnModel().getColumn(0).setPreferredWidth(550)
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
              .addComponent(self.openButton, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
              .addComponent(self.commentsButton, GroupLayout.DEFAULT_SIZE, 214, sys.maxint))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, sys.maxint)
            .addComponent(self.refreshButton, GroupLayout.PREFERRED_SIZE, 214, GroupLayout.PREFERRED_SIZE))
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addComponent(self.timeLabel, GroupLayout.PREFERRED_SIZE, 295, GroupLayout.PREFERRED_SIZE)
            .addGap(0, 0, sys.maxint)))
        .addContainerGap())
    )
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
        .addGap(70, 70, 70)
        .addComponent(self.timeLabel, GroupLayout.PREFERRED_SIZE, 27, GroupLayout.PREFERRED_SIZE)
        .addContainerGap())
    )

    layout = GroupLayout(self.getContentPane())
    self.getContentPane().setLayout(layout)
    layout.setHorizontalGroup(
      layout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addComponent(self.bgPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
    )
    layout.setVerticalGroup(
      layout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addComponent(self.bgPanel, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
    )

    self.pack()
    self.setLocationRelativeTo(None)
    
    with open("hotPosts.csv", "r") as f:
      reader = csv.reader(f)
      lis = list(reader)
      
    for i in lis:
      postList.append(post(i[0],
                           i[1],
                           i[2],
                           i[3],
                           i[4],
                           i[5]
                          ))
      
    for x in postList:
      parsed_date = datetime.utcfromtimestamp(float(x.timePosted))
      b = parsed_date.strftime("%I:%M %p")
      self.postTable.getModel().addRow([x.title + " - " + b, x.sub])
      
    self.timeLabel.setText("Last Refreshed: " + SimpleDateFormat("hh:mm a z").format(Calendar.getInstance().getTime()))
    
  def exitButtonMouseClicked(self, evt):
    sys.exit()
  
  def commentsButtonMouseEntered(self, evt):
    self.commentsButton.setBorder(border.LineBorder(Color.black))
    
  def commentsButtonMouseExited(self, evt):
    self.commentsButton.setBorder(None)
    
  def commentsButtonMouseClicked(self, evt):
    pid = postList[self.postTable.getSelectedRow()].postID
    sourceSub = postList[self.postTable.getSelectedRow()].subCode
    webbrowser.open("https://www.reddit.com/r/" + sourceSub + "/comments/" + pid)
    
  def openButtonMouseEntered(self, evt):
    self.openButton.setBorder(border.LineBorder(Color.black))
    
  def openButtonMouseExited(self, evt):
    self.openButton.setBorder(None)
    
  def unSaveButtonMouseEntered(self, evt):
    self.unSaveButton.setBorder(border.LineBorder(Color.black))
    
  def unSaveButtonMouseExited(self, evt):
    self.unSaveButton.setBorder(None)
    
  def refreshButtonMouseEntered(self, evt):
    self.refreshButton.setBorder(border.LineBorder(Color.black))
    
  def refreshButtonMouseExited(self, evt):
    self.refreshButton.setBorder(None)
    
  def refreshButtonMouseClicked(self, evt):
    subprocess.call("python3 getPosts.py", shell = True)

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
                           i[5]
                          ))

    self.postTable.getModel().setRowCount(0)

    for x in postList:
      b = parsed_date.strftime("%I:%M %p")
      self.postTable.getModel().addRow([x.title + " - " + b, x.sub])
      
    self.timeLabel.setText("Last Refreshed: " + SimpleDateFormat("hh:mm a").format(Calendar.getInstance().getTime()))
      
  def bgPanelMouseDragged(self, evt):
    x = evt.getXOnScreen()
    y = evt.getYOnScreen()

    self.setLocation(x - mouseLoc[0], y - mouseLoc[1])
      
  def bgPanelMousePressed(self, evt):
    del mouseLoc[:]
    mouseLoc.append(evt.getX())
    mouseLoc.append(evt.getY())
    
  def openButtonMouseClicked(self, evt):
    postLink = postList[self.postTable.getSelectedRow()].link
    webbrowser.open(postLink)
    
if __name__ == "__main__":
  print("Collecting posts...")
  subprocess.call("python3 getPosts.py", shell = True)
  print("Done!")
  
  mainWindow().setVisible(True)