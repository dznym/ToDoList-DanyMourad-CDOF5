def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Afficher les tâches")
    print("2. Ajouter une tâche")
    print("3. Supprimer une tâche")
    print("4. Mettre à jour une tâche")
    print("5. Quitter")

def display_tasks(tasks):
    if not tasks:
        print("La liste de tâches est vide.")
    else:
        print("\n--- Vos Tâches ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Entrez la tâche à ajouter : ")
    if task:
        tasks.append(task)
        print("Tâche ajoutée avec succès !")
    else:
        print("La tâche ne peut pas être vide.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Entrez le numéro de la tâche à supprimer : "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Tâche supprimée : {removed_task}")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")
def update_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Entrez le numéro de la tâche à mettre à jour : "))
        if 1 <= task_num <= len(tasks):
            while True:
                new_task = input("Entrez la nouvelle tâche : ")
                if new_task:
                    tasks[task_num - 1] = new_task
                    print("Tâche mise à jour avec succès !")
                    break
                else:
                    print("La nouvelle tâche ne peut pas être vide. Veuillez réessayer.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choisissez une option (1-5) : ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()

