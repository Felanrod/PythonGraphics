'''
Created on 2013-06-07

@author: Felanrod
'''
# import statements
from Tkinter import *
import tkMessageBox
import random
#from PIL import Image, ImageTk

# The main Class of the application
class PlaceGeometryApp:
    
    bet = 0
    betWon = ""
    cash = 1000
    jackpot = 100
    jackpotText = "$" + str(jackpot)
    jWon = "LOST"
    jackpotWon = "JACKPOT"
    betText =  "YOUR BET:$" + str(bet)
    cashText = "YOU HAVE:$" + str(cash)
    
    #Reel Images
    rImages = ["goomba.gif", "energy.gif", "master_sword_slot.gif",
               "starman.gif", "megaman.gif", "triforce.gif", "one_up.gif", "mario.gif"]
    rImageRef = ["Goomba", "Energy", "Sword", "Starman", "MMLife", "Triforce", "1Up", "Mario"]
    
    goomba = "goomba.gif"
    energy = "energy.gif"
    sword = "master_sword_slot.gif"
    starman = "starman.gif"
    mmLife = "megaman.gif"
    triforce = "triforce.gif"
    oneUp = "one_up.gif"
    mario = "mario.gif"
    
    def __init__(self, master=None):
        
        
        
        # Setup Application Fonts
        self.FixedSysFont = "-family Fixedsys -size 20 -weight normal -slant roman -underline 0 -overstrike 0"

        # Display the Slot Machine Image on a Canvas Panel ------------------
        self.bg_panel = Canvas(master, width=640, height=480, bg="white")
        self.bg_panel.pack(expand=YES,fill=BOTH)       
        #self.bg_img = Image.open("painting.bmp")
        #self.bg_imgTk = ImageTk.PhotoImage(self.bg_img)
        #self.bg_panel.create_image(0, 0, image = self.bg_imgTk, anchor = NW)
        
        # Display Jackpot
        self.myJackpotWon = Label (self.bg_panel)
        self.myJackpotWon.place(x=221,y=5,height=35,width=200)
        self.myJackpotWon.configure(background="#000000")
        self.myJackpotWon.configure(borderwidth="0")
        self.myJackpotWon.configure(font=self.FixedSysFont)
        self.myJackpotWon.configure(foreground="#00ff00")
        self.myJackpotWon.configure(anchor="n")
        self.myJackpotWon.configure(text=self.jackpotWon)
        
        # Display my Label - this will change when I click on the Buttons
        self.myJackpot = Label (self.bg_panel)
        self.myJackpot.place(x=221,y=50,height=35,width=200)
        self.myJackpot.configure(background="#000000")
        self.myJackpot.configure(borderwidth="0")
        self.myJackpot.configure(font=self.FixedSysFont)
        self.myJackpot.configure(foreground="#00ff00")
        self.myJackpot.configure(anchor="n")
        self.myJackpot.configure(text=self.jackpotText)
        
        # Display You Won
        self.youWon = Label (self.bg_panel)
        self.youWon.place(x=191,y=95,height=35,width=260)
        self.youWon.configure(background="#000000")
        self.youWon.configure(borderwidth="0")
        self.youWon.configure(font=self.FixedSysFont)
        self.youWon.configure(foreground="#00ff00")
        self.youWon.configure(anchor="n")
        self.youWon.configure(text=self.betWon)

        # Display the Reset button
        self.ResetButton = Button(self.bg_panel)
        self.ResetButton.place(x=430, y=5, height=80, width=200)
        self.ResetButton.configure(borderwidth="0")
        self.ResetButton_img = PhotoImage(file="reset.gif")
        self.ResetButton.configure(image=self.ResetButton_img)
        self.ResetButton.configure(cursor="hand2")
        self.ResetButton.bind("<Button-1>",self.ResetButtonClick)

        # Display the Power button
        self.PowerButton = Button(self.bg_panel)
        self.PowerButton.place(x=10, y=5, height=80, width=200)
        self.PowerButton.configure(borderwidth="0")
        self.PowerButton_img = PhotoImage(file="power.gif")
        self.PowerButton.configure(image=self.PowerButton_img)
        self.PowerButton.configure(cursor="hand2")
        self.PowerButton.bind("<Button-1>",self.PowerButtonClick)
        
        # Display Reel 1 Label
        self.reel1 = Label (self.bg_panel)
        self.reel1.place(x=85,y=150,height=100,width=100)
        #self.reel1Label_img = PhotoImage(file=goomba)
        self.reel1Label_img = PhotoImage(file=self.rImages[3])
        self.reel1.configure(image=self.reel1Label_img)
        
        # Display Reel 2 Label
        self.reel2 = Label (self.bg_panel)
        self.reel2.place(x=270,y=150,height=100,width=100)
        #self.reel2Label_img = PhotoImage(file=goomba)
        self.reel2Label_img = PhotoImage(file=self.rImages[3])
        self.reel2.configure(image=self.reel2Label_img)
        
        # Display Reel 3 Label
        self.reel3 = Label (self.bg_panel)
        self.reel3.place(x=455,y=150,height=100,width=100)
        #self.reel3Label_img = PhotoImage(file=goomba)
        self.reel3Label_img = PhotoImage(file=self.rImages[3])
        self.reel3.configure(image=self.reel3Label_img)
        
        # Display the Bet 50 button
        self.bet50 = Button(self.bg_panel)
        self.bet50.place(x=40, y=275, height=80, width=80)
        self.bet50.configure(borderwidth="0")
        self.bet50Button_img = PhotoImage(file="coin_block.gif")
        self.bet50.configure(image=self.bet50Button_img)
        self.bet50.configure(cursor="hand2")
        self.bet50.bind("<Button-1>",self.Bet50ButtonClick)
        
        # Display Bet 50 Label
        self.lblBet50 = Label (self.bg_panel)
        self.lblBet50.place(x=38,y=365,height=60,width=85)
        self.lblBet50Label_img = PhotoImage(file="bet_50.gif")
        self.lblBet50.configure(image=self.lblBet50Label_img)

        # Display the Bet 100 button
        self.bet100 = Button(self.bg_panel)
        self.bet100.place(x=160, y=275, height=80, width=80)
        self.bet100.configure(borderwidth="0")
        self.bet100Button_img = PhotoImage(file="coin_block.gif")
        self.bet100.configure(image=self.bet100Button_img)
        self.bet100.configure(cursor="hand2")
        self.bet100.bind("<Button-1>",self.Bet100ButtonClick)
        
        # Display Bet 100 Label
        self.lblBet100 = Label (self.bg_panel)
        self.lblBet100.place(x=158,y=365,height=60,width=85)
        self.lblBet100Label_img = PhotoImage(file="bet_100.gif")
        self.lblBet100.configure(image=self.lblBet100Label_img)
        
        # Display the Bet 200 button
        self.bet200 = Button(self.bg_panel)
        self.bet200.place(x=400, y=275, height=80, width=80)
        self.bet200.configure(borderwidth="0")
        self.bet200Button_img = PhotoImage(file="coin_block.gif")
        self.bet200.configure(image=self.bet200Button_img)
        self.bet200.configure(cursor="hand2")
        self.bet200.bind("<Button-1>",self.Bet200ButtonClick)
        
        # Display Bet 200 Label
        self.lblBet200 = Label (self.bg_panel)
        self.lblBet200.place(x=398,y=365,height=60,width=85)
        self.lblBet200Label_img = PhotoImage(file="bet_200.gif")
        self.lblBet200.configure(image=self.lblBet200Label_img)
        
        # Display the Bet All button
        self.betAll = Button(self.bg_panel)
        self.betAll.place(x=520, y=275, height=80, width=80)
        self.betAll.configure(borderwidth="0")
        self.betAllButton_img = PhotoImage(file="coin_block.gif")
        self.betAll.configure(image=self.betAllButton_img)
        self.betAll.configure(cursor="hand2")
        self.betAll.bind("<Button-1>",self.BetAllButtonClick)
        
        # Display Bet All Label
        self.lblBetAll = Label (self.bg_panel)
        self.lblBetAll.place(x=518,y=365,height=60,width=85)
        self.lblBetAllLabel_img = PhotoImage(file="bet_all.gif")
        self.lblBetAll.configure(image=self.lblBetAllLabel_img)
        
        # Display the Spin button
        self.spin = Button(self.bg_panel)
        self.spin.place(x=270, y=365, height=105, width=100)
        self.spin.configure(borderwidth="0")
        self.spinButton_img = PhotoImage(file="spin.gif")
        self.spin.configure(image=self.spinButton_img)
        self.spin.configure(cursor="hand2")
        self.spin.bind("<Button-1>",self.SpinButtonClick)
        
        # Display my Money
        self.myMoney = Label (self.bg_panel)
        self.myMoney.place(x=10,y=435,height=35,width=250)
        self.myMoney.configure(background="#000000")
        self.myMoney.configure(borderwidth="0")
        self.myMoney.configure(font=self.FixedSysFont)
        self.myMoney.configure(foreground="#ff0000")
        self.myMoney.configure(anchor="n")
        self.myMoney.configure(text=self.cashText)
        
        # Display my Bet
        self.myBet = Label (self.bg_panel)
        self.myBet.place(x=380,y=435,height=35,width=250)
        self.myBet.configure(background="#000000")
        self.myBet.configure(borderwidth="0")
        self.myBet.configure(font=self.FixedSysFont)
        self.myBet.configure(foreground="#ff0000")
        self.myBet.configure(anchor="n")
        self.myBet.configure(text=self.betText)

        
    # Event Handlers Begin Here -----------------------------------------
    
    # Reset Label    
    def ResetButtonClick(self,event):
        if tkMessageBox.askokcancel("Reset Pressed", "Are you sure you want to Reset?"):
            self.bet = 0
            self.myLabel.configure(text="unclicked")
            
    # Terminate Application
    def PowerButtonClick(self,event):
        if tkMessageBox.askokcancel("Power Off?", "Are you sure you want to Quit?"):
            sys.exit()
            
    # Change the label when the Click Me button is pressed
    def ClickMeButtonClick(self,event):
        self.myLabel.configure(text="Clicked!!")
        
    
    # Make Bet $50
    def Bet50ButtonClick(self,event):
        #self.myBet.configure(text="YOUR BET:$50")
        if self.cash - 50 >= 0:
            self.bet = 50
            self.ChangeBet()
        else:
            tkMessageBox.showinfo("You're Broke!", "You can't bet that much!")
    
    # Make Bet $100
    def Bet100ButtonClick(self,event):
        if self.cash - 100 >= 0:
            self.bet = 100
            self.ChangeBet()
        else:
            tkMessageBox.showinfo("You're Broke!", "You can't bet that much!")
        
    # Make Bet $200
    def Bet200ButtonClick(self,event):
        if self.cash - 200 >= 0:
            self.bet = 200
            self.ChangeBet()
        else:
            tkMessageBox.showinfo("You're Broke!", "You can't bet that much!")
    
    # Make Bet All
    def BetAllButtonClick(self,event):
        if self.cash != 0:
            self.bet = self.cash
            self.ChangeBet()
        else:
            tkMessageBox.showinfo("You're Broke!", "You have no more money!!!")
        
    
    def ChangeBet(self):
        self.betText = "YOUR BET:$" + str(self.bet)
        self.myBet.configure(text=self.betText)
        
    def UpdateReels(self):
        self.reel1.configure(image=self.reel1Label_img)
        self.reel2.configure(image=self.reel2Label_img)
        self.reel3.configure(image=self.reel3Label_img)
        
    def UpdateJackpot(self):
        self.myJackpotWon.configure(text=self.jackpotWon)
        self.myJackpot.configure(text=self.jackpotText)
    
    def UpdateMoney(self):
        self.youWon.configure(text=self.betWon)
        self.ChangeBet()
        self.cashText = "YOU HAVE:$" + str(self.cash)
        self.myMoney.configure(text=self.cashText)

    
    def Reels(self):
        """ When this function is called it determines the Bet_Line results.
            e.g. Triforce - Starman - Sword """
            
        # [0]Fruit, [1]Fruit, [2]Fruit
        Bet_Line = [" "," "," "]
        Outcome = [0,0,0]
        
        # Spin those reels
        for spin in range(3):
            Outcome[spin] = random.randrange(1,65,1)
            # Spin those Reels!
            if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
                Bet_Line[spin] = "Goomba"
            if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
                Bet_Line[spin] = "Energy"
            if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
                Bet_Line[spin] = "Sword"
            if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
                Bet_Line[spin] = "Starman"
            if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
                Bet_Line[spin] = "MMLife"
            if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
                Bet_Line[spin] = "Triforce"
            if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
                Bet_Line[spin] = "1Up"  
            if Outcome[spin] == 64:                         # 1.56%  Chance
                Bet_Line[spin] = "Mario"    
    
        
        return Bet_Line

    def is_number(self, Bet):
        """ This function Checks if the Bet entered by the user is a valid number """
        try:
            int(Bet)
            return True
        except ValueError:
            print("Please enter a valid number or Q to quit")
            return False
    
    def SpinButtonClick(self,event):
        """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
            It then calls the Reels function which generates the random Bet Line results.
            It calculates if the player wins or loses the spin.
            It returns the Player's Money and the Current Jackpot to the main function """
        if self.cash != 0:
            self.cash -= self.bet
            self.jackpot += (int(self.bet*.15)) # 15% of the player's bet goes to the jackpot
            self.jackpotText = "$" + str(self.jackpot)
            self.myJackpot.configure(text=self.jackpotText)
            win = False
            gameReel = self.Reels()
            #Fruits = gameReel[0] + " - " + gameReel[1] + " - " + gameReel[2]
            
            for reel in range(3):
                for images in range(7):
                    if gameReel[reel] == self.rImageRef[images]:
                        if reel == 0:
                            self.reel1Label_img = PhotoImage(file=self.rImages[images])
                        elif reel == 1:
                            self.reel2Label_img = PhotoImage(file=self.rImages[images])
                        elif reel == 2:
                            self.reel3Label_img = PhotoImage(file=self.rImages[images])
                            
            self.UpdateReels()
                    
            
            # Match 3
            if gameReel.count("Energy") == 3:
                winnings,win = self.bet*20,True
            elif gameReel.count("Sword") == 3:
                winnings,win = self.bet*30,True
            elif gameReel.count("Starman") == 3:
                winnings,win = self.bet*40,True
            elif gameReel.count("MMLife") == 3:
                winnings,win = self.bet*100,True
            elif gameReel.count("Triforce") == 3:
                winnings,win = self.bet*200,True
            elif gameReel.count("1Up") == 3:
                winnings,win = self.bet*300,True
            elif gameReel.count("Mario") == 3:
                winnings,win = self.bet*1000,True
            # Match 2 and 1 of same type
            elif gameReel.count("Goomba") == 0:
                if gameReel.count("Energy") == 2:
                    if gameReel.count("MMLife") == 1:
                        winnings,win = self.bet*35,True
                if gameReel.count("Sword") == 2:
                    if gameReel.count("Triforce") == 1:
                        winnings,win = self.bet*45,True
                elif gameReel.count("Starman") == 2:
                    if gameReel.count("1Up") == 1:
                        winnings,win = self.bet*55,True
                elif gameReel.count("MMLife") == 2:
                    if gameReel.count("Energy") == 1:
                        winnings,win = self.bet*50,True
                elif gameReel.count("Triforce") == 2:
                    if gameReel.count("Sword") == 1:
                        winnings,win = self.bet*60,True
                elif gameReel.count("1Up") == 2:
                    if gameReel.count("Starman") == 1:
                        winnings,win = self.bet*150,True
                elif gameReel.count("Mario") == 2:
                    winnings,win = self.bet*50,True
            
                # Match Lucky Mario
                elif gameReel.count("Mario") == 1:
                    winnings, win = self.bet*30,True
                    
                
                elif gameReel.count("Energy") == 1:
                    if gameReel.count("Sword") == 1:
                        if gameReel.count("Starman") == 1:
                            winnings, win = self.bet*25,True
                elif gameReel.count("MMLife") == 1:
                    if gameReel.count("Triforce") == 1:
                        if gameReel.count("1Up") == 1:
                            winnings, win = self.bet*250,True
                    
                else:
                    winnings, win = self.bet,True
            if win:    
                #print(Fruits + "\n" + "You Won $ " + str(int(winnings)) + "!!! \n")
                self.cash += int(winnings)
                self.betWon = "YOU WON $" + str(winnings)
                
                
            
                # Jackpot 1 in 450 chance of winning
                jackpot_try = random.randrange(1,51,1)
                jackpot_win = random.randrange(1,51,1)
                if  jackpot_try  == jackpot_win:
                    self.jackpotWon = "JACKPOT WON!"
                    self.cash += self.jackpot
                    self.jackpot = 100
                    self.jackpotText = "$" + str(self.jackpot)
                elif jackpot_try != jackpot_win:
                    self.jackpotWon = "JACKPOT LOST"
                self.UpdateJackpot()
            # No win
            else:
                self.betWon = "YOU LOST!!!"
            
            self.bet = 0
            self.UpdateMoney()
                #print(Fruits + "\nPlease try again. \n")
            
            #return Player_Money, Jack_Pot, win
