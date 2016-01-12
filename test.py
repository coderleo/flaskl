#coding='utf-8'
class people:
    names = ['jack','leo']      
    age = 1
    def printName(self):
    	self.names.append('wy')
    	self.age = 2
        print self.names,self.age
people().printName()
print people.names
print people.age