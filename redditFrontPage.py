from javax.swing import *
from java.awt import *
import sys
import csv
import webbrowser

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
    self.jScrollPane1 = JScrollPane()
    self.postTable = JTable()
    self.saveButton = JLabel(mouseEntered = self.saveButtonMouseEntered,
                             mouseExited = self.saveButtonMouseExited
                            )
    self.openButton = JLabel(mouseEntered = self.openButtonMouseEntered,
                             mouseExited = self.openButtonMouseExited,
                             mouseClicked = self.openButtonMouseClicked
                            )
    self.unSaveButton = JLabel(mouseEntered = self.unSaveButtonMouseEntered,
                             mouseExited = self.unSaveButtonMouseExited
                            )
    self.refreshButton = JLabel(mouseEntered = self.refreshButtonMouseEntered,
                                mouseExited = self.refreshButtonMouseExited
                               )

    self.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
    self.setUndecorated(True)

    self.exitButton.setText("X")
    self.exitButton.setCursor(Cursor(Cursor.HAND_CURSOR))

    self.postTable.setModel(table.DefaultTableModel(
      [],
      ["Post Title", "Sub", "URL", "ID"]
    ))
    
    self.postTable.getColumnModel().getColumn(0).setPreferredWidth(400)
    self.postTable.getColumnModel().getColumn(1).setPreferredWidth(75)
    self.postTable.getColumnModel().getColumn(2).setPreferredWidth(150)
    self.postTable.getColumnModel().getColumn(3).setPreferredWidth(50)
    
    self.jScrollPane1.setViewportView(self.postTable)

    self.saveButton.setBackground(Color(255, 255, 255))
    self.saveButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.saveButton.setText("Save Post")
    self.saveButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.saveButton.setOpaque(True)

    self.openButton.setBackground(Color(255, 255, 255))
    self.openButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.openButton.setText("Open Post")
    self.openButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.openButton.setOpaque(True)

    self.unSaveButton.setBackground(Color(255, 255, 255))
    self.unSaveButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.unSaveButton.setText("unSave Post")
    self.unSaveButton.setCursor(Cursor(Cursor.HAND_CURSOR))
    self.unSaveButton.setOpaque(True)

    self.refreshButton.setBackground(Color(255, 255, 255))
    self.refreshButton.setHorizontalAlignment(SwingConstants.CENTER)
    self.refreshButton.setText("Refresh Button")
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
          .addComponent(self.jScrollPane1, GroupLayout.DEFAULT_SIZE, 529, sys.maxint)
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addComponent(self.unSaveButton, GroupLayout.PREFERRED_SIZE, 133, GroupLayout.PREFERRED_SIZE)
            .addGap(0, 0, sys.maxint))
          .addGroup(bgPanelLayout.createSequentialGroup()
            .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.TRAILING)
              .addComponent(self.saveButton, GroupLayout.PREFERRED_SIZE, 133, GroupLayout.PREFERRED_SIZE)
              .addComponent(self.openButton, GroupLayout.PREFERRED_SIZE, 133, GroupLayout.PREFERRED_SIZE))
            .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED, GroupLayout.DEFAULT_SIZE, sys.maxint)
            .addComponent(self.refreshButton, GroupLayout.PREFERRED_SIZE, 133, GroupLayout.PREFERRED_SIZE)))
        .addContainerGap())
    )
    bgPanelLayout.setVerticalGroup(
      bgPanelLayout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addGroup(bgPanelLayout.createSequentialGroup()
        .addContainerGap()
        .addComponent(self.exitButton)
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addComponent(self.jScrollPane1, GroupLayout.PREFERRED_SIZE, 147, GroupLayout.PREFERRED_SIZE)
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addGroup(bgPanelLayout.createParallelGroup(GroupLayout.Alignment.BASELINE)
          .addComponent(self.openButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE)
          .addComponent(self.refreshButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE))
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addComponent(self.saveButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE)
        .addPreferredGap(LayoutStyle.ComponentPlacement.RELATED)
        .addComponent(self.unSaveButton, GroupLayout.PREFERRED_SIZE, 42, GroupLayout.PREFERRED_SIZE)
        .addContainerGap(20, sys.maxint))
    )

    layout = GroupLayout(self.getContentPane())
    self.getContentPane().setLayout(layout)
    layout.setHorizontalGroup(
      layout.createParallelGroup(GroupLayout.Alignment.LEADING)
      .addComponent(self.bgPanel, GroupLayout.Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, sys.maxint)
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
      self.postTable.getModel().addRow([i[0],
                                        i[1],
                                        i[2],
                                        i[3]
                                       ]
                                      )
    
  def exitButtonMouseClicked(self, evt):
    sys.exit()
  
  def saveButtonMouseEntered(self, evt):
    self.saveButton.setBorder(border.LineBorder(Color.black))
    
  def saveButtonMouseExited(self, evt):
    self.saveButton.setBorder(None)
    
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
      
  def bgPanelMouseDragged(self, evt):
    x = evt.getXOnScreen()
    y = evt.getYOnScreen()

    self.setLocation(x - mouseLoc[0], y - mouseLoc[1])
      
  def bgPanelMousePressed(self, evt):
    del mouseLoc[:]
    mouseLoc.append(evt.getX())
    mouseLoc.append(evt.getY())
    
  def openButtonMouseClicked(self, evt):
    postLink = str(self.postTable.getModel().getValueAt(self.postTable.getSelectedRow(), 2))
    webbrowser.open(postLink)
    
if __name__ == "__main__":
  mainWindow().setVisible(True)