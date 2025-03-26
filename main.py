
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
            for i, course in enumerate(self.courses):
                print(f"{i + 1}) {course}")
        else:
            print(f"No enrolled courses")



class Quiz:
    def __init__(self):
        self.questions = {
            "Python": [
                ("What is the output of 2**3?", "8"),
                ("Which keyword is used to declare a function in Python?", "def"),
                ("What does len() return?", "length")
            ],
            "Math": [
                ("What is 10+5 ?", "15"),
                ("Solve this: 12/4", "3"),
                ("What is 7*6 ?", "42")
            ]
        }


    def take_quiz(self, course):
        if course not in self.questions:
            print(f"No quiz questions for {course}")
            return
        else:
            score = 0

            for question, answer in self.questions[course]:
                user_response = input(question + " ")
                if user_response.strip().lower() == answer.lower():
                    score += 1
                    print(f"Correct!!! your score is => {score}")
                else:
                    print(f"Incorrect. The correct answer is {answer}")
                    print(f"Score: {score}")

                print()
                
            print(f"{self.questions[course]} Quiz completed")
            print(f"Final Score: {score}")




class TutorApp:

    def __init__(self):
        self.student = None
        self.quiz = Quiz()


    def start_app(self):
        student_name = input("Enter your name: ")
        self.student = Student(student_name)

        self.menu()


    def menu(self):
        while True:
            print("\n1.Course Enrollment \n2.View Enrolled Courses \n3.Study Session \n4.Take Quiz \n5.Exit")

            user_input = input("Enter number to select => ")

            if user_input.strip() == "1":
                new_course = input("Enter Course name: ")
                self.student.add_course(new_course)

            elif user_input.strip() == "2":
                self.student.show_courses()

            elif user_input.strip() == "3":
                self.student.study()

            elif user_input.strip() == "4":
                course_quiz = input("Enter the course name for the quiz => ")
                self.quiz.take_quiz(course_quiz)

            elif user_input.strip() == "5":
                print("Closing Tutor App....")
                print("Goodbye!")
                break
            
            else:
                print("Invalid Input. Try Again")
                print()



if __name__ == "__main__":
    app = TutorApp()

    app.start_app()
