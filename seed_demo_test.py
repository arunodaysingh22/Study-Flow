import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from todo.models import Course, PracticeTest, Question

def seed_demo_test():
    # 1. Create a demo test
    # test, created = PracticeTest.objects.get_or_create(title="Demo Academic Challenge 2026")
    test = PracticeTest.objects.filter(title="Demo Academic Challenge 2026").first()
    if not test:
        test = PracticeTest.objects.create(title="Demo Academic Challenge 2026")
    
    # Clear existing questions to avoid duplicates during re-seeding
    test.questions.all().delete()

    # 2. Add sample questions
    questions_data = [
        {
            'text': 'Which data structure follows the LIFO (Last In First Out) principle?',
            'option_a': 'Queue', 'option_b': 'Linked List', 'option_c': 'Stack', 'option_d': 'Array',
            'correct': 'C'
        },
        {
            'text': 'What is the primary purpose of the Django middleware?',
            'option_a': 'Database management', 'option_b': 'Request/Response processing', 'option_c': 'URL routing', 'option_d': 'Template rendering',
            'correct': 'B'
        },
        {
            'text': 'In UI design, what does "a11y" stand for?',
            'option_a': 'Alignment', 'option_b': 'Accessibility', 'option_c': 'Aesthetics', 'option_d': 'Availability',
            'correct': 'B'
        },
        {
            'text': 'Which complexity class represents problems solvable in polynomial time?',
            'option_a': 'NP', 'option_b': 'P', 'option_c': 'EXP', 'option_d': 'Log-space',
            'correct': 'B'
        },
        {
            'text': 'What is the standard port for HTTP?',
            'option_a': '443', 'option_b': '22', 'option_c': '80', 'option_d': '8080',
            'correct': 'C'
        },
        {
            'text': 'Which SQL command is used to remove all records from a table without deleting the table structure?',
            'option_a': 'DELETE', 'option_b': 'DROP', 'option_c': 'TRUNCATE', 'option_d': 'REMOVE',
            'correct': 'C'
        }
    ]

    for q_data in questions_data:
        Question.objects.create(
            test=test,
            text=q_data['text'],
            option_a=q_data['option_a'],
            option_b=q_data['option_b'],
            option_c=q_data['option_c'],
            option_d=q_data['option_d'],
            correct_option=q_data['correct']
        )

    print(f"Successfully seeded demo test: {test.title} with {len(questions_data)} questions.")

if __name__ == "__main__":
    seed_demo_test()
