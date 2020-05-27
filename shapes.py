class rectangle():
	def init(self):
		self.length = a
		self.breadth = b
	def set__landb(self,c,d):
		self.length = c
		self.breadth = d
	def get__landb(self):
		print("Length and Breadth of rectangle is " +str(self.length)+ " and " +str(self.breadth)+ " respectively") 
	def area(self):
		z = self.length * self.breadth
		print("Area of rectangle is " +str(z))
	def perimeter(self):
		z = 2 * (self.length + self.breadth)
		print("Perimeter of rectangle is " +str(z))		
	def diagonal(self):
		z = ((self.length * self.length) + (self.breadth * self.breadth)) ** 0.5
		print("Diagonal of rectangle is " +str(z))				
print("1) Rectangle")
c = rectangle()
c.set__landb(8,6)
c.get__landb()
c.area()
c.perimeter()
c.diagonal()
print("*****************************************************************")
class square():
	def init(self):
		self.side = a
	def set__side(self,c):
		self.side = c
	def get__side(self):
		print("Side of square is " +str(self.side))
	def area(self):
		z = self.side * self.side
		print("Area of square is " +str(z))
	def perimeter(self):
		z = 4 * self.side
		print("Perimeter of square is " +str(z))
	def diagonal(self):
		z = (2 ** 0.5) * self.side
		print("Diagonal of square is " +str(z))		
print("2) Square")
c = square()
c.set__side(8)
c.get__side()
c.area()
c.perimeter()
c.diagonal()
print("*****************************************************************")
class right_angled_triangle():
	def init(self):
		self.side1 = a
		self.side2 = b
	def set__sides(self,c,d):
		self.side1 = c
		self.side2 = d
	def get__sides(self):
		print("Two sides of triangle are " +str(self.side1)+ " and " +str(self.side2))
	def area(self):
		z = (1/2) * self.side1 * self.side2	
		print("Area of right angled triangle is " +str(z))
	def perimeter(self):
		z = self.side1 + self.side2 + (((self.side1 * self.side1) + (self.side2 * self.side2)) ** 0.5)
		print("Perimeter of right angled triangle is " +str(z))	
print("3) Right angled triangle")
c = right_angled_triangle()
c.set__sides(4,3)
c.get__sides()
c.area()
c.perimeter()
print("*****************************************************************")
class equilateral_triangle():
	def init(self):
		self.side = a
	def set_sides(self,b):
		self.side = b
	def get_sides(self):
		print("Side of triangle is " +str(self.side))
	def area(self):
		z = ((3 ** 0.5)/4) * (self.side * self.side)
		print("Area of equilateral triangle is " +str(z))		 
	def perimeter(self):
		z = 3 * self.side
		print("Perimeter of equilateral is " +str(z))
print("4) Equilateral triangle")
c = equilateral_triangle()
c.set_sides(6)
c.get_sides()
c.area()
c.perimeter()
print("*****************************************************************")
class regular_pentagon():
	def init(self):
		self.side = a
	def set_sides(self,b):
		self.side = b
	def get_sides(self):
		print("Side of pentagon is " +str(self.side))
	def area(self): 
		z = 1.7204 * (self.side * self.side)
		print("Area of regular pentagon is " +str(z))
	def perimeter(self):
		z = 5 * self.side
		print("Perimeter of regular polygon is " +str(z))
print("5) Regular Pentagon")
c = regular_pentagon()
c.set_sides(6)
c.get_sides()
c.area()
c.perimeter()
print("*****************************************************************")
class circle():
	def init(self):
		self.radius = a
	def set_radius(self,b):
		self.radius = b
	def get_radius(self):
		print("Radius of circle is " +str(self.radius))
	def area(self):
		import math
		z = math.pi * (self.radius * self.radius)
		print("Area of circle is " +str(z))
	def perimeter(self):
		import math
		z = math.pi * 2 * self.radius
		print("Perimeter of circle is " +str(z))
print("6) Circle")
c = circle()
c.set_radius(7)
c.get_radius()
c.area()
c.perimeter()
print("*****************************************************************")
class cylinder():
	def init(self):
		self.radius = a
		self.height = b
	def set_radius(self,c):
		self.radius = c
	def get_radius(self):
		print("Radius of cylinder is " +str(self.radius))
	def set_height(self,d):
		self.height = d
	def get_height(self):
		print("Height of cylinder is " +str(self.height))
	def surface_area(self):
		import math 
		z = math.pi * 2 * (self.radius * self.height) + (2 * math.pi * (self.radius * self.radius))
		print("Surface area of cylinder is " +str(z))
	def volume(self):
		import math
		z = math.pi * (self.radius * self.radius) * self.height
		print("Volume area of cylinder is " +str(z))
print("7) Cylinder")
c = cylinder()
c.set_radius(7)
c.get_radius()
c.set_height(10)
c.get_height()
c.surface_area()
c.volume()
print("*****************************************************************")
class cube():
	def init(self):
		self.side = a
	def set__side(self,c):
		self.side = c
	def get__side(self):
		print("Side of cube is " +str(self.side))
	def volume(self):
		z = self.side * self.side * self.side
		print("Volume of cube is " +str(z))
	def surface_area(self):
		z = 6 * self.side * self.side
		print("Surface area of cube is " +str(z))
	def diagonal(self):
		z = (3** 0.5) * self.side
		print("Diagonal of cube is " +str(z))		
print("8) Cube")
c = cube()
c.set__side(6)
c.get__side()
c.surface_area()
c.volume()
c.diagonal()
print("*****************************************************************")
class sphere():
	def init(self):
		self.radius = a
	def set_radius(self,b):
		self.radius = b
	def get_radius(self):
		print("Radius of sphere is " +str(self.radius))
	def surface_area(self):
		import math
		z = math.pi * 4 * (self.radius * self.radius)
		print("Surface area of sphere is " +str(z))
	def volume(self):
		import math
		z = math.pi * (4/3) * (pow(self.radius,3,10))
		print("Volume of sphere is " +str(z))
print("9) Sphere")
c = sphere()
c.set_radius(7)
c.get_radius()
c.surface_area()
c.volume()
print("*****************************************************************")
class parallelogram():
	def init(self):
		self.height = a
		self.length = c
		self.breadth = b
	def set__l_b_h(self,e,d,f):
		self.height = f
		self.breadth = d
		self.length = e
	def get__l_b_h(self):
		print("Length, Breadth and height of parallelogram is " +str(self.length)+ ", " +str(self.breadth)+ " and " +str(self.height)+ " respectively") 
	def area(self):
		z = self.height * self.breadth
		print("Area of parallelogram is " +str(z))
	def perimeter(self):
		z = 2 * (self.length + self.breadth)
		print("Perimeter of parallelogram is " +str(z))						
print("10) Parallelogram")
c = parallelogram()
c.set__l_b_h(8,5,4)
c.get__l_b_h()
c.area()
c.perimeter()
print("*****************************************************************")
