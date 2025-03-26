
class Student:

    def __init__(self, name):
        self.name = name
        self.courses = []
        self.study_streak = 0


    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Succesffully enrolled in {course}")
        else:
            print(f"Error. Already enrolled in {course}")

    
    def study(self):
        self.study_streak += 1
        print(f"Study Streak: {self.study_streak}")


    def show_courses(self):
        if self.courses:
            pass
        else:
            print(f"No enrolled courses")


def main():
    pass

if __name__ == "__main__":
    main()
