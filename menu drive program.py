print("1. Calculate area of square")
print("2. Calculate area of rectangle ")
choice= int(input(" Enter your choice (1 or 2):"))
if(choice==1):
             side=float(input("Enter side of a square :"))
             area_square=side*side
             print("Area of square is:",area_square)
else:
                length=float(input(" Enter length of a rectangle:"))
                breadth=float(input("Enter breadth of a rectangle:"))
                area_rectangle=length*breadth
                print("Area of a rectangle is :", area_rectangle)