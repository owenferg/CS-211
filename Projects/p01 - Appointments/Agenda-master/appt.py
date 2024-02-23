'''Owen Ferguson
CS 211: Appointments
Defines two Python classes "Appt" for a single appointment and "Agenda" for a list of pointments
Credits:
https://realpython.com/python-enumerate/
'''

from datetime import datetime

class Appt:
    '''An appointment has a start time, an end time, and a title.
    The start and end time should be on the same day.
    Usage example:
        appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), 'Early afternoon nap')
        appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), 'Coffee break')
        if appt2 > appt1:
            print(f'appt1 "{appt1}" was over when appt2 "{appt2}" started')
        elif appt1.overlaps(appt2):
            print('Oh no, a conflict in the schedule!')
            print(appt1.intersect(appt2))
        Should print:
            Oh no, a conflict in the schedule!
            2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    '''
    
    def __init__(self, start: datetime, finish: datetime, desc: str):
        '''An appointment from start time to finish time, with description desc.
        Start and finish should be the same day
        '''
        assert finish > start, f'Period finish ({finish}) must be after start ({start})'

        self.start = start
        self.finish = finish
        self.desc = desc

    def __eq__(self, other: 'Appt') -> bool:
        '''Equality means same time period, ignoring description'''
        return self.start == other.start and self.finish == other.finish
        
    def __lt__(self, other: 'Appt') -> bool:
        '''"Less than" meaning the time period is before the other'''
        return self.finish < other.start
        
    def __gt__(self, other: 'Appt') -> bool:
        '''"Greater than" meaning the time period is after the other'''
        return self.start > other.finish
    
    def overlaps(self, other: 'Appt') -> bool:
        '''Is there a non-zero overlap between these periods?'''
        return not (self.finish <= other.start or self.start >= other.finish)
    
    def intersect(self, other: 'Appt') -> 'Appt':
        '''The overlapping portion of two Appt objects'''
        assert self.overlaps(other) # Precondition

        new_start = max(self.start, other.start)
        new_finish = min(self.finish, other.finish)

        return Appt(new_start, new_finish, f'{self.desc} and {other.desc}')
    
    def __str__(self) -> str:
        '''The textual format of an appointment is
        yyyy-mm-dd hh:mm hh:mm | description
        Note that this is accurate only if start and finish
        are on the same day.
        '''

        date_iso = self.start.date().isoformat()
        start_iso = self.start.time().isoformat(timespec='minutes')
        finish_iso = self.finish.time().isoformat(timespec='minutes')
        return f'{date_iso} {start_iso} {finish_iso} | {self.desc}'
    
    def __repr__(self) -> str:
        return f'Appt({repr(self.start)}, {repr(self.finish)}, {repr(self.desc)})'

class Agenda:
    '''An Agenda is a collection of appointments,
    similar to a list
    
    Usage:
    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), 'Early afternoon nap')
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), 'Coffee break')
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda.text()}")
        print(f"Conflicts:\n {ag_conflicts}")

    Expected output:
    In agenda:
    2018-03-15 13:30 15:30 | Early afternoon nap
    2018-03-15 15:00 16:00 | Coffee break
    Conflicts:
    2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    '''
    
    def __init__(self):
        self.elements = []

    def __eq__(self, other: 'Agenda') -> bool:
        '''Delegate to __eq__ (==) of wrapped lists'''
        return self.elements == other.elements
    
    def __len__(self) -> int:
        '''Delegate to __len__ (len()) of wrapped lists'''
        return len(self.elements)
    
    def append(self, appt: 'Appt') -> None:
        '''Delegate to the append method of the list'''
        self.elements.append(appt)
    
    def __str__(self):
        '''Each Appt on its own line'''
        lines = [ str(e) for e in self.elements ]
        return '\n'.join(lines)
    
    def __repr__(self) -> str:
        '''The constructor does not actually work this way'''
        return f'Agenda({self.elements})'
    
    def sort(self):
        '''Sort agenda by appointment start times'''
        self.elements.sort(key=lambda appt: appt.start)
    
    def conflicts(self) -> 'Agenda':
        '''Returns an agenda consisting of the conflicts
        (overlaps) between appointments in this agenda.
        Side effect: This agenda is sorted
        '''
        result = Agenda()
        self.sort()

        for i, appt1 in enumerate(self.elements): # iterates over each appointment 'appt1' and index 'i' from enumerate
            for appt2 in self.elements[i + 1:]: # iterates over remaining appointments 'appt2' after appt1
                if appt1 < appt2: # if appt1 is before appt2 stop searching
                    break
                elif appt1.overlaps(appt2): # if they overlap add it on to the conflicts list
                    result.elements.append(appt1.intersect(appt2))

        return result

if __name__ == "__main__":
    print("Running usage examples")
    appt1 = Appt(datetime(2018, 3, 15, 13, 30), datetime(2018, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00), datetime(2018, 3, 15, 16, 00), "Coffee break")
    if appt2 > appt1:
        print(f"appt1 '{appt1}' was over when appt2 '{appt2}'  started")
    elif appt1.overlaps(appt2):
        print("Oh no, a conflict in the schedule!")
        print(appt1.intersect(appt2))
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda}")
        print(f"Conflicts:\n {ag_conflicts}")