import pymysql
from secrets import host, user, password

#print all open tasks and their ids in order of ids
def show_tasks(c):
    select_statement = """
        SELECT id, task FROM tasks WHERE done != 1 ORDER BY id;
        """
    c.execute(select_statement)
    print(c.fetchall())

def mark_as_done(c, task_id):
    update_statement = """
        UPDATE tasks SET done = 1 WHERE id = %s;
        """
    c.execute(update_statement, (task_id))

def add_new_task(c, new_task, done_status):
    insert_statement = """
        INSERT INTO tasks (task, done) 
        VALUES (%s, %s);
        """  
    c.execute(insert_statement, (new_task, done_status))

db = pymysql.connect(host, user, password, "")
# 1. Create generically to MySQL and create the todo_app database
with db.cursor() as c:
    c._defer_warnings = True
    c.execute("CREATE DATABASE IF NOT EXISTS todo_app DEFAULT CHARACTER SET utf8;")
    #CREATE SCHEMA/DATABASE

db.close()

# 2. Connect to newly created database todo_app
db = pymysql.connect(host, user, password, "todo_app")

# Here is our code!

create_statement = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
        task TEXT NOT NULL, 
        done BOOLEAN
    );
""" 
with db.cursor() as c:
    c.execute(create_statement)
    #In a loop: ask user what to do using input()
    # show task list
    # mark task as done
    # add new task
    # exit application
    while True:
        print("""
            Menu:
            1 - show task list
            2 - mark task as done
            3 - add new task
            4 - exit application
            """)
        option = int(input("Your option is: "))
        if option not in [1, 2, 3, 4]:
            continue
        if option == 1:
            show_tasks(c)
        elif option == 2:
            task_id = int(input("Please insert ID for update: "))
            mark_as_done(c, task_id)
        elif option == 3:
            new_task = input("Please insert new task name: ")
            done_status = input(" Please insert status (0 or 1): ")
            add_new_task(c, new_task, done_status)
        if option == 4:
            break
    db.commit()
db.close()

# option_mappings = {
#     1: show_tasks
#     2: mark_as_done
#     3: add_new_task
# }
