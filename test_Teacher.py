import pytest

from Employee import Employee 
from Teacher import Teacher

class TestTeacher:
    emp_2 = Teacher('Jane', 'Doe', 10, 192)

    def test_TeacherAssertionError(self):
        with pytest.raises(AssertionError):
            emp_3 = Teacher('Jane', 'Doe', 10, 0)

    def test_set_teaching_hours(self):
        with pytest.raises(ValueError):
            self.emp_2.set_teaching_hours(-10)