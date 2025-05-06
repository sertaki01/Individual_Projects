
print(r"""
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \
   |_|\___/ \__,_|\___/|___/
      
""")

print("***********************************")

answer = input("Enter a command. Type 'h' for help:\n")

todo_list = []

completed_todos = []

completed_counter = 0

while not answer == "q":
    
    counter = 0

    if answer.isnumeric():
        if int(answer) <= len(todo_list):
          idx = int(answer) - 1 
          completed_todos.append(todo_list[idx])
          todo_list.pop(idx)
          completed_counter += 1
    elif answer != "h":
        todo_list.append(answer)
    else:
        print("TODO LIST HELP\n" + "Type 'q' to quit\n" + "To add a todo to the list, type it and hit enter\n" + "To complete a todo enter its number")
    
    
    for todo in todo_list:
        print(f"{counter + 1}) {todo}")
        counter += 1

    print("***********************************")

    answer = input("Enter a command. Type 'h' for help:\n")

print(f"Today you completed {completed_counter} todos:")

if completed_counter > 0: 
  for todo in completed_todos:
      print(f"* {todo}")
else:
    print("You haven't done any todos for today. You need to start your tasks")