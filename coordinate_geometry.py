x1=int(input('enter x1'))
y1=int(input('enter y1'))
x2=int(input('enter x2'))
y2=int(input('enter y2'))

x_sq = (x2-x1) ** 2
y_sq = (y2-y1) ** 2

distance = (x_sq + y_sq) ** 0.5

print("distance : "+str(distance))
