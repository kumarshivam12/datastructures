class Employee(object):
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):#Can be thought as a Constructor/Initializers
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
    def fullname(self):
        return "{}{}".format(self.first,self.last)  
        

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)



class Dev(Employee):
    def __init__(self,first,last,pay,gf):
        super().__init__(first,last,pay)
        self.gf=gf
    
dev_1=Dev('shivam','kumar',2700000,1)
dev_2=Dev('sanhita','saha',270000,1)
dev_3=Dev('shubham','kumar',27000,1)

class Manager(Employee):
    def __init__(self, first, last, pay, employee=None):
        super().__init__(first,last,pay)
        if employee is None:
            self.employee=[]
        else:
            self.employee=employee
    
    def add_emp(self,emp):
        if emp not in self.employee:
            self.employee.append(emp)
            
                
    def rem_emp(self,emp):
        if emp in self.employee:
            self.employee.remove(emp)
            
    def prnt(self):
        for emp in self.employee:
            print('---->',emp.fullname())
            
man_1=Manager('shivam','kumar',27000000,[dev_3])
man_1.add_emp(dev_1)
man_1.add_emp(dev_2)

print(man_1.prnt())


