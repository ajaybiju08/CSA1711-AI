% FACTS: student(StudentName, SubjectCode)
student(ram, cs101).
student(shyam, ma102).
student(gita, cs101).
student(anil, ph103).

% FACTS: teacher(TeacherName, SubjectCode)
teacher(prof_sharma, cs101).
teacher(dr_verma, ma102).
teacher(prof_das, ph103).

% RULE: Find the teacher of a specific student
% A Teacher teaches a Student if they both share the same SubCode.
teaches(Teacher, Student) :-
    teacher(Teacher, SubCode),
    student(Student, SubCode).