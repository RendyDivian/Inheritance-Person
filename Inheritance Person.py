class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def to_string(self):
        return f"{self.name}({self.address})"


class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.courseGrade = {}
        self.totalGrade = 0
        self.numCourse = 0

    def tostring(self):
        return f'{Person.tostring(self)}'

    def addcoursegrade(self, course, grade):
        self.course = course
        self.grade = grade
        self.coursegrade.update({course: grade})
        self.numcourses = len(self.coursegrade)

    def printgrades(self):
        for i in self.course_grade:
            print(f'{i}: {self.coursegrade[i]}')

    def getavggrade(self):
        for i in self.coursegrade.values():
            self.total += i
        self.avggrade = self.total / len(self.coursegrade)
        return self.avggrade

    def getnumcourses(self):
        return self.numcourses


class Teacher(Person):
    def __init__(self, name, address):
        Person.__init__(self, name, address)
        self.courses = []
        self.numcourses = 0

    def tostring(self):
        return f'{Person.tostring(self)}'

    def addcourse(self, course):
        if course in self.courses:
            return False
        else:
            self.courses.append(course)
            self.numcourses = len(self.courses)
            return True

    def removecourse(self, course):
        if course not in self.courses:
            return False
        else:
            self.courses.remove(course)
            self.numcourses = len(self.courses)
            return True

    def getnumcourses(self):
        return self.numcourses

#Need to fix still doesn't work, yet
if __name__ == '__main__':
    student1 = Student("Bill","Jakarta")
    teacher1 = Teacher("Tom", "Jakarta")
    student1.addcoursegrade("Maths", 81)
    student1.addcoursegrade("English", 90)
    student1.addcoursegrade("Biology", 89)
    student1.addcoursegrade("Physics", 60)
    print(student1.getaveragegrades())
    print(student1.getnumcourses())
    teacher1.addcourses("Maths")
    teacher1.addcourses("English")
    teacher1.addcourses("Biology")
    teacher1.removecourse("Physics")


