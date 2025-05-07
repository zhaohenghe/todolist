import argparse
from task_manager import TaskManager
from storage import load_tasks, save_tasks

TASKS_FILE = 'tasks.json'

def main():
    parser = argparse.ArgumentParser(description='ToDoList CLI App')
    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('--title', required=True)
    add_parser.add_argument('--description', required=True)
    add_parser.add_argument('--due', required=True)

    subparsers.add_parser('list')

    complete_parser = subparsers.add_parser('complete')
    complete_parser.add_argument('--index', type=int, required=True)


    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('--index', type=int, required=True)

    args = parser.parse_args()
    tasks = load_tasks()
    manager = TaskManager(tasks)

    if args.command == 'add':
        manager.add_task(args.title, args.description, args.due)
        print(f"Task '{args.title}' added.")
    elif args.command == 'list':
        manager.list_tasks()
    elif args.command == 'complete':
        manager.complete_task(args.index)
    elif args.command == 'delete':
        manager.delete_task(args.index)
    elif args.command == 'help':
        parser.print_help()
        return
    else:
        parser.print_help()
        return

    save_tasks(manager.tasks)

if __name__ == '__main__':
    main()