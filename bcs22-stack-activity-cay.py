class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        print(f'Task "{title}" added successfully!')

    def mark_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f'Task "{self.tasks[task_index].title}" marked as completed!')
        else:
            print('Invalid task index!')

    def edit_task(self, task_index, new_title, new_description):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            task.title, task.description = new_title, new_description
            print('Task updated successfully!')
        else:
            print('Invalid task index!')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for index, task in enumerate(self.tasks):
                status = 'Completed' if task.completed else 'Pending'
                print(f'{index}. {task.title} - {task.description} [{status}]')

def main():
    task_manager = TaskManager()

    while True:
        print('\nTask Manager Menu:')
        print('1. Add Task')
        print('2. Mark Task as Completed')
        print('3. Edit Task')
        print('4. Display Tasks')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            title = input('Enter task title: ')
            description = input('Enter task description: ')
            task_manager.add_task(title, description)
        elif choice == '2':
            task_index = int(input('Enter task index to mark as completed: '))
            task_manager.mark_as_completed(task_index)
        elif choice == '3':
            task_index = int(input('Enter task index to edit: '))
            new_title = input('Enter new task title: ')
            new_description = input('Enter new task description: ')
            task_manager.edit_task(task_index, new_title, new_description)
        elif choice == '4':
            task_manager.display_tasks()
        elif choice == '5':
            print('Exiting Task Manager. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()
