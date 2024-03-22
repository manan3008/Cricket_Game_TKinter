####
# Group Number 5

# STUDENT NAME: Manan Amitkumar Patel
# STUDENT NUMBER: s361298

# STUDENT NAME: Dhruv Dineshbhai Patel
# STUDENT NUMBER: s360693
####

# VIDEO LINK: https://youtu.be/wdmMuErJlZE

# QUESTION 2 - OPEN ENDED QUESTION

# Import all functions and built-in modules of tkinter library
from tkinter import *

# Import tkinter.messagebox module provides a template base class as well as variety of convenience methods for commonly used configuration
import tkinter.messagebox

# Import random for generating or manipulating random integers
import random

# Creating the window
screen = Tk()

# Setting up the dimensions of the Tkinter window
screen.geometry("1350x750+0+0")

# setting up the title of window
screen.title("CRICKET 2022")

# setting up the background color of window
screen.configure(background='#536dfe')

# set the frame attributes in tops variable
Tops = Frame(screen, bg='#6200ea', pady=2, width=1350, height=100, relief=RIDGE)

# grid geometery use for setting up rows and column to arrange widgets
Tops.grid(row=0, column=0)

# setting the main frame 
MainFrame = Frame(screen, bg='#1a237e', pady=2,
                  width=1350, height=400, relief=RIDGE)

# Setting main frame grid with 2 rows and 0 columns
MainFrame.grid(row=2, column=0, sticky=S + N + E + W)

# setting the left frame  
LeftFrame = Frame(MainFrame, bd=10, width=675, height=500,
                  pady=2, padx=10, bg='#1a237e', relief=RIDGE)
LeftFrame.pack(side=LEFT)

# setting up the title using label function named CRICKET 2022
lblTitle = Label(Tops, font=('arial', 35, 'bold'), text="CRICKET 2022", bd=21, fg='white', bg='#536dfe',
                 justify=CENTER)
lblTitle.grid(row=0, column=0, sticky=S + N + E + W)

# setting information label using label function
Info_lbl = Label(screen, font=('arial', 20, 'bold'),
                 text="TEAM  SELECTION", fg='white', bg='#03a9f4')
Info_lbl.grid(row=1, column=0)

# ==================== state management ====================

# setting up two empty variable that is my team and opponent team selection
my_team = ""
opp_team = ""

# constructing the string variable with master widget
my_team_var = StringVar()
opp_team_var = StringVar()

# ==================== display all buttons for teams ====================

INDIA = Button(LeftFrame, text="INDIA ", font=('arial', 30, 'bold'), height=1,
             width=12, fg="#fffde7", bg='#fdd835', command=lambda: select_team("IND", INDIA))
INDIA.grid(row=0, column=0, padx=10, pady=18, sticky=S + N + E + W)

AUSTRALIA = Button(LeftFrame, text="AUSTRALIA", font=('arial', 30, 'bold'), height=1,
            width=12, fg="#fffde7", bg='#3d5afe', command=lambda: select_team("AUS", AUSTRALIA))
AUSTRALIA.grid(row=0, column=1, padx=10, pady=18, sticky=S + N + E + W)

ENGLAND = Button(LeftFrame, text="ENGLAND", font=('arial', 30, 'bold'), height=1,
              width=12, fg="#fffde7", bg='#d81b60', command=lambda: select_team("ENG", ENGLAND))
ENGLAND.grid(row=1, column=0, padx=10, pady=18, sticky=S + N + E + W)

NEWZEALAND = Button(LeftFrame, text="NEW ZEALAND", font=('arial', 30, 'bold'), height=1,
             width=12, fg="#fffde7", bg='#5e35b1', command=lambda: select_team("NZ", NEWZEALAND))
NEWZEALAND.grid(row=1, column=1, padx=10, pady=18, sticky=S + N + E + W)

PAKISTAN = Button(LeftFrame, text="PAKISTAN", font=('arial', 30, 'bold'), height=1,
             width=12, fg="#fffde7", bg='#00e676', command=lambda: select_team("PAK", PAKISTAN))
PAKISTAN.grid(row=2, column=0, padx=10, pady=18, sticky=S + N + E + W)

BANGLADESH = Button(LeftFrame, text="BANGLADESH", font=('arial', 30, 'bold'), height=1,
            width=12, fg="#fffde7", bg='#448aff', command=lambda: select_team("BAN", BANGLADESH))
