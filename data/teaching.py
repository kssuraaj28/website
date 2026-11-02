from dataclasses import dataclass

from data_model import Bold, BulletList, Section, Text


@dataclass(frozen=True)
class CourseTeaching:
    code: str
    name: str
    role: str
    sem: str
    year: int

    def __post_init__(self):
        possible_sem = ('Fall', 'Spring', 'Summer', 'Winter')
        # TODO: Vet course numbers?
        if self.sem not in possible_sem:
            raise ValueError(f"sem must be in {possible_sem}. Got {self.sem}")


def course_to_text(c: CourseTeaching) -> Text:
    return Text((
        Bold(f'{c.sem} {c.year}: '),
        f'{c.role}, {c.code} ({c.name})'))  # TODO: Make this better


head_ta = 'Head teaching assistant'
guest = 'Guest lecture'

taed = [
    CourseTeaching('CS4450', 'Introduction to Computer Networks',
                   head_ta, 'Fall', 2022),

    CourseTeaching('CS4450', 'Introduction to Computer Networks',
                   head_ta, 'Spring', 2023),

    CourseTeaching('CS3410', 'Computer System Organization and Programming',
                   head_ta, 'Fall', 2023),

    CourseTeaching('CS4450', 'Introduction to Computer Networks',
                   guest, 'Spring', 2024),

    CourseTeaching('CS4450', 'Introduction to Computer Networks',
                   guest, 'Fall', 2024),

    CourseTeaching('CS2800', 'Mathematical Foundations of Computing',
                   head_ta, 'Fall', 2025),

    CourseTeaching('CS2800', 'Mathematical Foundations of Computing',
                   head_ta, 'Fall', 2026),
]
taed.reverse()

this_section = Section(
    "Teaching",
    (Text(("I've been involved with teaching the following courses at Cornell:",)), BulletList(tuple(course_to_text(c) for c in taed))))
