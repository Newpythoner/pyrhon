class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getcoordinate (self):
        point = (self.x,self.y)
        print ('定义坐标位置:',point)
        return point

class Line:
    def __init__(self,pointA,pointB):
        self.pointA = pointA
        self.pointB = pointB
        
    def getlang (self):
        if self.pointA[0] > 0 and self.pointB[0] <0:
            lang = self.pointA[0] + abs(self.pointB[0])
        elif self.pointA[0] < 0 and self.pointB[0] > 0:
            lang = abs(self.pointA[0]) + self.pointB[0]
        else:
            lang = max(abs(self.pointA[0]),abs(self.pointB[0])) -min(abs(self.pointA[0]),abs(self.pointB[0]))
        return lang

    def getwide (self):
        if self.pointA[1] > 0 and self.pointB[1] <0:
            lang = self.pointA[1] + abs(self.pointB[1])
        elif self.pointA[1] < 0 and self.pointB[1] > 0:
            lang = abs(self.pointA[1]) + self.pointB[1]
        else:
            lang = max(abs(self.pointA[1]),abs(self.pointB[1])) -min(abs(self.pointA[1]),abs(self.pointB[1]))
        return lang

x1 = int (input ('第一个点X坐标:'))
y1 = int (input ('第一个点Y坐标:'))
x2 = int (input ('第二个点X坐标:'))
y2 = int (input ('第二个点Y坐标:'))
p1 = Point(x1,y1)
p2 = Point(x2,y2)

l = Line(p1.getcoordinate(),p2.getcoordinate())
linelang = (l.getlang()**2 + l.getwide()**2)**0.5
print ('两点之间的直线长度是:%.4f(默认保留四位小数)'%linelang)
