class Student:

    school = 'Nepal'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # instance methods

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value

    # class method
    # annotations are called decorator in python

    @classmethod
    def getSchoolName(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class.. in abc module")


s1 = Student(34, 67, 32)
s2 = Student(32, 11, 12)

print(s1.avg())

print(Student.getSchoolName())

Student.info()