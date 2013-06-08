'''
Created on 2013-06-06

@author: Felanrod
'''
from Tkinter import *

#create the MyApp Class
class MyApp:
    #define the attributes of the class
    def __init__(self, parent):
        self.myParent = parent
        #creates a frame whose parent is root
        self.myContainer1 = Frame(parent, height=600, width=480)
        #pack the frame - show it on the screen
        self.myContainer1.pack_propagate(0)
        self.myContainer1.pack()
        
        #the button1 attributes
        self.bSpin = Button(self.myContainer1)
        self.bSpin.configure(text="SPIN!", background= "green", justify=RIGHT, pady=200, padx=10)
        #display button1
        self.bSpin.pack()
        self.bSpin.focus_force() #forces the focus to go to the OK button
        #Bind button1 with button1Click
        self.bSpin.bind("<Button-1>", self.bSpinClick)
        self.bSpin.bind("<Return>", self.bSpinClick) #bind return keypress

        #the button2 attributes
        self.bBet = Button(self.myContainer1)
        self.bBet.configure(text="BET!", background= "red", justify=LEFT, pady=200, padx=10)
        #display button2
        self.bBet.pack()
        #Bind button2 with button2Click
        self.bBet.bind("<Button-1>", self.bBetClick)
        self.bBet.bind("<Return>", self.bBetClick) #bind return keypress

    #change colour of buttons
    def bSpinClick(self, event):
        report_event(event) #send event information to be printed
        if self.bSpin["background"] == "green":
            self.bSpin["background"] = "yellow"
        else:
            self.bSpin["background"] = "green"

    #close GUI
    def bBetClick(self, event):
        report_event(event) #send event information to be printed
        self.myParent.destroy()

#report event function
def report_event(event): 
    """Print a description of an event, based on its attributes.
    """
    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print("Time:", str(event.time)) #print the time of the event and its type
    print("EventType=" + str(event.type), \
    event_name[str(event.type)],\
        "EventWidgetId=" + str(event.widget), \
        "EventKeySymbol=" + str(event.keysym))

def main():
    #create a top-level window
    root = Tk()
    #call the MyApp class
    myapp = MyApp(root)
    #execute the mainloop method of the "root" object
    root.mainloop()

if __name__ == "__main__": main()