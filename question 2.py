class Point:
  def __init__(self, _length = 0, _width = 0):
    self.length = _length
    self.width = _width

  def getWidth(self):
    return self.width
  
  def getLength(self):
    return self.length

  def __str__(self): #Print
        return "({0},{1})".format(self.length,self.width)

  #Operators
  def __add__(self, other):
      x = self.length + other.length
      y = self.width + other.width
      return Point(x, y)
  
  def __sub__(self, other):
      x = self.length - other.length
      y = self.width - other.width
      return Point(x, y)

  def __mul__(self, other):
      x = self.length * other.length
      y = self.width * other.width
      return Point(x, y)

  def __truediv__(self, other):
      x = self.length / other.length
      y = self.width / other.width
      return Point(x, y)

  def __floordiv__(self, other):
      x = self.length // other.length
      y = self.width // other.width
      return Point(x, y)

  def __mod__(self, other):
      x = self.length % other.length
      y = self.width % other.width
      return Point(x, y)
  
  #Comparison Operators
  def __lt__(self, other):
      self_mag = (self.length ** 2) + (self.width ** 2)
      other_mag = (other.length ** 2) + (other.width ** 2)
      return self_mag < other_mag

  def __le__(self, other):
      self_mag = (self.length ** 2) + (self.width ** 2)
      other_mag = (other.length ** 2) + (other.width ** 2)
      return self_mag <= other_mag
  
  def __eq__(self, other):
      self_mag = (self.length ** 2) + (self.width ** 2)
      other_mag = (other.length ** 2) + (other.width ** 2)
      return self_mag == other_mag
  
  def __ne__(self, other):
      self_mag = (self.length ** 2) + (self.width ** 2)
      other_mag = (other.length ** 2) + (other.width ** 2)
      return self_mag != other_mag
  
  def __gt__(self, other):
      self_mag = (self.length ** 2) + (self.width ** 2)
      other_mag = (other.length ** 2) + (other.width ** 2)
      return self_mag > other_mag
  
  def __ge__(self, other):
      self_mag = (self.length ** 2) + (self.width ** 2)
      other_mag = (other.length ** 2) + (other.width ** 2)
      return self_mag >= other_mag

if __name__ == "__main__":
    x = Point(4 , 4)
    y = Point(4 , 4)

    if x > y :  
      print (x + y)
    elif x == y:
      print (x - y)
    else:
      print(x / y)

