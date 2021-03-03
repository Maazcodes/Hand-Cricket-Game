# Welcome to see the codes of the game behind the curtains.
# Yes it is the game of Bam Bush - hand cricket
'''human player with machine player'''

print('Rules of the game')
print('First, the human player will have to choose: odd or even, for a toss')
print('Both the players will have to select(type) the numbers from 1 to 6 at the same time')
print('The toss will depend on the sum of both the numbers')
print('One will bat and the other will bowl as per the third point')
print('If the numbers selected by both the players are same, then it is OUT')

from random import randint


def computer_runs():  # Ask the computer to select the runs from 1-6
    position = randint(1, 6)
    return position


def choose_odd_even():  # Ask the user to choose odd or even
    fool = ''

    while fool not in ['odd', 'even']:
        fool = input('choose odd or even - ').lower()

        if fool not in ['odd', 'even']:
            print('selection invalid')
            continue

        if fool[0] == 'o':
            return ('odd', 'even')
        else:
            return ('even', 'odd')


def human_runs():  # Ask the user to select the runs from 1-6
    choice = ''

    while choice not in ['1', '2', '3', '4', '5', '6']:
        choice = input('select runs from 1 to 6 - ')

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print('selection invalid')

    return int(choice)


def odd_or_even(position, choice):  # To check if the sum of the user and machine runs are even or odd.
    if (position+choice) % 2 == 0:
        return True
    else:
        return False


def toss_win_check(fool, position, choice):  # To check who wins the toss - machine or the user
    if fool == 'even' and odd_or_even(position, choice):  # even and the user won the toss
        return True
    elif fool == 'odd' and not odd_or_even(position, choice):  # odd and the user won the toss
        return True
    else:  # machine won the toss
        return False


def bat_bowl(fool, position, choice):
    if toss_win_check(fool, position, choice):  # if the user wins the toss, ask him or her to select bowling or batting
        print('Great!! You have won the toss')
        select = input('choose batting or bowling - ').lower()
        users = select

        if users[0:3] == 'bat':
            machines = 'bowling'
        else:
            machines = 'batting'
    else:
        
        print('you loose the toss')  # if the computer wins the toss, ask the computer to choose batting or bowling.
        lst = {1: 'batting', 2: 'bowling'}
        pos = randint(1, 2)
        value = lst[pos]
        machines = value
        if machines == 'batting':
            users = 'bowling'
            print('the machine has selected to bat first')
            
        else:
            print('the machine has selected to bowl first')
            users = 'batting'
    return users, machines


run_lst = [0]


def total_runs_user(choice):
    # Appending or adding the runs made by the user while batting and to return the sum of these runs.
    run_lst.append(choice)
    result = 0
    for i in run_lst:
        result = result + i
    return result


mach_lst = [0]


def total_runs_machine(position):  # the same goes for the machine.
    mach_lst.append(position)
    result1 = 0
    for i in mach_lst:
        result1 = result1 + i
    return result1


def bowl_byuser():  # dummy bowling runs by user which should not be added in the above runs.
    bowl_user = ''

    while bowl_user not in ['1', '2', '3', '4', '5', '6']:
        bowl_user = input('select runs from 1 to 6 - ')

        if bowl_user not in ['1', '2', '3', '4', '5', '6']:
            print('selection invalid')

    return int(bowl_user)


def bowl_bymach():  # dummy bowling runs by machine
    bowl_mach = randint(1, 6)
    return bowl_mach


def replay():  # clearing the list of runs of the previous game made by the user or machine

    play = input('Keep playing? Yes or No - ').lower()
    if play[0] == 'y':
        run_lst.clear()
        mach_lst.clear()
        print('\n'*5)
        return True
    else:
        return False


print('\nWelcome to the game of Bam Bush!!\n')

while True:
    user, machine = choose_odd_even()
    human = human_runs()
    goal = computer_runs()
    print('these are the runs of machine - ', goal)
    
    rose = odd_or_even(goal, human)
   
    toss_win_check(user, goal, human)

    user1, machine1 = bat_bowl(user, goal, human)
    
    game_on = input('Are you ready to play? - Yes or No - ').lower()
    if game_on[0] == 'y':
        games = True
    else:
        games = False
        
    while games:
        if (user1 == 'batting' and toss_win_check(user, goal, human)) or \
                (machine1 == 'bowling' and not toss_win_check(user, goal, human)):
            
            # (user wins the toss and opt to bat) or (machine wins the toss and opt to bowl)
            print('Machine is bowling\n')
            human = human_runs()  # user is batting
            print('Baaaam')
            bowlmach = bowl_bymach()  # machine is bowling
            print('runs selected by machine are - ', bowlmach)
            print('Busssh\n')
            Runs_user = total_runs_user(human)
            
            if human == bowlmach:  # out check
                
                print('Out!!\n')
                lava = (Runs_user + 1) - human
                print('The number of runs to be scored by the machine are - ', lava)
                # minus human means not to include the runs scored in the end.
                print('\nNow you will bowl. So start defending.\n')
                bowling = True

                # bowling by the user, machine has to score the runs made by the user.
                while bowling:
                    
                    bowluser = bowl_byuser()  # user is bowling
                    goal = computer_runs()  # machine is batting
                    print(f'runs selected by machine are - {goal}\n')
                    Runs_machine = total_runs_machine(goal)

                    if Runs_machine >= lava:  # win check
                        print(f'The machine has scored {Runs_machine} runs')
                        print('Oops!! You loose\n')    
                        games = False
                        break
                    
                    elif bowluser == goal:  # out check
                        print('\nOut!! Congratz!! You win\n')
                        games = False
                        break
                    else:
                        print('The total number of runs scored by the machine are - ', Runs_machine)

                        bowling = True  # continue bowling by user
            else:
                print('The total number of runs scored by you are - ', Runs_user)

                user1 = 'batting'  # continue batting by user

        elif (user1 == 'bowling' and toss_win_check(user, goal, human)) \
                or (machine1 == 'batting' and not toss_win_check(user, goal, human)):
            # (user wins the toss and opt to bowl) or (machine wins the toss and opt to bat)
            print('Machine is batting now')
            bowluser = bowl_byuser()  # user is bowling
            goal = computer_runs()  # machine is batting
            print('runs selected by machine are - ', goal)
            Runs_machine = total_runs_machine(goal)
            print('\n')

            if bowluser == goal:
                print('Out!!')
                guava = (Runs_machine+1) - goal
                print('The number of runs are to be scored by you are - ', guava)
                print('\nNow you will bat')
                batting = True

                # batting by user, user has to make the runs scored by the machine.
                while batting:
                    
                    human = human_runs()  # user is batting
                    bowlmach = bowl_bymach()  # machine is bowling
                    print('runs selected by machine are - ', bowlmach)
                    Runs_user = total_runs_user(human)
                    print('\n')
                    Runs_machine = total_runs_machine(goal)

                    if Runs_user >= guava:  # out check

                        print('Congratz!! You win!\n')    
                        games = False
                        break
                    elif human == bowlmach:  # win check
                        print('Out!! You loose\n')
                        games = False
                        break
                    else:
                        print('The total number of runs scored by you are - ', Runs_user)

                        batting = True  # coninue batting by user
                
            else:
                
                print('The total number of runs scored by the machine are - ', Runs_machine)

                user1 = 'bowling'  # continue bowling by user
                
    if not replay():
        break

  #The end of game
