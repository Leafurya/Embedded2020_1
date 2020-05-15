from RectangleModule import *

class PatternCell:
	def __init__(self,center,w,h):
		self.val=0
		self.rect=Rect(center,w,h)
		self.clicked=False
		self.rect.ShowRect()
		

class ArrayPattern:
	def __init__(self,cellSize,clientW,clientH,col,row):
		self.pattern=list()
		self.cellSize=cellSize
		self.col=col
		self.row=row
		self.clientW=clientW
		self.clientH=clientH
		self.oldIndex=-1
		self.passVal=1
		for i in range(0,self.col*self.row):
			center=Point(((clientW//col)//2)+((clientW//col)*(i%col)),((clientH//row)//2)+((clientH//row)*(i//row)))
			tCell=PatternCell(center,cellSize,cellSize)
			self.pattern.append(tCell)

	def InputPattern(self,mPos):
		index=(int)((mPos.x//(self.clientW/self.col))+(mPos.y//(self.clientH/self.row)*self.col))
		if(self.pattern[index].rect.PointInRect(mPos)):
			if (self.oldIndex!=index):
				print(index,"cell")
				self.pattern[index].val+=self.passVal
				self.oldIndex=index
				self.passVal+=1

	def ComparePattern(self,nPattern):
		for i in range(0,self.col*self.row):
			if(self.pattern[i].val!=nPattern.pattern[i].val):
				return False
		return True

	def ShowPattern(self):
		for i in range(0,self.col*self.row):
			print(self.pattern[i].val,end=' ')

	def SavePatternToFile(self,fileName):
		patternVals=str()
		for i in range(0,9):
			patternVals="%s %d"%(patternVals,self.pattern[i].val)
		patternVals="%s\n"%patternVals
		print(patternVals)
		file=open(fileName,'a')
		file.write(patternVals)
		file.close()

	def SetPattern(self,patternList):
		for i in range(0,self.col*self.row):
			self.pattern[i].val=patternList[i]