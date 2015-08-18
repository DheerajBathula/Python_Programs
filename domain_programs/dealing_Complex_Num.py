from math import sqrt

class Complex:
    def __init__(self,real=0,im=0):
        self.r=real
        self.i=im

    def cprint(self):
        if self.i==0:
            print "%.2f" %self.r
        elif self.r==0:
            print str("%.2f" % self.i) + "i"
        elif self.i<0:
            s1=str("%.2f" %self.r)
            s2=str("%.2f" % abs(self.i))
            print s1 + " - " + s2 + "i"
        elif self.i>0:
            s1=str("%.2f" %self.r)
            s2=str("%.2f" % self.i)
            print s1 + " + " + s2 + "i"


    def __add__(self,c):
        res=Complex()
        res.r=self.r+c.r
        res.i=self.i+c.i
        return res

    def __sub__(self,c):
        res=Complex()
        res.r=self.r-c.r
        res.i=self.i-c.i
        return res 

    def __mul__(self,c):
        res=Complex()
        res.r=self.r*c.r-self.i*c.i
        res.i=self.r*c.i+self.i*c.r
        return res   

    def __div__(self,c):
        res=Complex()
        res.r=(self.r*c.r+self.i*c.i)/(c.r**2+c.i**2)
        res.i=(self.i*c.r-self.r*c.i)/(c.r**2+c.i**2)
        return res

    def __abs__(self):
        res= "%.2f" % sqrt(self.r**2+self.i**2)
        return res

a,b=raw_input().split()
a,b=float(a),float(b)
c1=Complex(a,b)
a,b=raw_input().split()
a,b=float(a),float(b)
c2=Complex(a,b)

c3=c1+c2
c3.cprint()
c3=c1-c2
c3.cprint()
c3=c1*c2
c3.cprint()
c3=c1/c2
c3.cprint()
c3=abs(c1)
print c3
c3=abs(c2)
print c3
