from graphics import*

#setting window size
shapesWin = GraphWin ("shapes", 700, 700)
shapesWin.setCoords (0,0,500,500)

winX = 500
winY = 500

#rectangle
#Rec1
pSq = Rectangle (Point(0, 450), Point(500,500))
pSq.setFill(color_rgb(250,250, 250))
pSq.draw(shapesWin)

#Input1
inputBox = Entry(Point(400,475), 20)
inputStr = inputBox.getText()
#inputBox.setText("32.0")
#inputBox.setFace("courier")
#inputBox.setSize(25)
#inputBox.setStyle("italic")
inputBox.setTextColor("Black")
#inputBox.setFill("white")
inputBox.draw(shapesWin)

#Rec2
pSq = Rectangle (Point(0, 400), Point(500,350))
pSq.setFill(color_rgb(250,250, 250))
pSq.draw(shapesWin)
#Rec3
pSq = Rectangle (Point(0, 300), Point(500,250))
pSq.setFill(color_rgb(250,250, 250))
pSq.draw(shapesWin)
#Rec4
pSq = Rectangle (Point(0, 200), Point(500,150))
pSq.setFill(color_rgb(250,250, 250))
pSq.draw(shapesWin)
#Rec5
pSq = Rectangle (Point(0, 100), Point(500,50))
pSq.setFill(color_rgb(250,250, 250))
pSq.draw(shapesWin)

#text
#Box1
message = Text(Point (100, 475) , "What is the title of your favorite song?")
message.draw(shapesWin)


#Box2
message = Text(Point (100, 375) , "Who is the creator of your song?")
message.draw(shapesWin)
#Box3
message = Text(Point (100, 275) , "Who is the performer on the song?")
message.draw(shapesWin)
#Box4
message = Text(Point (100, 175) , "In what language is the song in?")
message.draw(shapesWin)
#Box4
message = Text(Point (100, 75) , "In what language is the song in?")
message.draw(shapesWin)

#window
shapesWin.getMouse()
shapesWin.close()
