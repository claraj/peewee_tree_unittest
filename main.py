import controller 
import ui 
def main():

    while True:
        choice = ui.menu_choice()
        if choice == 'A':
            controller.add_tree()
        elif choice == 'S':
            controller.all_trees()
        elif choice == 'D':
            controller.delete_tree()
        elif choice == 'Q':
            break 


if __name__ == '__main__':
    main()
