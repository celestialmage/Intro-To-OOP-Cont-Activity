from school_schedule.student import Student

# Write your tests here!

def test_new_student_init():

    name = "Eric"
    grade = "A"
    classes = ["Math", "Art"]

    student = Student(name=name, grade=grade, classes=classes)

    assert student.name == name
    assert student.grade == grade
    assert len(student.classes) == len(classes)
    assert student.classes == classes

def test_add_classes():

    name = "Matthew"
    grade = "B"
    classes = ["Music", "Art"]

    new_class = "Football"

    student = Student(name=name, grade=grade, classes=classes)

    updated_classes = student.add_class(new_class)

    assert len(student.classes) == 3
    assert new_class in updated_classes
    assert new_class in student.classes

def test_add_classes_non_string_returns_false():

    name = "Samantha"
    grade = "C"
    classes = ["Music", "Wrestling"]

    new_class = 2

    student = Student(name=name, grade=grade, classes=classes)

    results = student.add_class(new_class)

    assert results == False