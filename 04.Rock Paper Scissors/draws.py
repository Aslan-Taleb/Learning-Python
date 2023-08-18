rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lost = '''
                         ___`.\.//
                            `---.---   WHO LOST NOW ?!
                           /     \.--
                          /       \-
                         |   /\    
                         |\==/\==/  |
                         | `@'`@'  .--.
                  .--------.           )
                .'             .   `._/
               /               |     
              .               /       |
              |              /        |
              |            .'         |   .--.
             .'`.        .'_          |  /    
           .'    `.__.--'.--`.       / .'      |
         .'            .|    \\     |_/        |
       .'            .' |     \\               |
     .-`.           /   |      .      __       |
   .'    `.     \   |   `           .'  )      
  /        \   / \  |            .-'   /       |
 (  /       \ /   \ |                 |        |
  \/         (     \/                 |        |
  (  /        )    /                 /   _.----|
   \/   //   /   .'                  |.-'       `
   (   /(   /   /                    /      `.   |
    `.(  `-')  .---.                |    `.   `._/
       `._.'  /     `.   .---.      |  .   `._.'
              |       \ /     `.     \  `.___.'
              |        Y        `.    `.___.'
              |      . |          \         
              |       `|           \         |
              |        |       .    \        |
              |        |        \    \       |
            .--.       |         \           |
           /    `.  .----.        \          /
          /       \/      \        \        /
          |       |        \       |       /
           \      |    @    \   `-. \     /
            \      \         \     \|.__.'
             \      \         \     |
              \      \         \    |
               \      \         \   |
                \    .'`.        \  |
                 `.-'    `.    _.'\ |
                   |       `.-'    ||
              .     \     . `.     ||      .'
               `.    `-.-'    `.__.'     .'
                 `.                    .'
             .                       .'
              `.
                                           .-'
                                        .-'

      \                 
       \         ..      
        \       /  `-.--.___ __.-.___
`-.      \     /  #   `-._.-'    \   `--.__
   `-.        /  ####    /   ###  \        `.
________     /  #### ############  |       _|           .'
            |\ #### ##############  \__.--' |    /    .'
            | ####################  |       |   /   .'
            | #### ###############  |       |  /
            | #### ###############  |      /|      ----
          . | #### ###############  |    .'<    ____
        .'  | ####################  | _.'-'\|
      .'    |   ##################  |       |
             `.   ################  |       |
               `.    ############   |       | ----
              ___`.     #####     _..____.-'     .
             |`-._ `-._       _.-'    \\\         `.
          .'`-._  `-._ `-._.-'`--.___.-' \          `.
        .' .. . `-._  `-._        ___.---'|   \   
      .' .. . .. .  `-._  `-.__.-'        |    \   
     |`-. . ..  . .. .  `-._|             |     \   
     |   `-._ . ..  . ..   .'            _|
      `-._   `-._ . ..   .' |      __.--'
          `-._   `-._  .' .'|__.--'
              `-._   `' .'
                  `-._.'
                  '''

won = '''
              ,~,
             (((}
             -''-.
            (\  /\) 
      ~______\) | `
   ~~~(         |  ') 
      | )____(  |
     /|/     ` /|
     \ \      / |
so ez  |\|\   /| |
    '''
draw = '''
Art by Shanaka Dias
  <=======]}======
    --.   /|
   _\"/_.'/
 .'._._,.'
 :/ \ /
(L  /--',----._
    |          \\
   : /-\ .'-'\ / |
 \\, ||    \|
     \/ ||    ||
     I did not lose,duel me again !!!!!!
'''
#Write your code below this line 👇

def play(choice):
    name_choice = ""
    if choice == 0:
        print(rock)
        name_choice = "Rock"
    elif choice == 1:
        print(paper)
        name_choice = "Paper"
    elif choice == 2:
        print(scissors)  
        name_choice = "Scissors"
    return name_choice

def rules(human,computer):
    if human == computer:
        print(draw)
        print("Draw ! ")
        return False
    if human == "Rock" and computer == "Paper" or human == "Scissors" and computer == "Rock" or human == "Paper" and computer == "Scissors"  :
        print(lost)
        print("You lose")
        return True
    elif human == "Paper" and computer == "Rock" or human == "Rock" and computer == "Scissors" or human == "Scissors" and computer == "Paper":
        print(won)
        print("You won !!")
        return True
        