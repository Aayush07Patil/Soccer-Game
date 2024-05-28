import time
import random
import pandas as pd

from tkinter import *
import tkinter as tk



def app():
    
    
    bg_colour = '#2f3030'
    fg_colour = '#419977'
    window = tk.Tk()
    window.title('Soccer Manager')
    window.geometry("700x500")
    window.minsize(350,400)
    #window.maxsize(600,650)
    #small_icon = tk.PhotoImage(file="taxi_small.png")
    #large_icon = tk.PhotoImage(file="taxi_big.png")
    #window.iconphoto(False, large_icon, small_icon)
    window.configure(bg= bg_colour)
    window.attributes('-fullscreen',True)
    
    frame_main_menu = Frame(bg = bg_colour)
    #frame_main_menu.place(relx=0.5,rely=0.5,anchor=CENTER)
    frame_teams_select = Frame(bg = bg_colour)
    frame_teams_select.grid(sticky=NSEW)
    
    
    # Main Menu Frame 
    label_title = Label(frame_main_menu,text = 'SOCCER MANAGER', bg = bg_colour,fg = fg_colour,font=("Arial",45,"bold"))
    label_title.pack(pady=20)
    
    button_start_game = Button(frame_main_menu,text='START GAME',width=15,font=("Arial",14),bg= fg_colour,fg="white")
    button_start_game.pack(pady=5,ipadx=50,ipady=5)

    button_options = Button(frame_main_menu,text='OPTIONS',width=15,font=("Arial",14),bg= fg_colour,fg="white")
    button_options.pack(pady=5,ipadx=50,ipady=5)

    button_quit = Button(frame_main_menu,text='QUIT',width=15,font=("Arial",14),bg= fg_colour,fg="white",command=quit)
    button_quit.pack(pady=5,ipadx=50,ipady=5)
    
    # Team Select Frame
    
    window.columnconfigure(0,weight=1)
    window.columnconfigure(1,weight=1)
    window.rowconfigure(0,weight=1)
    window.rowconfigure(1,weight=3)
    window.rowconfigure(2,weight=1)
    
    
    
    label_team_select = Label(frame_teams_select, text= 'TEAM SELECT',bg = bg_colour,fg = fg_colour, font=("Arial",45,"bold"))
    label_team_select.grid(row=0,columnspan=2,sticky=NSEW)
    
    frame_player_team_select = Frame(frame_teams_select, height = 700, width = 300,bg = 'white')
    frame_player_team_select.grid(row=1,column=0,sticky=NSEW)
    
    frame_opposition_team_select = Frame(frame_teams_select, height = 700, width = 300, bg = 'white')
    frame_opposition_team_select.grid(row= 1, column= 1,sticky=NSEW)   
    
    button_league_player = Button(frame_player_team_select,text='<',width=15,font=("Arial",18),bg= fg_colour,fg="white")
    button_league_player.grid()
    
    button_league_opposition = Button(frame_opposition_team_select,text='<',width=15,font=("Arial",18),bg= fg_colour,fg="white")
    button_league_opposition.grid()
    
    button_back = Button(frame_teams_select,text='Back',width=15,font=("Arial",14),bg= fg_colour,fg="white",command=quit)
    button_back.grid(row=2,column=1, sticky=NSEW)
    
    
    window.mainloop()
    
    
if __name__ == "__main__":
    app()