BANGLADESH.grid(row=2, column=1, padx=10, pady=18, sticky=S + N + E + W)

IRELAND = Button(LeftFrame, text="IRELAND", font=('arial', 30, 'bold'), height=1,
             width=12, fg="#fffde7", bg='#ef6c00', command=lambda: select_team("IRL", IRELAND))
IRELAND.grid(row=3, column=0, padx=10, pady=18, sticky=S + N + E + W)

WESTINDIES = Button(LeftFrame, text="WESTINDIES", font=('arial', 30, 'bold'), height=1,
            width=12, fg="#fffde7", bg='#e040fb', command=lambda: select_team("WI", WESTINDIES))
WESTINDIES.grid(row=3, column=1, padx=10, pady=18, sticky=S + N + E + W)

#  ==================== display all buttons  ====================

# setting up the frame in the right frame widget with 500 height and width 675
# padx and pady are also setup for pixel to pad widget horizontally and vertically

RightFrame = Frame(MainFrame, bd=10, width=675, height=500,
                   padx=10, pady=2, bg='#1a237e', relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=8, width=600, height=200,
                    padx=10, pady=2, bg='#303f9f', relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=8, width=560, height=360,
                    padx=10, pady=2, bg='#303f9f', relief=RIDGE)
RightFrame2.grid(row=1, column=0)

# Setting up label on rightframe with user team selection and oposition team selection
lbl_myteam = Label(RightFrame1, font=('arial', 40, 'bold'),
                   text="Your Team :", padx=2, pady=2, bg="#5e35b1", fg="white")
lbl_myteam.grid(row=0, column=0, sticky=W)

lbl_opp_team = Label(RightFrame1, font=('arial', 40, 'bold'),
                     text="Opp. Team :", padx=2, pady=2, bg="#5e35b1", fg="white")
lbl_opp_team.grid(row=1, column=0, sticky=W)

# entry widget is used for single line text input
# here we are going to print the user selected team and oposition team in that entry box

e_myteam = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=3, fg="black",
                 width=7, justify=LEFT, textvariable=my_team_var).grid(row=0, column=1)

e_oppteam = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=3, fg="black",
                  width=7, justify=LEFT, textvariable=opp_team_var).grid(row=1, column=1)


# Setting up two button widget one is for reset game and another is for start game

btn_resetgame = Button(RightFrame2, text="RESET GAME", font=('arial', 40, 'bold'), height=1, width=15, fg='white',
                    bg='#00897b', command=lambda: reset_game(1))
btn_resetgame.grid(row=2, column=0, padx=1, pady=11, columnspan=2)


btn_startgame = Button(RightFrame2, text="Start Game", font=('arial', 40, 'bold'), height=1, width=15, fg='white',
                    bg='#5e35b1', state="disabled", command=lambda: startGame())
btn_startgame.grid(row=3, column=0, padx=1, pady=11, columnspan=2)

# team selection variable initialize at 0
team_selection_count = 0

# Setting up the validation 
# declaring function with parameter teamname and object
def select_team(teamname, obj):

    # Global variable declaration for my_team , opp_team and team_selection_count
    global my_team, team_selection_count, opp_team

    # checking if the team selection count is less than 2
    if team_selection_count < 2:

        # if the length of my_team  is 0
        if len(my_team) == 0:

            # swapping the teamname with my_team and set the variable team with my team
            my_team = teamname
            my_team_var.set(my_team)

            # Increment the team selection count by 1
            team_selection_count += 1
        
        
        else:
            # if the teamname is not equal to myteam variable
            if teamname != my_team:

                # validate successful, then swap the team name and set the opp_team variable
                opp_team = teamname
                opp_team_var.set(opp_team)

                # configure the state to normal when the validation successful
                btn_startgame.configure(state="normal")

                # increment the team_selection_count by 1
                team_selection_count += 1


# ====================== state management ======================

# setting up dict() function which creates dictionary
# A dictionary is a collection which is unordered, changeable and indexed

# two variables, batsman and bowlers selection in unorder list
batsman_dict = dict()
bowers_dict = dict()

# managing the value of widget, usingg StringVar()
lbl_player_selection = StringVar()
lbl_bow_selection = StringVar()

# ====================== state management ======================

# setting up the frame
MainFrame1 = Frame()

