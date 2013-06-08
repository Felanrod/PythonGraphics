# import statements
from Tkinter import *
import tkMessageBox
#from PIL import Image, ImageTk

# The main Class of the application
class PlaceGeometryApp:
    def __init__(self, master=None):
                
        # Setup Application Fonts
        self.FixedSysFont = "-family Fixedsys -size 20 -weight normal -slant roman -underline 0 -overstrike 0"

        # Display the Slot Machine Image on a Canvas Panel ------------------
        self.bg_panel = Canvas(master, width=640, height=480, bg="white")
        self.bg_panel.pack(expand=YES,fill=BOTH)       
        #self.bg_img = Image.open("painting.bmp")
        #self.bg_imgTk = ImageTk.PhotoImage(self.bg_img)
        #self.bg_panel.create_image(0, 0, image = self.bg_imgTk, anchor = NW)
        
        # Display my Label - this will change when I click on the Buttons
        self.myLabel = Label (self.bg_panel)
        self.myLabel.place(x=221,y=27,height=35,width=200)
        self.myLabel.configure(background="#000000")
        self.myLabel.configure(borderwidth="0")
        self.myLabel.configure(font=self.FixedSysFont)
        self.myLabel.configure(foreground="#ff0000")
        self.myLabel.configure(anchor="n")
        self.myLabel.configure(text="unclicked")

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
        self.reel1Label_img = PhotoImage(file="starman.gif")
        self.reel1.configure(image=self.reel1Label_img)
        
        # Display Reel 2 Label
        self.reel2 = Label (self.bg_panel)
        self.reel2.place(x=270,y=150,height=100,width=100)
        self.reel2Label_img = PhotoImage(file="starman.gif")
        self.reel2.configure(image=self.reel2Label_img)
        
        # Display Reel 3 Label
        self.reel3 = Label (self.bg_panel)
        self.reel3.place(x=455,y=150,height=100,width=100)
        self.reel3Label_img = PhotoImage(file="starman.gif")
        self.reel3.configure(image=self.reel3Label_img)
        
        # Display the Bet 50 button
        self.bet50 = Button(self.bg_panel)
        self.bet50.place(x=40, y=275, height=80, width=80)
        self.bet50.configure(borderwidth="0")
        self.bet50Button_img = PhotoImage(file="coin_block.gif")
        self.bet50.configure(image=self.bet50Button_img)
        self.bet50.configure(cursor="hand2")
        self.bet50.bind("<Button-1>",self.ClickMeButtonClick)
        
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
        self.bet100.bind("<Button-1>",self.ClickMeButtonClick)
        
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
        self.bet200.bind("<Button-1>",self.ClickMeButtonClick)
        
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
        self.betAll.bind("<Button-1>",self.ClickMeButtonClick)
        
        # Display Bet All Label
        self.lblBetAll = Label (self.bg_panel)
        self.lblBetAll.place(x=518,y=365,height=60,width=85)
        self.lblBetAllLabel_img = PhotoImage(file="bet_all.gif")
        self.lblBetAll.configure(image=self.lblBetAllLabel_img)
        
        # Display the Spin button
        self.spin = Button(self.bg_panel)
        self.spin.place(x=262, y=365, height=105, width=100)
        self.spin.configure(borderwidth="0")
        self.spinButton_img = PhotoImage(file="spin.gif")
        self.spin.configure(image=self.spinButton_img)
        self.spin.configure(cursor="hand2")
        self.spin.bind("<Button-1>",self.ClickMeButtonClick)

        
    # Event Handlers Begin Here -----------------------------------------
    
    # Reset Label    
    def ResetButtonClick(self,event):
        if tkMessageBox.askokcancel("Reset Pressed", "Are you sure you want to Reset?"):
            self.myLabel.configure(text="unclicked")
            
    # Terminate Application
    def PowerButtonClick(self,event):
        if tkMessageBox.askokcancel("Power Off?", "Are you sure you want to Quit?"):
            sys.exit()
            
    # Change the label when the Click Me button is pressed
    def ClickMeButtonClick(self,event):
        self.myLabel.configure(text="Clicked!!")


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

if __name__ == '__main__': main()