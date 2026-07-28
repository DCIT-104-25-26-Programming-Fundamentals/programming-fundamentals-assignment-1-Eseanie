def main():

    def add_task(tasks):
        task = input("Enter task: ").strip()

        if task == "":
            print("Task cannot be empty.")
        else:
            tasks.append(task)
            print(f'Task added: "{task}"')


    def view_tasks(tasks):
        if len(tasks) == 0:
            print("Your to-do list is empty.")
            return

        print("Your Tasks:")

        number = 1

        for task in tasks:
            print(f"{number}. {task}")
            number += 1


    def delete_task(tasks):
        if len(tasks) == 0:
            print("There are no tasks to delete.")
            return

        view_tasks(tasks)

        task_number = int(input("Enter task number to delete: "))
        
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Invalid task number.")


    def display_menu():
        print("============================")
        print("     TO-DO LIST MENU")
        print("============================")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")


        tasks = []

        while True:
            display_menu()

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                add_task(tasks)

            elif choice == "2":
                view_tasks(tasks)

            elif choice == "3":
                delete_task(tasks)

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 4.")


main()