class Rect:
	def __init__(self,center,w,h):
		self.left=center.x-(w/2)
		self.top=center.y-(h/2)
		self.right=center.x+(w/2)
		self.bottom=center.y+(h/2)

	def PointInRect(self,point):
		if ((self.left<point.x<self.right)and(self.top<point.y<self.bottom)):
			return True
		else:
			return False

	def ShowRect(self):
		print("[",self.left,self.top,self.right,self.bottom,"]")


class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y