# function declaration name startGame():
def startGame():

    # mainframe will be destroy all the widgets and exit mainloop
    MainFrame.destroy()

    # setting up, information label
    Info_lbl.configure(text="Player Selection")

    # Setting up mainframe, batsman list frame and bowler list frame
    MainFrame1 = Frame(screen, bg='#1a237e', width=1350,
                       pady=10, padx=10, height=600, relief=RIDGE)
    MainFrame1.grid(row=2, column=0, sticky=S + N + E + W)

    bat_list_frame = Frame(MainFrame1, bd=10, width=750,
                           height=600, pady=10, padx=10, bg='#1a237e', relief=RIDGE)
    bat_list_frame.grid(row=0, column=0)

    bow_list_frame = Frame(MainFrame1, bd=10, width=750,
                           height=600, pady=10, padx=10, bg='#880e4f', relief=RIDGE)
    bow_list_frame.grid(row=0, column=1)

    Myplayer_Frame = Frame(MainFrame1, bd=10, width=500,
                           height=600, pady=10, padx=10, bg='#42a5f5', relief=RIDGE)
    Myplayer_Frame.grid(row=0, column=2)

    # button for reset and play game

    btn = Button(Myplayer_Frame, text="RESET", font=('arial', 30, 'bold'), height=3,
                 width=20, fg="white", bg='#1565c0', command=lambda: reset_game(2))
    btn.grid(row=2, column=0, padx=10, pady=10,
             columnspan=10, sticky=S + N + E + W)

    btn = Button(Myplayer_Frame, text="PLAY GAME", font=('arial', 30, 'bold'),
                 height=3, width=20, fg="white", bg='#1565c0', command=lambda: display_player())
    btn.grid(row=4, column=0, padx=10, pady=10,
             columnspan=10, sticky=S + N + E + W)

    # select batsman using button
    lbl_batsman = Button(bat_list_frame, text="SELECT BATSMAN (0/4)", textvariable=lbl_player_selection, font=(
        'arial', 20, 'bold'), height=1, width=15, fg="#9c27b0", bg='white', command=lambda: select_team("CSK", INDIA))
    lbl_batsman.grid(row=0, column=0, columnspan=3,
                     padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="MS Dhoni", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("MS Dhoni"))
    btn.grid(row=1, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Virat Kohali", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Virat Kohali"))
    btn.grid(row=1, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Faf du plessis", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Faf du plessis"))
    btn.grid(row=1, column=2, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Hardik Pandya", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Hardik Pandya"))
    btn.grid(row=2, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="KL Rahul", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("KL Rahul"))
    btn.grid(row=2, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Rohit Sharma", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Rohit Sharma"))
    btn.grid(row=2, column=2, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="David Warner", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("David Warner"))
    btn.grid(row=3, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Shreyas Iyer", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Shreyas Iyer"))
    btn.grid(row=3, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Sanju Samson", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Sanju Samson"))
    btn.grid(row=3, column=2, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="S. Dhawan", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("S. Dhawan"))
    btn.grid(row=4, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Q. DE.KOCK", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Q. DE.KOCK"))
    btn.grid(row=4, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bat_list_frame, text="Ab de villiers", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#9c27b0', command=lambda: select_bat("Ab de villiers"))
    btn.grid(row=4, column=2, padx=10, pady=10, sticky=S + N + E + W)

    # select bowler
    lbl_bowler = Button(bow_list_frame, text="SELECT BOWLER (0/2)", font=('arial', 20, 'bold'), textvariable=lbl_bow_selection,
                        height=1, width=15, fg="#2962ff", bg='white', command=lambda: select_team("CSK", INDIA))
    lbl_bowler.grid(row=0, column=0, columnspan=3,
                    padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="K. Rabada", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("K. Rabada"))
    btn.grid(row=1, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="M. Shami", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("M. Shami"))
    btn.grid(row=1, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Rashid Khan", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Rashid Khan"))
    btn.grid(row=1, column=2, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Jofra Archer", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Jofra Archer"))
    btn.grid(row=2, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="JaspritBumrah", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("JaspritBumrah"))
    btn.grid(row=2, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Y. Chahal", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Y. Chahal"))
    btn.grid(row=2, column=2, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Trent Boult", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Trent Boult"))
    btn.grid(row=3, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Anrich Nortje", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Anrich Nortje"))
    btn.grid(row=3, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Rahul Chahar", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Rahul Chahar"))
    btn.grid(row=3, column=2, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Chakravarthy", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Chakravarthy"))
    btn.grid(row=4, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="Bravo", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("Bravo"))
    btn.grid(row=4, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn = Button(bow_list_frame, text="piyush", font=('arial', 10, 'bold'), height=3,
                 width=11, fg="#fffde7", bg='#e65100', command=lambda: select_ball("piyush"))
    btn.grid(row=4, column=2, padx=10, pady=10, sticky=S + N + E + W)

# setting batsman and bowler count 0
bat_count = 0
bow_count = 0

# set selection batsman 
lbl_player_selection.set("SELECT BATSMAN ("+str(bat_count)+" / 4)")


def select_bat(playername):
    global batsman_dict, bat_count, lbl_player_selection

    if bat_count < 4:
        if playername not in batsman_dict:
            batsman_dict[playername] = 0
            bat_count += 1
            # SELECT BATSMAN (0/4)
            lbl_player_selection.set("SELECT BATSMAN ("+str(bat_count)+" / 4)")
    else:
        print(batsman_dict)

# set selection bowler
lbl_bow_selection.set("SELECT BOWLER ("+str(bow_count)+" / 2)")

# function for select bowler
def select_ball(playername):
    global bowers_dict, bow_count, lbl_bow_selection
    if bow_count < 2:
        if playername not in bowers_dict:
            bowers_dict[playername] = 0
            bow_count += 1
            lbl_bow_selection.set("SELECT BOWLER ("+str(bow_count)+" / 2)")
    else:
        print(bowers_dict)


# ===================== reset game ===========================

def reset_game(stage):
    global my_team_var, my_team, opp_team_var, opp_team, team_selection_count
    global batsman_dict, bowers_dict, bat_count, bow_count
    if stage == 1:
        my_team = ""
        opp_team = ""
        my_team_var.set(my_team)
        opp_team_var.set(my_team)
        team_selection_count = 0
    if stage == 2:
        batsman_dict.clear()
        bowers_dict.clear()
        bat_count = 0
        bow_count = 0
        lbl_player_selection.set("SELECT BATSMAN ("+str(bat_count)+" / 4)")
        lbl_bow_selection.set("SELECT BOWLER ("+str(bow_count)+" / 2)")


count = 0   # for reset toss count

# display players list funtion

def display_player():
    global count
    toss_var.set("RESULT PENDING !")
    count = 0   # it will reset toss value
    if bat_count == 4 and bow_count == 2:
        MainFrame1.destroy()
        Info_lbl.configure(text="All Players")
        MainFrame2 = Frame(screen, bg='#2196f3', width=1350,
                           pady=10, padx=10, height=600, relief=RIDGE)
        MainFrame2.grid(row=2, column=0, sticky=S + N + E + W)

        # display in listbox
        listbox = Listbox(MainFrame2, font=('arial', 40, 'bold'),
                          height=6, width=27, fg="white", bg='#6200ea')
        listbox.grid(row=0, column=0, sticky=S + N + E + W)

        # display all batsman and bowlers in same listbox
        i = 1
        for k in batsman_dict.keys():
            listbox.insert(i, k)
            i += 1

        for k in bowers_dict.keys():
            listbox.insert(i, k)
            i += 1

        Myplayer_Frame = Frame(MainFrame2, bd=10, width=500,
                               height=600, pady=10, padx=10, bg='#42a5f5', relief=RIDGE)
        Myplayer_Frame.grid(row=0, column=2)

        btn = Button(Myplayer_Frame, text="BACK", font=('arial', 30, 'bold'),
                     height=3, width=20, fg="white", bg='#1565c0', command=lambda: startGame())
        btn.grid(row=2, column=0, padx=10, pady=10,
                 columnspan=10, sticky=S + N + E + W)

        btn = Button(Myplayer_Frame, text="TOSS", font=('arial', 30, 'bold'),
                     height=3, width=20, fg="white", bg='#1565c0', command=lambda: toss_time())
        btn.grid(row=4, column=0, padx=10, pady=10,
                 columnspan=10, sticky=S + N + E + W)



# ===============  TOSS TIME  ==================

toss_var = StringVar()  # toss variable declaration
MainFrame2 = Frame()


def toss_time():
    MainFrame1.destroy()
    Info_lbl.configure(text="TOSS")
    MainFrame2 = Frame(screen, bg='#2196f3', width=1350,
                       pady=10, padx=10, height=600, relief=RIDGE)
    MainFrame2.grid(row=2, column=0, sticky=S + N + E + W)

    LeftFrame = Frame(MainFrame2, bd=10, width=675, height=600,
                      pady=10, padx=10, bg='purple', relief=RIDGE)
    LeftFrame.grid(row=0, column=0)

    toss_result = Button(LeftFrame, text="RESULT PENDING !", textvariable=toss_var, font=(
        'arial', 20, 'bold'), height=3, width=12, fg="white", bg='#1565c0')
    toss_result.grid(row=0, column=0, padx=10, pady=10,
                     columnspan=2, sticky=S + N + E + W)

    btn_heads = Button(LeftFrame, text="HEADS", font=('arial', 30, 'bold'), height=3,
                       width=12, fg="white", bg='#1565c0', command=lambda: toss("h", btn_heads))
    btn_heads.grid(row=1, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn_tails = Button(LeftFrame, text="TAILS", font=('arial', 30, 'bold'), height=3,
                       width=12, fg="white", bg='#1565c0', command=lambda: toss('t', btn_tails))
    btn_tails.grid(row=1, column=1, padx=10, pady=10, sticky=S + N + E + W)

    RightFrame = Frame(MainFrame2, bd=15, width=690, height=600,
                       pady=10, padx=40, bg='#b39ddb', relief=RIDGE)
    RightFrame.grid(row=0, column=2)

    btn = Button(RightFrame, text="YOUR TEAM :", font=(
        'arial', 20, 'bold'), height=1, width=15, fg="white", bg='#311b92')
    btn.grid(row=0, column=0, padx=5, pady=10, sticky=S + N + E + W)

    btn = Button(RightFrame, text="OPP. TEAM  :", font=(
        'arial', 20, 'bold'), height=1, width=15, fg="white", bg='#311b92')
    btn.grid(row=1, column=0, padx=5, pady=10, sticky=S + N + E + W)

    btn = Button(RightFrame, text=my_team, font=('arial', 20, 'bold'),
                 height=1, bd=2, width=12, fg="#1565c0", bg='white')
    btn.grid(row=0, column=1, padx=5, pady=10,
             columnspan=5, sticky=S + N + E + W)

    btn = Button(RightFrame, text=opp_team, font=('arial', 20, 'bold'),
                 height=1, bd=2, width=12, fg="#1565c0", bg='white')
    btn.grid(row=1, column=1, padx=5, pady=10,
             columnspan=5, sticky=S + N + E + W)

    btn = Button(RightFrame, text="BACK", font=('arial', 30, 'bold'), height=1,
                 width=20, fg="white", bg='#1565c0', command=lambda: display_player())
    btn.grid(row=3, column=0, padx=10, pady=15,
             columnspan=10, sticky=S + N + E + W)

    btn = Button(RightFrame, text="PLAY GAME", font=('arial', 30, 'bold'), height=1,
                 width=20, fg="white", bg='#1565c0', command=lambda: playthegame())
    btn.grid(row=4, column=0, padx=10, pady=15,
             columnspan=10, sticky=S + N + E + W)

# setting toss value and winning team empty string variable 
toss_value = ""
toss_wining_team = ""
toss_var.set("RESULT PENDING !")

# function for toss
def toss(toss_choice, obj):
    global toss_value, toss_wining_team, count  # global variables declaration 

    # random choice for heads and tails

    toss_value = random.choice(['h', 't'])
    if count == 0:
        if toss_choice == toss_value:
            toss_wining_team = my_team
            toss_var.set(my_team+" won the toss and elected to bat first")
            obj.configure(bg="#00e676")
            count += 1
        else:
            toss_wining_team = opp_team
            toss_var.set(opp_team+" won the toss and elected to bat first")
            obj.configure(bg="#00e676")
            count += 1


# setting up string variables to handle widgets for match result 
match_info = StringVar()     # match_information
match_team = StringVar()     # match team handling
match_score = StringVar()    # match score handling
match_balls = StringVar()    # match balls handling 
match_display = StringVar()  # match commentry display

match_info.set("RESULT PENDING !")

# ============ Main game frame setup =====================

btnball=Button()
def playthegame():
    MainFrame2.destroy()
    Info_lbl.configure(text="SCORE BOARD")
    MainFrame3 = Frame(screen, bg='#2196f3', width=1350,
                       pady=10, padx=10, height=600, relief=RIDGE)
    MainFrame3.grid(row=2, column=0, sticky=S + N + E + W)

    LeftFrame = Frame(MainFrame3, bd=10, width=675, height=600,pady=10, padx=10, bg='purple', relief=RIDGE)
    LeftFrame.grid(row=0, column=0)

    btn_info = Button(LeftFrame, text="RESULT PENDING !", textvariable=match_info, font=('arial', 20, 'bold'), height=1, width=12, fg="white", bg='#1565c0')
    btn_info.grid(row=0, column=0, padx=10, pady=10,columnspan=3, sticky=S + N + E + W)

    btn_team = Button(LeftFrame, text="HEADS", textvariable=match_team, font=('arial', 30, 'bold'), height=2, width=8, fg="white", bg='#1565c0')
    btn_team.grid(row=1, column=0, padx=10, pady=10, sticky=S + N + E + W)

    btn_score = Button(LeftFrame, text="HEADS", textvariable=match_score, font=('arial', 30, 'bold'), height=2, width=8, fg="white", bg='#1565c0')
    btn_score.grid(row=1, column=1, padx=10, pady=10, sticky=S + N + E + W)

    btn_balls = Button(LeftFrame, text="HEADS", textvariable=match_balls, font=('arial', 30, 'bold'), height=2, width=8, fg="white", bg='#1565c0')
    btn_balls.grid(row=1, column=2, padx=10, pady=10, sticky=S + N + E + W)

    btn_lead = Button(LeftFrame, text="", font=('arial', 30, 'bold'),textvariable=match_display, height=1, width=8, fg="white", bg='#1565c0')
    btn_lead.grid(row=2, column=0, padx=10, pady=10,columnspan=3, sticky=S + N + E + W)

    RightFrame = Frame(MainFrame3, bd=15, width=690, height=600,pady=10, padx=40, bg='#b39ddb', relief=RIDGE)
    RightFrame.grid(row=0, column=2)

    btn = Button(RightFrame, text="YOUR TEAM :", font=('arial', 20, 'bold'), height=1, width=15, fg="white", bg='#311b92')
    btn.grid(row=0, column=0, padx=5, pady=10, sticky=S + N + E + W)

    btn = Button(RightFrame, text="OPP. TEAM  :", font=('arial', 20, 'bold'), height=1, width=15, fg="white", bg='#311b92')
    btn.grid(row=1, column=0, padx=5, pady=10, sticky=S + N + E + W)

    btn = Button(RightFrame, text=my_team, font=('arial', 20, 'bold'),height=1, bd=2, width=12, fg="#1565c0", bg='white')
    btn.grid(row=0, column=1, padx=5, pady=10,columnspan=5, sticky=S + N + E + W)

    btn = Button(RightFrame, text=opp_team, font=('arial', 20, 'bold'),height=1, bd=2, width=12, fg="#1565c0", bg='white')
    btn.grid(row=1, column=1, padx=5, pady=10,columnspan=5, sticky=S + N + E + W)

    btn = Button(RightFrame, text="RESET", font=('arial', 30, 'bold'), height=1,width=20, fg="white", bg='#1565c0', command=lambda: startGame())
    btn.grid(row=3, column=0, padx=10, pady=15,columnspan=10, sticky=S + N + E + W)

    btnball = Button(RightFrame, text="NEXT BALL", font=('arial', 30, 'bold'), height=1, width=20, fg="white", bg='#1565c0',command=lambda: match())
    btnball.grid(row=4, column=0, padx=10, pady=15,columnspan=10, sticky=S + N + E + W)

# setting up different ball values and 
ball_value=0
ball_2_value=0

# list for different score list generation
score_list=[1,"OUT",2,4,6,"OUT",2,4,6,1,"OUT","OUT",2,1]

# declaration for team score and opponent team score , remaining score and remaining ball
myteam_score=0
oppteam_score=0
rem_score=0
rem_ball=10

# Wicket declaration for opponent and user team
wicket=0
o_wicket=0

# match running logic
def match():
    global ball_value,ball_2_value,score_list,myteam_score,oppteam_score,rem_score,rem_ball,wicket,o_wicket
    if toss_wining_team == my_team:
        
        if ball_value < 10:
            ball_value += 1
            print("-----------------> ball 1 ", ball_value)
            s = random.choice(score_list)
            print("------------------> score ", s)
            if s == 1:
                myteam_score += 1
                #add_score(1)
                display_score_board("it's a Single", my_team, myteam_score, wicket, ball_value)
            elif s == 2:
                myteam_score += 2
                #add_score(2)
                display_score_board("it's a double", my_team, myteam_score, wicket, ball_value)
            elif s == 4:
                myteam_score += 4
                #add_score(4)
                display_score_board("it's a boundary", my_team, myteam_score, wicket, ball_value)
            elif s == 6:
                myteam_score += 6
                #add_score(6)
                display_score_board("it's a SIX ! ", my_team, myteam_score, wicket, ball_value)
            elif s == "OUT":
                wicket += 1
                if wicket == 3:
                    display_score_board("OOPS ! IT'S ALL OUT ! ", my_team, myteam_score, wicket, ball_value)
                    defending_score(opp_team, myteam_score+1, ball_2_value+10)
                    ball_value = 11
                else:
                    display_score_board("OOPS ! IT's a wicket !", my_team, myteam_score, wicket, ball_value)
            elif s == 0:
                #add_score(0)
                display_score_board("It's DOT BALL", my_team, myteam_score, wicket, ball_value)
            rem_score = myteam_score+1
        else:
            if ball_2_value < 10:
                ball_2_value += 1
                if rem_score <= 0:
                    winningscore(opp_team+" won the match ")
                    btnball.configure(state="disabled")
                    btnball.configure(text="GAME OVER")
                    ball_2_value = 11
                else:
                        rem_ball -= 1
                        print("-----------------> ball 2 ", rem_ball)
                        s = random.choice(score_list)
                        if s == 1:
                            oppteam_score += 1
                            display_score_board("it's a Single", opp_team, oppteam_score, o_wicket, ball_2_value)
                            rem_score -= 1
                            defending_score(opp_team, rem_score, rem_ball)
                        elif s == 2:
                            oppteam_score += 2
                            display_score_board("it's a double", opp_team, oppteam_score, o_wicket, ball_2_value)
                            rem_score -= 2
                            defending_score(opp_team, rem_score, rem_ball)
                        elif s == 4:
                            oppteam_score += 4
                            display_score_board("it's a boundary", opp_team, oppteam_score, o_wicket, ball_2_value)
                            rem_score -= 4
                            defending_score(opp_team, rem_score, rem_ball)
                        elif s == 6:
                            oppteam_score += 6
                            display_score_board("it's a SIX ! ", opp_team, oppteam_score, o_wicket, ball_2_value)
                            rem_score -= 6
                            defending_score(opp_team, rem_score, rem_ball)
                        elif s == "OUT":
                            o_wicket += 1
                            if o_wicket == 3:
                                display_score_board("OOPS ! ITS ALL OUT ! ", opp_team, oppteam_score, o_wicket, ball_2_value)
                            
                                if oppteam_score > myteam_score:
                                    winningscore(opp_team+" won the match ")
                                    btnball.configure(state="disabled")
                                    ball_2_value = 11
                                else:
                                    winningscore(my_team+" won the match ")
                                    btnball.configure(state="disabled")
                                    ball_2_value = 11
                            else:
                                display_score_board("OOPS ! IT's a wicket !", opp_team, oppteam_score, o_wicket, ball_2_value)
                                defending_score(opp_team, rem_score, rem_ball)
                        elif s == 0:
                            display_score_board("It's DOT BALL", opp_team, oppteam_score, o_wicket, ball_2_value)
                            defending_score(opp_team, rem_score, rem_ball)
            else:
                if oppteam_score > myteam_score:
                    winningscore(opp_team+" won the match ")
                    btnball.configure(state="disabled")
                    btnball.configure(text="GAME OVER")
                else:
                    winningscore(my_team+" won the match ")
                    btnball.configure(state="disabled")
                    btnball.configure(text="GAME OVER")
    else:
        if ball_value<10:
            ball_value+=1
            print("-----------------> ball 1 ",ball_value)
            s=random.choice(score_list)
            print("------------------> score ",s)
            if s==1:
                oppteam_score+=1
                display_score_board("it's a Single",opp_team,oppteam_score,wicket,ball_value)
            elif s==2:
                oppteam_score+=2
                display_score_board("it's a double",opp_team,oppteam_score,wicket,ball_value)
            elif s==4:
                oppteam_score+=4
                display_score_board("it's a boundary",opp_team,oppteam_score,wicket,ball_value)
            elif s==6:
                oppteam_score+=6
                display_score_board("it's a SIX ! ",opp_team,oppteam_score,wicket,ball_value)
            elif s=="OUT":
                wicket+=1
                if wicket == 3:
                    display_score_board("OOPS ! IT'S ALL OUT ! ",opp_team,oppteam_score,wicket,ball_value)
                    defending_score(my_team,oppteam_score+1,ball_2_value+10)
                    ball_value=11
                else:
                    display_score_board("OOPS ! IT's a wicket !",opp_team,oppteam_score,wicket,ball_value)
            elif s==0:
                display_score_board("It's DOT BALL",opp_team,oppteam_score,wicket,ball_value)     
            rem_score=oppteam_score+1        
        else:
            if ball_2_value<10:
                if rem_score<=0:
                    winningscore(my_team+" won the match ")
                    btnball.configure(state="disabled")
                    btnball.configure(text="GAME OVER")
                    ball_2_value=11
                else:
                    ball_2_value+=1
                    rem_ball-=1
                    print("-----------------> ball 2 ",rem_ball)
                    s=random.choice(score_list)
                    if s==1:
                        myteam_score+=1
                        display_score_board("it's a Single",my_team,myteam_score,o_wicket,ball_2_value)
                        rem_score-=1
                        defending_score(my_team,rem_score,rem_ball)
                    elif s==2:
                        myteam_score+=2
                        display_score_board("it's a double",my_team,myteam_score,o_wicket,ball_2_value)
                        rem_score-=2
                        defending_score(my_team,rem_score,rem_ball)
                    elif s==4:
                        myteam_score+=4
                        display_score_board("it's a boundary",my_team,myteam_score,o_wicket,ball_2_value)
                        rem_score-=4
                        defending_score(my_team,rem_score,rem_ball)
                    elif s==6:
                        myteam_score+=6
                        display_score_board("it's a SIX ! ",my_team,myteam_score,o_wicket,ball_2_value)
                        rem_score-=6
                        defending_score(my_team,rem_score,rem_ball)
                    elif s=="OUT":
                        o_wicket+=1
                        if o_wicket == 3:
                            display_score_board("OOPS ! ITS ALL OUT ! ",my_team,myteam_score,o_wicket,ball_2_value)
                            if oppteam_score>myteam_score:
                                winningscore(opp_team+" won the match ")
                                btnball.configure(state="disabled")
                                btnball.configure(text="GAME OVER")
                                ball_2_value=11
                            else:
                                winningscore(my_team+" won the match ")
                                btnball.configure(state="disabled")
                                btnball.configure(text="GAME OVER")
                                ball_2_value=11
                        else:
                            display_score_board("OOPS ! IT's a wicket !",my_team,myteam_score,o_wicket,ball_2_value)
                            defending_score(my_team,rem_score,rem_ball)
                    elif s==0:
                        display_score_board("It's DOT BALL",my_team,myteam_score,o_wicket,ball_2_value)
                        defending_score(my_team,rem_score,rem_ball)
            else:
                if oppteam_score>myteam_score:
                    winningscore(opp_team+" won the match ")
                    btnball.configure(state="disabled")
                    btnball.configure(text="GAME OVER")
                else:
                    winningscore(my_team+" won the match ")
                    btnball.configure(text="GAME OVER")
                    btnball.configure(state="disabled")

# function for display score board
def display_score_board(commentry,teamname,score,wicket,balls):
    match_info.set(commentry)
    match_team.set(teamname)
    match_score.set(str(score)+" / "+str(wicket))
    match_balls.set(str(balls)+" ball ")

# function for defending score display
def defending_score(teamname,score,no_of_ball):
    if score<0:
        score=0
        match_display.set(str(teamname)+" needs "+str(score)+" runs in  "+str(no_of_ball)+" balls ")
    else:
        match_display.set(str(teamname)+" needs "+str(score)+" runs in  "+str(no_of_ball)+" balls ")

# function for winning team declaration
def winningscore(msg):
    match_display.set(str(msg))

# runnning the python Tkinter event loop
screen.mainloop()
