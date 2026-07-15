print("Welcome to TickIt Planner")

tasks = []
events = []

while True:

    print("\n MAIN MENU ")
    print("1. Task Related")
    print("2. Event Related")
    print("3. Display All")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        while True:

            print("\n TASK MENU ")
            print("1. Add Task")
            print("2. Display Tasks")
            print("3. Mark Task Complete")
            print("4. Delete Task")
            print("5. Back to Main Menu")

            task_choice = input("Enter your choice: ")

            if task_choice == "1":

                print("\nAdd Task Selected")

                title = input("Enter Task Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD): ")

                print("Select Priority: 1. HIGH   2. MEDIUM   3. LOW")
                priority_choice = input("Enter your choice: ")

                if priority_choice == "1":
                    priority = "HIGH"
                elif priority_choice == "3":
                    priority = "LOW"
                else:
                    priority = "MEDIUM"

                task = {
                    "title": title,
                    "description": description,
                    "due_date": due_date,
                    "priority": priority,
                    "completed": False
                }

                tasks.append(task)

                print("\nTask Added Successfully!")

            elif task_choice == "2":

                if len(tasks) == 0:
                    print("\nNo Tasks Available Yet.")

                else:

                    print("\n--- YOUR TASKS ---")

                    for i in range(len(tasks)):

                        t = tasks[i]

                        status = "Done" if t["completed"] else "Pending"

                        print("\n" + str(i + 1) + ". " + t["title"])
                        print("   Description : " + t["description"])
                        print("   Due Date    : " + t["due_date"])
                        print("   Priority    : " + t["priority"])
                        print("   Status      : " + status)

            elif task_choice == "3":

                if len(tasks) == 0:
                    print("\nNo Tasks Available Yet.")

                else:

                    print("\n--- SELECT TASK TO MARK COMPLETE ---")

                    for i in range(len(tasks)):
                        print(str(i + 1) + ". " + tasks[i]["title"])

                    task_num = input("Enter Task Number: ")

                    index = int(task_num) - 1

                    if index >= 0 and index < len(tasks):

                        tasks[index]["completed"] = True
                        print("\nTask marked as complete!")

                    else:

                        print("\nInvalid Task Number!")

            elif task_choice == "4":

                if len(tasks) == 0:
                    print("\nNo Tasks Available Yet.")

                else:

                    print("\n--- SELECT TASK TO DELETE ---")

                    for i in range(len(tasks)):
                        print(str(i + 1) + ". " + tasks[i]["title"])

                    task_num = input("Enter Task Number: ")

                    index = int(task_num) - 1

                    if index >= 0 and index < len(tasks):

                        removed = tasks[index]["title"]
                        tasks.pop(index)
                        print("\nTask '" + removed + "' deleted!")

                    else:

                        print("\nInvalid Task Number!")

            elif task_choice == "5":

                break

            else:

                print("\nInvalid Choice!")

    elif choice == "2":

        while True:

            print("\n EVENT MENU ")
            print("1. Add Event")
            print("2. Display Events")
            print("3. Delete Event")
            print("4. Back to Main Menu")

            event_choice = input("Enter your choice: ")

            if event_choice == "1":

                print("\nAdd Event Selected")

                title = input("Enter Event Title: ")
                description = input("Enter Description: ")
                date = input("Enter Date (YYYY-MM-DD): ")
                start_time = input("Enter Start Time (HH:MM): ")
                end_time = input("Enter End Time (HH:MM): ")
                location = input("Enter Location: ")

                event = {
                    "title": title,
                    "description": description,
                    "date": date,
                    "start_time": start_time,
                    "end_time": end_time,
                    "location": location
                }

                events.append(event)

                print("\nEvent Added Successfully!")

            elif event_choice == "2":

                if len(events) == 0:
                    print("\nNo Events Available Yet.")

                else:

                    print("\n--- YOUR EVENTS ---")

                    for i in range(len(events)):

                        e = events[i]

                        print("\n" + str(i + 1) + ". " + e["title"])
                        print("   Description : " + e["description"])
                        print("   Date        : " + e["date"])
                        print("   Time        : " + e["start_time"] + " - " + e["end_time"])
                        print("   Location    : " + e["location"])
                        
            elif event_choice == "3":

                if len(events) == 0:
                    print("\nNo Events Available Yet.")

                else:

                    print("\n--- SELECT EVENT TO DELETE ---")

                    for i in range(len(events)):
                        print(str(i + 1) + ". " + events[i]["title"])

                    event_num = input("Enter Event Number: ")

                    index = int(event_num) - 1

                    if index >= 0 and index < len(events):

                        removed = events[index]["title"]
                        events.pop(index)
                        print("\nEvent '" + removed + "' deleted!")

                    else:

                        print("\nInvalid Event Number!")

            elif event_choice == "4":

                break

            else:

                print("\nInvalid Choice!")

    elif choice == "3":

        if len(tasks) == 0 and len(events) == 0:
            print("\nNo Tasks or Events Available Yet.")

        else:

            if len(tasks) > 0:

                print("\n--- ALL TASKS ---")

                for i in range(len(tasks)):

                    t = tasks[i]
                    status = "Done" if t["completed"] else "Pending"

                    print("\n" + str(i + 1) + ". " + t["title"])
                    print("   Description : " + t["description"])
                    print("   Due Date    : " + t["due_date"])
                    print("   Priority    : " + t["priority"])
                    print("   Status      : " + status)

            if len(events) > 0:

                print("\n--- ALL EVENTS ---")

                for i in range(len(events)):

                    e = events[i]

                    print("\n" + str(i + 1) + ". " + e["title"])
                    print("   Description : " + e["description"])
                    print("   Date        : " + e["date"])
                    print("   Time        : " + e["start_time"] + " - " + e["end_time"])
                    print("   Location    : " + e["location"])

    elif choice == "4":

        print("\nThank You for using TickIt Planner!")
        break

    else:

        print("\nInvalid Choice! Please try again.")