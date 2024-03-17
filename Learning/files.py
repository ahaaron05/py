file_path = "Learning/blank.txt"
people = ["Bob", "Tim", "Sally"]

with open(file_path, "w") as file_obj:
    for person in people:
        response = input("Why do you like programming: ")
        file_obj.write(f"{person}: {response}\n")