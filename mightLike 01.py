from graphics import*

#setting window size
shapesWin = GraphWin ("shapes", 700, 700)
shapesWin.setCoords (0,0,500,500)

winX = 500
winY = 500

#fuction for rectangle
def draw_Rec(rX, rY, size, color, win):
    rectangle = Rectangle(rX, rY)
    rectangle.setFill(color)
    rectangle.draw(win)

def continueButton(rX, rY, text, txSize, txCol, style, win):
    #nextRec = Rectangle(Point(rX , rY), Point(rX, rY))
    #nextRec.setFill(rCol)
    #nextRec.draw(win)

    nextTex = Text(Point(rX, rY), text)
    nextTex.setSize(txSize)
    nextTex.setStyle(style)
    nextTex.setTextColor(txCol)
    nextTex.draw(win)
    
rX = 400
rY = 30
text = "Continue"
txSize = 15
rCol = color_rgb(0, 255, 0)
txCol = "black"
style = "bold"

#Rec1
draw_Rec(Point(0,450), Point(500,500), 50, "white", shapesWin)

message = Text(Point (100, 475) , "What is the title of your favorite song?")
message.draw(shapesWin)

inputBox = Entry(Point(400,475), 20)
inputStr = inputBox.getText()
inputBox.setTextColor("Black")
inputBox.draw(shapesWin)

#Rec2
draw_Rec(Point(0,400), Point(500,350), 50, "white", shapesWin)


message = Text(Point (100, 375) , "Who is the creator of your song?")
message.draw(shapesWin)

inputBox = Entry(Point(400,375), 20)
inputStr = inputBox.getText()
inputBox.setTextColor("Black")
inputBox.draw(shapesWin)

#Rec3
draw_Rec(Point(0,300), Point(500,250), 50, "white", shapesWin)

message = Text(Point (100, 275) , "Who is the performer on the song?")
message.draw(shapesWin)

inputBox = Entry(Point(400,275), 20)
inputStr = inputBox.getText()
inputBox.setTextColor("gray")
inputBox.draw(shapesWin)

#Rec4
draw_Rec(Point(0,200), Point(500,150), 50, "white", shapesWin)

message = Text(Point (100, 175) , "In what language is the song in?")
message.draw(shapesWin)


inputBox = Entry(Point(400,175), 20)
inputStr = inputBox.getText()
inputBox.setTextColor("Black")
inputBox.draw(shapesWin)

#Rec5
draw_Rec(Point(0,100), Point(500,50), 50, "white", shapesWin)

message = Text(Point (100, 75) , "In what language is the song in?")
message.draw(shapesWin)

inputBox = Entry(Point(400,75), 20)
inputStr = inputBox.getText()
inputBox.setTextColor("Black")
inputBox.draw(shapesWin)

# continue button
continueButton(rX, rY, text, txSize, txCol, style, shapesWin)
#window
shapesWin.getMouse()
shapesWin.close()

#Input1
#inputBox = Entry(Point(400,475), 20)
#inputStr = inputBox.getText()
#inputBox.setText("32.0")
#inputBox.setFace("courier")
#inputBox.setSize(25)
#inputBox.setStyle("italic")
#inputBox.setTextColor("Black")
#inputBox.setFill("white")
#inputBox.draw(shapesWin)
