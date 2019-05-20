class Grades (object):
    ''''''
    def __init__(self):
        self.grades = {}
        self.students = []
        self.isSorted = True

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('student already exists')
        self.students.append(student)
        self.grades[student.getIdNum()] = []# using student id to organise their grades
        self.isSorted = False
        
    def addGrade(self, grade):
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in GradeBook')

    def getGrade(self, student):
        try:
            return  self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student Not in grade book')
        
    def allStudent(self):
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
            
