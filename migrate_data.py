import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from todo.models import Task

old_tasks = Task.objects.using('old_sqlite').all()
new_tasks = []
for task in old_tasks:
    # Create the instance without saving
    new_task = Task(
        id=task.id,
        title=task.title,
        is_completed=task.is_completed,
        priority=task.priority
    )
    # Manually set the created_at to preserve original timestamp
    new_task.created_at = task.created_at
    new_tasks.append(new_task)

Task.objects.using('default').bulk_create(new_tasks)
print(f"Migrated {len(new_tasks)} tasks successfully.")
