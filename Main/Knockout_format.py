import customtkinter as Ct
import tkinter as tk
import algorithms 
import shelve
import FUNC
import openpyxl

data_file='INDOOR.db'

def match_format(page):
#R016
    RO16_1 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_1.place(relx=0.02, rely=0.05)

    RO16_2 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold'),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_2.place(relx=0.02, rely=0.15)

    RO16_3 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    RO16_3.place(relx=0.02, rely=0.28)


    RO16_4 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    RO16_4.place(relx=0.02, rely=0.38)


    RO16_5 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_5.place(relx=0.02, rely=0.51)

    RO16_6 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_6.place(relx=0.02, rely=0.61)

    RO16_7 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_7.place(relx=0.02, rely=0.74)


    RO16_8 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_8.place(relx=0.02, rely=0.85)

    RO16_9 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    RO16_9.place(relx=0.85, rely=0.05)

    RO16_10 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_10.place(relx=0.85, rely=0.15)

    RO16_11 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_11.place(relx=0.85, rely=0.28)


    RO16_12 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    RO16_12.place(relx=0.85, rely=0.38)


    RO16_13 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_13.place(relx=0.85, rely=0.51)

    RO16_14 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    RO16_14.place(relx=0.85, rely=0.61)

    RO16_15 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    RO16_15.place(relx=0.85, rely=0.75)


    RO16_16= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    RO16_16.place(relx=0.85, rely=0.85)



    #QUARTER
    QF_1 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    QF_1.place(relx=0.17, rely=0.10)


    QF_2 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    QF_2.place(relx=0.17, rely=0.33)

    QF_3 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    QF_3.place(relx=0.17, rely=0.56)

    QF_4 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    QF_4.place(relx=0.17, rely=0.8)

    QF_5 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    QF_5.place(relx=0.71, rely=0.10)


    QF_6 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    QF_6.place(relx=0.71, rely=0.33)

    QF_7 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    QF_7.place(relx=0.71, rely=0.56)

    QF_8 = tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2 
                 )


    QF_8.place(relx=0.71, rely=0.8)


    #SEMI
    SF_1= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    SF_1.place(relx=0.3, rely=0.215)


    SF_2= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    SF_2.place(relx=0.3, rely=0.68)


    SF_3= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    SF_3.place(relx=0.57, rely=0.215)


    SF_4= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    SF_4.place(relx=0.57, rely=0.68)

    #FINALS
    Finals1= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    Finals1.place(relx=0.35, rely=0.38)


    Finals2= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                )


    Finals2.place(relx=0.5, rely=0.38)
    
    Loser_Finals1= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                 )


    Loser_Finals1.place(relx=0.35, rely=0.53)


    Loser_Finals2= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=19, height=2  
                )


    Loser_Finals2.place(relx=0.5, rely=0.53)

    label_RO16_1= Ct.CTkLabel(page,text="ROUND OF 16",
                    width=100,height=40,corner_radius=0,bg_color=('transparent'),
                    fg_color=('transparent'),text_color='white',
                    font=("Stylus",20,'bold' )  )
    label_RO16_1.place(relx=0.0355, rely=0.927)

    label_RO16_2= Ct.CTkLabel(page,text="ROUND OF 16",
                    width=100,height=40,corner_radius=0,bg_color=('transparent'),
                    fg_color=('transparent'),text_color='white',
                    font=("Stylus",20,'bold' )  )
    label_RO16_2.place(relx=0.867, rely=0.927)

    
    label_QUARTER_1= Ct.CTkLabel(page,text="QUARTER FINAL",
                        width=100,height=40,corner_radius=0,bg_color=('transparent'),
                        fg_color=('transparent'),text_color='white',
                        font=("Stylus",20,'bold' )  )
    label_QUARTER_1.place(relx=0.17, rely=0.87)

    label_QUARTER_2= Ct.CTkLabel(page,text="QUARTER FINAL",
                        width=100,height=40,corner_radius=0,bg_color=('transparent'),
                        fg_color=('transparent'),text_color='white',
                        font=("Stylus",20,'bold' )  )
    label_QUARTER_2.place(relx=0.71, rely=0.87)

    label_SEMI_1= Ct.CTkLabel(page,text="SEMI FINAL",
                    width=100,height=40,corner_radius=0,bg_color=('transparent'),
                    fg_color=('transparent'),text_color='white',
                    font=("Stylus",20,'bold' )  )
    label_SEMI_1.place(relx=0.32, rely=0.755)

    label_SEMI_2= Ct.CTkLabel(page,text="SEMI FINAL",
                        width=100,height=40,corner_radius=0,bg_color=('transparent'),
                        fg_color=('transparent'),text_color='white',
                        font=("Stylus",20,'bold' )  )
    label_SEMI_2.place(relx=0.59, rely=0.755)

    label_FINAL= Ct.CTkLabel(page,text="FINAL",
                    width=100,height=40,corner_radius=0,bg_color=('transparent'),
                    fg_color=('transparent'),text_color='white',
                    font=("Stylus",20,'bold' )  )
    label_FINAL.place(relx=0.449, rely=0.315)

    label_LOSER_FINAL= Ct.CTkLabel(page,text="LOSERS FINAL",
                        width=100,height=40,corner_radius=0,bg_color=('transparent'),
                        fg_color=('transparent'),text_color='white',
                        font=("Stylus",20,'bold' )  )
    label_LOSER_FINAL.place(relx=0.435, rely=0.45)


    Button_Of_RO16=[(RO16_1,RO16_2),(RO16_3,RO16_4),(RO16_5,RO16_6),(RO16_7,RO16_8),(RO16_9,RO16_10),(RO16_11,RO16_12),(RO16_13,RO16_14),(RO16_15,RO16_16)]
    Button_Of_QF=[(QF_1,QF_2),(QF_3,QF_4),(QF_5,QF_6),(QF_7,QF_8)]
    Button_Of_SF=[(SF_1,SF_2),(SF_3,SF_4)]
    Button_Of_FINALS=[(Finals1,Finals2)]
    Button_Of_LOSER_FINALS=[(Loser_Finals1,Loser_Finals2)]
    for i in Button_Of_RO16:
        i[0].configure(state="disabled")
        i[1].configure(state="disabled")
    for i in Button_Of_QF:
        i[0].configure(state="disabled")
        i[1].configure(state="disabled")
    for i in Button_Of_SF:
        i[0].configure(state="disabled")
        i[1].configure(state="disabled")
    for i in Button_Of_FINALS:
        i[0].configure(state="disabled")
        i[1].configure(state="disabled")
    for i in Button_Of_LOSER_FINALS:
        i[0].configure(state="disabled")
        i[1].configure(state="disabled")
    #Winner.configure(state="disabled")

    START_button = Ct.CTkButton(page,bg_color=('transparent'),
                text='START',text_color='black',
                font=("Plasma",20,'bold' ),
                fg_color=('white')  ,width=150, height=60 ,
                command=lambda:Matching()) 
    
    START_button.place(relx=0.425, rely=0.9)
    
    Print_button = Ct.CTkButton(page,bg_color=('transparent'),
                    text='PRINT',text_color='black',border_width=3,border_color='black',
                    fg_color=('white')  ,width=100, height=40  
                    )
    
    def Matching():
        f=shelve.open(data_file)
        First_Round=algorithms.create_fixtures(data_file)
        
        #RO16
        if len(First_Round)==8:
            button_list=[]
           
            for i in Button_Of_RO16:
                i[0].configure(state="normal")
                i[1].configure(state="normal")

            for i,j in enumerate(First_Round): 

                Button_Of_RO16[i][0].configure(text=j[0][0:2])
                Button_Of_RO16[i][0].configure(command=lambda a=Button_Of_RO16[i][0],b=Button_Of_RO16[i][1]:Select(a,b))

                Button_Of_RO16[i][1].configure(text=j[1][0:2])
                Button_Of_RO16[i][1].configure(command=lambda a=Button_Of_RO16[i][1],b=Button_Of_RO16[i][0]:Select(a,b))
                button_list.extend([Button_Of_RO16[i][0],Button_Of_RO16[i][1]]) 
                
            START_button.forget()
            Submit_button1= Ct.CTkButton(page,bg_color=('transparent'),
                    text='SUBMIT',text_color='black',
                    font=("Plasma",20,'bold' ),
                    fg_color=('white')  ,width=150, height=60 ,
                    command=lambda:Match_Check_RO16(button_list)) 
        
            Submit_button1.place(relx=0.425, rely=0.9)

            



            def Match_Check_RO16(button_list):
                for i in button_list:
                    if i.cget('bg')=='blue':
                        tk.messagebox.showerror("Error",'Update All The Matches ')
                        break
                else:
                    deselected_button=[a.cget('text') for a in button_list if a.cget('bg')=='red']
                    for i in deselected_button:
                        FUNC.delete1(i[:6])
                    tk.messagebox.showinfo('SUCESS','Student moved to the next Round')
                    Next_Round_R016()
        #QF
        elif len(First_Round)==4:
           
            
            for i in Button_Of_QF:
                i[0].configure(state="normal")
                i[1].configure(state="normal")
            for i,j in enumerate(First_Round): 

                Button_Of_QF[i][0].configure(text=j[0][0:2])
                Button_Of_QF[i][0].configure(command=lambda a=Button_Of_QF[i][0],b=Button_Of_QF[i][1]:Select(a,b))

                Button_Of_QF[i][1].configure(text=j[1][0:2])
                Button_Of_QF[i][1].configure(command=lambda a=Button_Of_QF[i][1],b=Button_Of_QF[i][0]:Select(a,b))
                
            Button_Of_QF_1=[QF_1,QF_2,QF_3,QF_4,QF_5,QF_6,QF_7,QF_8]
            START_button.forget()
            Submit_button2= Ct.CTkButton(page,bg_color=('transparent'),
                    text='SUBMIT',text_color='black',
                    font=("Plasma",20,'bold' ),
                    fg_color=('white')  ,width=150, height=60 ,
                    command=lambda:Match_Check_QF()) 
        
            Submit_button2.place(relx=0.425, rely=0.9)

            


            def Match_Check_QF():
                for i in Button_Of_QF_1:
                    if i.cget('bg')=='blue':
                        tk.messagebox.showerror("Error",'Update All The Matches ')
                        break
                else:
                    Next_Round_SF1()
        #SF
        elif len(First_Round)==2:
            button_list=[]
            
            for i in Button_Of_SF:
                i[0].configure(state="normal")
                i[1].configure(state="normal")
            for i,j in enumerate(First_Round): 

                Button_Of_SF[i][0].configure(text=j[0][0:2])
                Button_Of_SF[i][0].configure(command=lambda a=Button_Of_SF[i][0],b=Button_Of_SF[i][1]:Select(a,b))

                Button_Of_SF[i][1].configure(text=j[1][0:2])
                Button_Of_SF[i][1].configure(command=lambda a=Button_Of_SF[i][1],b=Button_Of_SF[i][0]:Select(a,b))
                button_list.extend([Button_Of_SF[i][0],Button_Of_SF[i][1]]) 

            START_button.forget()
            Submit_button3 = Ct.CTkButton(page,bg_color=('transparent'),
                    text='SUBMIT',text_color='black',
                    font=("Plasma",20,'bold' ),
                    fg_color=('white')  ,width=150, height=60 ,
                    command=lambda:Match_Check_SF()) 
            
            Submit_button3.place(relx=0.425, rely=0.9)
            Button_Of_SF_1=[SF_1,SF_2,SF_3,SF_4]
            def Match_Check_SF():
                for i in Button_Of_SF_1:
                    if i.cget('bg')=='blue':
                        tk.messagebox.showerror("Error",'Update All The Matches ')
                        break
                else:
                    NextRound_Finals1()

        # FOR RO16
    def Next_Round_R016():
        Submit_button11= Ct.CTkButton(page,bg_color=('transparent'),
                    text='NEXT ROUND',text_color='black',
                    font=("Plasma",20,'bold' ),
                    fg_color=('white')  ,width=150, height=60 ,
                    command=lambda:Next_Round_QF1()) 
        Submit_button11.place(relx=0.425, rely=0.9)
        
    def Next_Round_QF1():
        Print_button.destroy()
        Button_Of_QF=[(QF_1,QF_2),(QF_3,QF_4),(QF_5,QF_6),(QF_7,QF_8)]
        for i in Button_Of_QF:
            i[0].configure(state="normal")
            i[1].configure(state="normal")

        Button_Of_RO16_1=[(RO16_1,RO16_2),(RO16_3,RO16_4),(RO16_5,RO16_6),(RO16_7,RO16_8),(RO16_9,RO16_10),(RO16_11,RO16_12),(RO16_13,RO16_14),(RO16_15,RO16_16)]
        Button_Of_QF_1=[QF_1,QF_2,QF_3,QF_4,QF_5,QF_6,QF_7,QF_8]

        for i in range (len(Button_Of_RO16_1)):
            if Button_Of_RO16_1[i][0].cget('bg')=='green':
                a=Button_Of_RO16_1[i][0].cget('text')
                Button_Of_QF_1[i].configure(text=a)
                
            else:
                a=Button_Of_RO16_1[i][1].cget('text')
                Button_Of_QF_1[i].configure(text=a)

        Button_Of_QF_2=[(QF_1,QF_2),(QF_3,QF_4),(QF_5,QF_6),(QF_7,QF_8)]

        for i in range(len(Button_Of_QF_2)):
            Button_Of_QF_2[i][0].configure(command=lambda a=Button_Of_QF_2[i][0],b=Button_Of_QF_2[i][1]:Select(a,b))
            Button_Of_QF_2[i][1].configure(command=lambda a=Button_Of_QF_2[i][1],b=Button_Of_QF_2[i][0]:Select(a,b))

        for i in Button_Of_RO16:
            i[0].configure(state="disabled")
            i[1].configure(state="disabled")

        
        Submit_button12= Ct.CTkButton(page,bg_color=('transparent'),
                text='NEXT ROUND',text_color='black',
                font=("Plasma",20,'bold' ),
                fg_color=('white')  ,width=150, height=60 ,
                command=lambda:Match_Check_QF()) 
        Submit_button12.place(relx=0.425, rely=0.9) 

        def Match_Check_QF():
                for i in Button_Of_QF_1:
                    if i.cget('bg')=='blue':
                        tk.messagebox.showerror("Error",'Update All The Matches ')
                        break
                else:
                    Next_Round_SF1()
    def Next_Round_SF1():
        
        Button_Of_SF=[(SF_1,SF_2),(SF_3,SF_4)]
        for i in Button_Of_SF:
            i[0].configure(state="normal")
            i[1].configure(state="normal")

        Button_Of_QF_1=[(QF_1,QF_2),(QF_3,QF_4),(QF_5,QF_6),(QF_7,QF_8)]
        Button_Of_SF_1=[SF_1,SF_2,SF_3,SF_4]

        for i in range (len(Button_Of_QF_1)):
            if Button_Of_QF_1[i][0].cget('bg')=='green':
                a=Button_Of_QF_1[i][0].cget('text')
                Button_Of_SF_1[i].configure(text=a)
            
            else:
                a=Button_Of_QF_1[i][1].cget('text')
                Button_Of_SF_1[i].configure(text=a)

        Button_Of_SF_2=[(SF_1,SF_2),(SF_3,SF_4)]

        for i in range(len(Button_Of_SF_2)):
            Button_Of_SF_2[i][0].configure(command=lambda a=Button_Of_SF_2[i][0],b=Button_Of_SF_2[i][1]:Select(a,b))
            Button_Of_SF_2[i][1].configure(command=lambda a=Button_Of_SF_2[i][1],b=Button_Of_SF_2[i][0]:Select(a,b))

        for i in Button_Of_QF:
            i[0].configure(state="disabled")
            i[1].configure(state="disabled")

        

        
        Submit_button13= Ct.CTkButton(page,bg_color=('transparent'),
            text='NEXT ROUND',text_color='black',
            font=("Plasma",20,'bold' ),
            fg_color=('white')  ,width=150, height=60 ,
            command=lambda:Match_Check_SF()) 
        Submit_button13.place(relx=0.425, rely=0.9) 

        def Match_Check_SF():
                for i in Button_Of_SF_1:
                    if i.cget('bg')=='blue':
                        tk.messagebox.showerror("Error",'Update All The Matches ')
                        break
                else:
                    NextRound_Finals1()

    def NextRound_Finals1():
        
        Button_Of_FINALS=[(Finals1,Finals2)]
        for i in Button_Of_FINALS:
            i[0].configure(state="normal")
            i[1].configure(state="normal")

        Button_Of_LOSER_FINALS=[(Loser_Finals1,Loser_Finals2)]
        for i in Button_Of_LOSER_FINALS:
            i[0].configure(state="normal")
            i[1].configure(state="normal")

        Button_Of_SF_1=[(SF_1,SF_2),(SF_3,SF_4)]
        Button_Of_FINALS_1=[Finals1,Finals2]
        Button_Of_LOSER_FINALS_1=[Loser_Finals1,Loser_Finals2]
        #FOR FINAL
        for i in range (len(Button_Of_SF_1)):
            if Button_Of_SF_1[i][0].cget('bg')=='green':
                a=Button_Of_SF_1[i][0].cget('text')
                Button_Of_FINALS_1[i].configure(text=a)
            
            else:
                a=Button_Of_SF_1[i][1].cget('text')
                Button_Of_FINALS_1[i].configure(text=a)

        Button_Of_FINALS_2=[(Finals1,Finals2)]

        for i in range(len(Button_Of_FINALS_2)):
            Button_Of_FINALS_2[i][0].configure(command=lambda a=Button_Of_FINALS_2[i][0],b=Button_Of_FINALS_2[i][1]:Select(a,b))
            Button_Of_FINALS_2[i][1].configure(command=lambda a=Button_Of_FINALS_2[i][1],b=Button_Of_FINALS_2[i][0]:Select(a,b))

        #FOR LOSERS FINAL
        for i in range (len(Button_Of_SF_1)):
            if Button_Of_SF_1[i][0].cget('bg')=='red':
                a=Button_Of_SF_1[i][0].cget('text')
                Button_Of_LOSER_FINALS_1[i].configure(text=a)
            
            else:
                a=Button_Of_SF_1[i][1].cget('text')
                Button_Of_LOSER_FINALS_1[i].configure(text=a)
        
        Button_Of_LOSER_FINALS_2=[(Loser_Finals1,Loser_Finals2)]
        
        for i in range(len(Button_Of_LOSER_FINALS_2)):
            Button_Of_LOSER_FINALS_2[i][0].configure(command=lambda a=Button_Of_LOSER_FINALS_2[i][0],b=Button_Of_LOSER_FINALS_2[i][1]:Select(a,b))
            Button_Of_LOSER_FINALS_2[i][1].configure(command=lambda a=Button_Of_LOSER_FINALS_2[i][1],b=Button_Of_LOSER_FINALS_2[i][0]:Select(a,b))


        for i in Button_Of_SF_1:
            i[0].configure(state="disabled")
            i[1].configure(state="disabled")

       
        #Submit_button13.forget()
        Submit_button14= Ct.CTkButton(page,bg_color=('transparent'),
            text='RESULT',text_color='black',
            font=("Plasma",20,'bold' ),
            fg_color=('white')  ,width=150, height=60 ,
            command=lambda:Match_Check_FINALS()) 
        Submit_button14.place(relx=0.425, rely=0.9) 

        def Match_Check_FINALS():
                for i in Button_Of_FINALS_1:
                    if i.cget('bg')=='blue':
                        tk.messagebox.showerror("Error",'Update All The Matches ')
                        break
                    else:
                        for i in Button_Of_LOSER_FINALS_1:
                            if i.cget('bg')=='blue':
                                tk.messagebox.showerror("Error",'Update All The Matches ')
                                break
                else:
                    RESULTS()

    def RESULTS():
        
        Button_Of_FINALS=[(Finals1,Finals2)]
        Winner= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=35, height=1  
                 )
        Winner.place(relx=0.39, rely=0.025)
        
        RunnerUp_1= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=35, height=1  
                 )
        RunnerUp_1.place(relx=0.39, rely=0.07)
        
        for i in range (len(Button_Of_FINALS)):
            if Button_Of_FINALS[i][0].cget('bg')=='green':
                a=Button_Of_FINALS[i][0].cget('text')
                Winner.configure(text='1st.'+a)
                Winner.configure(bg='gold')
            
            else:
                a=Button_Of_FINALS[i][1].cget('text')
                Winner.configure(text='1st.'+a)
                Winner.configure(bg='gold')
        for i in range (len(Button_Of_FINALS)):
            if Button_Of_FINALS[i][0].cget('bg')=='red':
                a=Button_Of_FINALS[i][0].cget('text')
                RunnerUp_1.configure(text='2nd.'+a)
                RunnerUp_1.configure(bg='silver')
            else:
                a=Button_Of_FINALS[i][1].cget('text')
                RunnerUp_1.configure(text='2nd.'+a)
                RunnerUp_1.configure(bg='silver')
            
        RunnerUp_2= tk.Button(page,bg=('blue'),text='',
                font=("Plasma",10,'bold' ),borderwidth=3,
                fg=('black')  ,width=35, height=1 
                 )
        RunnerUp_2.place(relx=0.39, rely=0.116)
        
        for i in range (len(Button_Of_LOSER_FINALS)):
            if Button_Of_LOSER_FINALS[i][0].cget('bg')=='green':
                a=Button_Of_LOSER_FINALS[i][0].cget('text')
                RunnerUp_2.configure(text='3rd.'+a)
                RunnerUp_2.configure(bg='brown')
            else:
                a=Button_Of_LOSER_FINALS[i][1].cget('text')
                RunnerUp_2.configure(text='3rd.'+a)
                RunnerUp_2.configure(bg='brown') 
        for i in Button_Of_FINALS:
            i[0].configure(state="disabled")
            i[1].configure(state="disabled")

        for i in Button_Of_LOSER_FINALS:
            i[0].configure(state="disabled")
            i[1].configure(state="disabled")
        

    def Select(a,b):
        if a.cget('bg')!='green':  
            a.configure(bg='green')
            b.configure(bg='red')
        else:
            a.configure(bg='red')
            b.configure(bg='green')



    