# todo

while True:
    # Get userr input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        with open("project1/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("project1/todos.txt", "w") as file:
            todos = file.writelines(todos)

    elif user_action.startswith("show"):
        with open("project1/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            # item = item.title()
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            with open("project1/todos.txt", "r") as file:
                todos = file.readlines()
            print("Here is todos existing", todos)
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            with open("project1/todos.txt", "w") as file:
                todos = file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open("project1/todos.txt", "r") as file:
                todos = file.readlines()
            
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            with open("project1/todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye")
