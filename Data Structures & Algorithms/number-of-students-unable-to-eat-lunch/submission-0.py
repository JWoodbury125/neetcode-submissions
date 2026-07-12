class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        students = deque(students)

        rotations = 0
        sandwich_idx = 0

        while students and rotations < len(students):
            student = students.popleft()

            if student == sandwiches[sandwich_idx]:
                sandwich_idx += 1
                rotations = 0
            else:
                students.append(student)
                rotations += 1

        return len(students)