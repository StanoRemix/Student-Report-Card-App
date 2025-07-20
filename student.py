class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.marks = subjects
        self.aver = self.calc_aver()
        self.grade = self.pin_grade()
    def calc_aver(self):
        grand_total = sum(self.marks.values())
        return grand_total / len(self.marks) if self.marks else 0
    def pin_grade(self):
        if self.aver >= 70:
            return 'A'
        elif self.aver >= 60:
            return 'B'
        elif self.aver >= 50:
            return 'C'
        elif self.aver >= 40:
            return 'D'
        else:
            return 'F' 
    def to_rec(self):
        return {
            'name': self.name,
            'marks': self.marks,
            'average': self.aver,
            'grade': self.grade
        }