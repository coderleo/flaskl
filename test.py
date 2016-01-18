#coding='utf-8'
class people:
    names = ['jack','leo']      
    age = 1
    def printName(self):
    	self.names.append('wy')
    	self.age = 2
        print self.names,self.age
p = people()
#p.age=2
print people.age
#print people.names
print p.age
#####