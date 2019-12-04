class School:
    
    def __init__(self, name=None, roster = {}):
        self.name = name
        self.roster = roster
        
    def add_student(self, name, grade):
        grade_list = self.roster.get(grade, [])
        grade_list.append(name)
        self.roster[grade] = grade_list
        
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        sorted_roster = self.roster
        for key in sorted_roster:
            sorted_roster[key].sort()
        return sorted_roster