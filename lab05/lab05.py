'''Owen Ferguson Lab 05 2-7-24'''

from typing import Optional

class Student:

    def __init__(self, name: str,
                 interests: list[str]):
        self.name = name
        self.interests = interests
        self.freetimes = set([8, 9, 10, 11, 12, 13, 14, 15])
        self.meetings: list[int] = []

    def schedule_meeting(self, time: int):
        if time in self.freetimes:
            self.meetings.append(time)
            self.freetimes.remove(time)
    
class Club:

    def __init__(self, name: str):
        self.name = name
        self.members: list[Student] = []
        self.meeting_time: Optional[int] = None

    def join(self, student: Student):
        self.members.append(student)

    def find_common_time(self) -> int:
        common_times = self.members[0].freetimes
        for member in self.members:
            for time in common_times:
                if time not in member.freetimes:
                    common_times.remove(time)
        if len(common_times) != 0:
            return list(common_times)[0]
        return 0
    
    def schedule(self, time: int):
        for s in self.members:
            s.schedule_meeting(time)

    def __str__(self) -> str:
        member_names = [member.name for member in self.members]
        return f'{self.name} ({", ".join(member_names)})'

class ASUO:

    def __init__(self):
        self.students: list[Student] = []
        self.clubs: list[Club] = []

    def enroll(self, s: Student):
        self.students.append(s)

    def form_clubs(self):
        clubs_to_form: dict[str, Club] = {}

        for student in self.students:
            for interest in student.interests:
                if interest not in clubs_to_form and interest not in self.clubs:
                    clubs_to_form[interest] = Club(interest)
                    clubs_to_form[interest].join(student)
                elif interest in clubs_to_form and interest not in self.clubs:
                    clubs_to_form[interest].join(student)
    
        for club in clubs_to_form:
            self.clubs.append(clubs_to_form[club])

    def schedule_clubs(self):
        for club in self.clubs:
            new_time = club.find_common_time()
            if new_time != 0:
                club.schedule(new_time)
                club.meeting_time = new_time
                
    
    def print_club_schedule(self):
        for club in self.clubs:
            if club.meeting_time is not None:
                print(f'{club} meets at {club.meeting_time}')

asuo = ASUO()
asuo.enroll(Student("Marty", ["badminton", "robotics"]))
asuo.enroll(Student("Kim", ["backgammon"]))
asuo.enroll(Student("Tara", ["robotics", "horticulture", "chess"]))
asuo.enroll(Student("George", ["chess", "badminton"]))

asuo.form_clubs()
asuo.schedule_clubs()
asuo.print_club_schedule()