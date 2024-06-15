import unittest
from main import Student

class TestStudent(unittest.TestCase):
    def test_walk(self):
        student = Student("John")  # Provide a name argument
        for _ in range(10):
            student.walk()
        self.assertEqual(student.distance, 500, f"Дистанции не равны {student.distance} != 500")

    def test_run(self):
        student = Student("Jane")  # Provide a name argument
        for _ in range(10):
            student.run()
        self.assertEqual(student.distance, 1000, f"Дистанции не равны {student.distance} != 1000")

    def test_competition(self):
        student1 = Student("Alice")  # Provide a name argument
        student2 = Student("Bob")  # Provide a name argument
        for _ in range(10):
            student1.run()
            student2.walk()
        self.assertGreater(student1.distance, student2.distance, f"{student1.name} должен преодолеть дистанцию больше, чем {student2.name}")

if __name__ == '__main__':
    unittest.main()