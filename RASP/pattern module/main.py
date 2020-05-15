from ArrayPatternModule import *
from RectangleModule import *
from tkinter import *
"""import numpy as np
import cv2 as cv"""

def LoadPatternFromFile(pattern,fileName):
	file=open(fileName,'r')
	lines=file.readlines()
	for line in lines:
		print(line.split())
		ptli=[int(i) for i in line.split()]
		pattern.SetPattern(ptli)
	file.close()

def MouseMove(event):
	mPos=Point(event.x,event.y)
	if (inputMode=="create_pattern"):
		pattern1.InputPattern(mPos)
	elif (inputMode=="get_pattern"):
		pattern2.InputPattern(mPos)

def MouseRelease(event):
	global pattern2
	if (inputMode=="get_pattern"):
		if(pattern1.ComparePattern(pattern2)):
			print("success")
		else:
			print("fail")
		print("create pattern",pattern2.ShowPattern())
		
		pattern2=ArrayPattern(cellSize,clientW,clientH,col,row)
	elif (inputMode=="create_pattern"):
		pattern1.SavePatternToFile("patterns.txt")
		print("create pattern",pattern1.ShowPattern())

def ChangeInputMode():
	global inputMode
	global pattern1
	global pattern2
	if (inputMode=="create_pattern"):
		pattern2=ArrayPattern(cellSize,clientW,clientH,col,row)
		inputMode="get_pattern"
	elif (inputMode=="get_pattern"):
		pattern1=ArrayPattern(cellSize,clientW,clientH,col,row)
		inputMode="create_pattern"
	print(inputMode)

root=Tk()
clientW=500
clientH=500
cellSize=100
col=3
row=3
inputMode="create_pattern"

pattern1=ArrayPattern(cellSize,clientW,clientH,col,row)
pattern2=ArrayPattern(cellSize,clientW,clientH,col,row)

LoadPatternFromFile(pattern1,"patterns.txt")
pattern1.ShowPattern()

#img=np.zeros((clientW,clientH,3),np.uint8)

"""for i in range(0,9):
	tu1=tuple([int(pattern1.pattern[i].rect.left),int(pattern1.pattern[i].rect.top)])
	tu2=tuple([int(pattern1.pattern[i].rect.right),int(pattern1.pattern[i].rect.bottom)])
	img=cv.rectangle(img,tu1,tu2,(255,0,0),3)
	
cv.imshow('img',img)"""

frame=Frame(root,width=clientW,height=clientH)
frame.bind("<B1-Motion>",MouseMove)
frame.bind("<ButtonRelease-1>",MouseRelease)
setPatternBtn=Button(root,text='set pattern',command=ChangeInputMode)
setPatternBtn.pack()
frame.pack()

root.mainloop()