# The main function    
def main():
    
    #Starting point when module is the main routine.
    window = Tk()
    # Remove minimize and maximize buttons from window toolbar
    window.attributes("-toolwindow", True) 
    window.title('Place Geometry Manager Example')
    # Initial Window Geometry
    window.geometry('640x480+532+0')
    #prevent application window from changing size
    window.minsize(width=640,height=480)
    window.maxsize(width=640,height=480)

    # instatiate myApp class and kick off the application
    myApp = PlaceGeometryApp(window)
    # start the application - Display the Top Level window Container
    window.mainloop()
    """ The Main function that runs the game loop """
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    # Flag to initiate the game loop
    KeepGoing = True
    
    while KeepGoing == True:
        win = 0
        # Give the player some money if he goes broke
        if Player_Money <1:
            input("You have no more money. Here is $500 \nPress Enter\n")
            Player_Money = 500
        
        # User Input
        Prompt = raw_input(" Place Your Bet ! \n Jackpot $ " + str(Jack_Pot) + "\n Money $ " + str(Player_Money) + "\n Q = quit \n")
        if Prompt  == "q" or Prompt  == "Q":
            KeepGoing = False
            break
        
        if Prompt == "" and Turn >1:
            self.bet = Prev_Bet
            print("Using Previous Bet")
            if self.bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
            elif self.bet <= Player_Money:
                Turn +=1
                Prev_Bet = self.bet
                Player_Money, Jack_Pot, win = pullthehandle(self.bet, Player_Money, Jack_Pot)
        
        elif is_number(Prompt ):
            self.bet = int(Prompt )
            # not enough money
            if self.bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
                
            # Let's Play
            elif self.bet <= Player_Money:
                Turn +=1
                Prev_Bet = self.bet
                Player_Money, Jack_Pot, win = pullthehandle(self.bet, Player_Money, Jack_Pot)
        
        # determine win/loss ratio for debugging purposes
        if win:
            win_number += 1
        else:
            loss_number += 1
        win_ratio = "{:.2%}".format(win_number / Turn)
        print("Wins: " + str(win_number) + "\nLosses: " + str(loss_number) + "\nWin Ratio: " + win_ratio + "\n")           
                
    
    #The End
    print("- Program Terminated -")

if __name__ == '__main__': main()