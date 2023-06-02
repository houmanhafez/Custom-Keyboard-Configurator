import time
from data import keycap_sets, keyboard_kits, switch_sets, other, keyboards
import requests
from bs4 import BeautifulSoup
from PIL import Image
import customtkinter
import webbrowser

''' !Note!
In order to run this app, make sure you have python 3 and also please install the libraries with pip: requests, pil or pillow, bs4, webbrowser and customtkinter
To do this, you need to go into your terminal and type 'pip install *libraryName*'
Created by Houman Hafez Alghoran (I started at 21st March 2023 and the first beta release on Github was v.0.2.0-beta)'''


customtkinter.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme('blue')  # Themes: "blue", "green", "dark-blue"



def loadImages(list):
    images = {}
    for x in list:
        small_image = list[x]['images']['small']
        large_image = list[x]['images']['large']
        images[x] = {
            "images": {
                "small": customtkinter.CTkImage(Image.open(small_image['path']), size=small_image['size']),
                "large": customtkinter.CTkImage(Image.open(large_image['path']), size=large_image['size'])
            }
        }
    return images

kitImages =     loadImages(keyboard_kits)
keycapImages =  loadImages(keycap_sets)
switchImages =  loadImages(switch_sets)
otherImages =   loadImages(other)
keyboardImages= loadImages(keyboards)
#MAIN CLASS 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        

        # THE WINDOW

        self.title("Custom Keyboard Configurator")
        self.geometry(f"{1300}x{900}")
        self.iconbitmap("icons/icon.ico")
        self.resizable(False, False)
        

        # THE USED FONT AND SIZE 
        
        font1 = customtkinter.CTkFont(family= "Microsoft New Tai Lue" ,size=20,weight="bold")
        font2 = customtkinter.CTkFont(family= "Microsoft New Tai Lue" , size=16 ,weight="bold")
        
        # START PAGE WITH THE WIDGETS

        self.start_frame = customtkinter.CTkFrame(self,
                                            height= 900,
                                            width= 400,
                                            corner_radius=0)
        self.start_frame.grid(row=0, column=1)


        self.start_page_bg = customtkinter.CTkLabel(self.start_frame,
                                            image= otherImages['start_bg']['images']['small'],
                                            text="")
        self.start_page_bg.grid(row=0, column= 1)

        self.start_page_logos = customtkinter.CTkButton(self.start_frame,
                                            image= otherImages['github_logo']['images']['small'],
                                            command = lambda: webbrowser.open(other['github_logo']['link']),   
                                            fg_color=("#fbd3c7"),
                                            bg_color=("#fbd3c7"),
                                            hover_color=("#fbd3c7"),
                                            text="",
                                            height=50,
                                            width= 20)
        self.start_page_logos.grid(row=0, column= 1)
        self.start_page_logos.place(x = 0, y = 840)
        
        self.start_page_logos2 = customtkinter.CTkButton(self.start_frame,
                                            image= otherImages['discord']['images']['small'],
                                            command = lambda: webbrowser.open(other['discord']['link']),   
                                            fg_color=("#fbd3c7"),
                                            bg_color=("#fbd3c7"),
                                            hover_color=("#fbd3c7"),
                                            text="",
                                            height=50,
                                            width= 20)
        
        self.start_page_logos2.place(x = 60, y = 840)

        self.start_button = customtkinter.CTkButton(self.start_frame,
                                            fg_color=("#003366"),
                                            bg_color=("#fbd3c7"),
                                            hover_color=("#ffb6c1"),
                                            corner_radius=80,
                                            text= 'Start',
                                            command=self.show_the_frame,
                                            font= customtkinter.CTkFont(family= "Microsoft New Tai Lue" ,size=22,weight="bold"),
                                            height= 65,
                                            width=210)
        self.start_button.grid(row=2, column=1, columnspan= 4, rowspan= 4)
        self.start_button.place(x = 550, y = 610)
        
        self.keeb_button = customtkinter.CTkButton(self.start_frame,
                                            fg_color=("#003366"),
                                            bg_color=("#fbd3c7"),
                                            hover_color=("#ffb6c1"),
                                            corner_radius=80,
                                            text= 'Keyboards',
                                            command=self.show_keeb,
                                            font=customtkinter.CTkFont(family= "Microsoft New Tai Lue" ,size=22,weight="bold"),
                                            height= 65,
                                            width=210,
                                           
                                            )
        self.keeb_button.grid(row=2, column=1, columnspan= 4, rowspan= 4)
        self.keeb_button.place(x = 550, y = 720)
        

        self.start_title = customtkinter.CTkLabel(self.start_frame, 
                                                width=700,
                                                height= 230,
                                                font=customtkinter.CTkFont(family= "Microsoft New Tai Lue" ,size=28,weight="bold"),
                                                text= "Build your Custom Keyboard",
                                                fg_color='#fbd3c7',
                                                text_color= "#003366")
        self.start_title.grid(row=0, column=1, pady=100)
        self.start_title.place(x = 315, y = 90)
        
        self.start_text = customtkinter.CTkLabel(self.start_frame, 
                                                width=700,
                                                height= 230,
                                                font=customtkinter.CTkFont(family= "Calibri" ,size=22,weight="bold"),
                                                text= "ㅤChoose a Keyboard kit in your budget\nㅤChoose the switches you like\nㅤChoose a keycap set \nㅤSee the prices \nㅤListen to a sound test \n\nㅤㅤ watch recommended reviews and learn about mods.\n ",
                                                fg_color='#fbd3c7',
                                                text_color= "#003366")
        self.start_text.grid(row=0, column=1, pady=100)
        self.start_text.place(x = 300, y = 300)
       
       #SIDE_BAR
        self.sidebar_frame = customtkinter.CTkFrame(self,
                                                width=120,
                                                border_width=2,
                                                corner_radius=1,)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                 text="Keeb Configurator",
                                                 compound= 'right', 
                                                 font=font1)
        
        self.hide_sidebar_button = customtkinter.CTkButton(self.sidebar_frame,
                                                    text = "",
                                                    command =self.hide_sidebar,
                                                    image=otherImages['menu']['images']['small'],
                                                    fg_color=("gray17"),
                                                    hover_color=("#242424"),
                                                    height= 35,
                                                    width= 35)
        self.hide_sidebar_button.place(x= 0, y= 30)
        

        self.show_sidebar_button = customtkinter.CTkButton(self,
                                                    text = "",
                                                    command =self.show_sidebar,
                                                    image=otherImages['menu']['images']['small'],
                                                    fg_color=("#242424"),
                                                    hover_color=("gray17"),
                                                    height= 35,
                                                    width= 35)
        
        
        
        
        
        # SIDEBAR BUTTONS
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("#333333"),
                                                border_color= ("#3E5A70"),
                                                command = lambda: webbrowser.open(other['kits_guide']['link']),                           
                                                image=otherImages['new_tab']['images']['small'],
                                                border_width=2,
                                                corner_radius=20,
                                                text= 'ㅤㅤKitsㅤGuideㅤㅤ',
                                                font= customtkinter.CTkFont(size=16 ,weight="bold"),
                                                height= 35,
                                                width=235)                   
                                   
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("#333333"),
                                                border_color= ("#3E5A70"),
                                                command = lambda: webbrowser.open(other['switches_guide']['link']), 
                                                image=otherImages['new_tab']['images']['small'],
                                                border_width=2,
                                                corner_radius=20,
                                                text= 'ㅤSwitches Guideㅤ',
                                                font= customtkinter.CTkFont(size=16 ,weight="bold"),
                                                height= 35,
                                                width=235)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("#333333"),
                                                border_color= ("#3E5A70"),
                                                command = lambda: webbrowser.open(other['mods_guide']['link']), 
                                                image=otherImages['new_tab']['images']['small'],
                                                border_width=2,
                                                corner_radius=20,
                                                text= 'ㅤㅤMods Guideㅤㅤ',
                                                font= customtkinter.CTkFont(size=16 ,weight="bold"),
                                                height= 35,
                                                width=235)
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("#333333"),
                                                border_color= ("#3E5A70"),
                                                command = lambda: webbrowser.open(other['stabilizers']['link']), 
                                                image=otherImages['new_tab']['images']['small'],
                                                border_width=2,
                                                corner_radius=20,
                                                text= 'ㅤㅤStabs Guideㅤㅤ',
                                                font= customtkinter.CTkFont(size=16 ,weight="bold"),
                                                height= 35,
                                                width=235)


        self.sidebar_widget = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("gray17"),
                                                hover_color=("gray17"),
                                                border_color= "#3E5A70",
                                                border_width=2,
                                                corner_radius=20,
                                                command = lambda: webbrowser.open(other['widget0']['link']), 
                                                image=otherImages['widget0']['images']['large'], 
                                                text="", 
                                                height=220,
                                                width=180)
        
        
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                    text="UI Scaling:",
                                                    font= font2,
                                                    anchor="w")
        
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,

                                                               values=["100%", "105%"],
                                                               fg_color="#3E5A70",
                                                               command=self.change_scaling_event)


        # THE MAIN LABEL WITH THE MAIN FUNCTIONS ETC.
        self.main_top = customtkinter.CTkLabel(self,
                                               text="Your Config:",
                                               anchor=customtkinter.N,
                                               font=font1, 
                                               height= 340, 
                                               width= 100,)


        self.main_switch = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                text= 'Choose a Switch',
                                                font=customtkinter.CTkFont(family= "Microsoft New Tai Lue", weight="bold"),
                                                height=180,
                                                width=100)
        
        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",
                                                hover_color=("#242424"),
                                                text= 'Choose a Keyboard Kit',
                                                font=customtkinter.CTkFont(family= "Microsoft New Tai Lue", weight="bold"),
                                                height=180,
                                                width=100)


        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",
                                                hover_color=("#242424"),
                                                text= 'Choose a Keycap Set',
                                                font=customtkinter.CTkFont(family= "Microsoft New Tai Lue", weight="bold"),
                                                height=180,
                                                width=100)
        
        
        self.main_switchset_price = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),                      
                                                font=font1,
                                                height=80,
                                                text= '',
                                                width=100)

        self.main_kit_price = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),                      
                                                font=font1,
                                                text= "",
                                                height=80,
                                                width=100)
        
        self.main_keycapset_price = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),                      
                                                font=font1,
                                                text= '',
                                                height=80,
                                                width=100)
        

 
        # ALL THE SCROLLABLE FRAMES (SWITCHES), (KEYCAPS) and (KEYBOARD KITS)
        self.keyboardkit_frame = customtkinter.CTkScrollableFrame(self,
                                                label_text="Keyboard Kits",
                                                label_font=font2,
                                                width= 220,
                                                height= 300)
        self.keyboardkit_frame_switches = []


        self.keycaps_frame = customtkinter.CTkScrollableFrame(self,
                                                        label_text="Keycaps",
                                                        label_font=font2,
                                                        height= 300)
        self.keycaps_frame_switches = []

        self.switches_frame = customtkinter.CTkScrollableFrame(self,
                                                               label_text="Switches (Prices are for 70 Switches)",
                                                               label_font=font2,
                                                               orientation="horizontal",
                                                               height=55)
        self.switches_frame_switches = []




        # ALL THE KEYBOARD KITS BUTTONS 
        self.tofu60 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                              command=self.tofu_60,
                                              image=kitImages['tofu60']['images']['small'],
                                              corner_radius=20,
                                              fg_color=("#3e706d"),
                                              border_width=0,
                                              border_color= "#3e706d",
                                              text='Tofu60')
        self.keyboardkit_frame_switches.append(self.tofu60)



        self.tofu65 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                              command=self.tofu_65,
                                              corner_radius=20,
                                              fg_color=("#3e706d"),
                                              border_width=0,
                                              border_color= "#3e706d",
                                              image=kitImages['tofu65']['images']['small'],
                                              text='Tofu65')
        self.keyboardkit_frame_switches.append(self.tofu65)
 


        self.tester68 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                command=self.tester_68,
                                                corner_radius=20,
                                                fg_color=("#3e706d"),
                                                border_width=0,
                                                border_color= "#3e706d",
                                                image=kitImages['tester68']['images']['small'],
                                                text='Tester68')
        self.keyboardkit_frame_switches.append(self.tester68)


        self.tester84 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                command=self.tester_84,
                                                corner_radius=20,
                                                fg_color=("#3e706d"),
                                                border_width=0,
                                                border_color= "#3e706d",
                                                image=kitImages['tester84']['images']['small'],
                                                text='Tester84')

        self.keyboardkit_frame_switches.append(self.tester84)


        self.gmk67 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                            command=self.gmk_67,
                                            corner_radius=20,
                                            fg_color=("#3e706d"),
                                            border_width=0,
                                            border_color= "#3e706d",
                                            image=kitImages['gmk67']['images']['small'],
                                            text='Gmk 67')

        self.keyboardkit_frame_switches.append(self.gmk67)


        self.gas67 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                            command=self.gas_67,
                                            corner_radius=20,
                                            fg_color=("#3e706d"),
                                            border_width=0,
                                            border_color= "#3e706d",   
                                            image=kitImages['gas67']['images']['small'],
                                            text='GAS 67')

        self.keyboardkit_frame_switches.append(self.gas67)


        self.everglide75 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                   command=self.everglide_75,
                                                   corner_radius=20,
                                                   fg_color=("#3e706d"),
                                                    border_width=0,
                                                    border_color= "#3e706d",
                                                   image=kitImages['everglide75']['images']['small'],
                                                   text='EG 75')

        self.keyboardkit_frame_switches.append(self.everglide75)
 


        self.mk870 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.mk_870,
                                             corner_radius=20,
                                             fg_color=("#3e706d"),
                                            border_width=0,
                                            border_color= "#3e706d",
                                             image=kitImages['mk870']['images']['small'],
                                             text='MK 870')

        self.keyboardkit_frame_switches.append(self.mk870)
 


        self.monsgeekm1 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                  command=self.monsgeek_m1,
                                                  corner_radius=20,
                                                  fg_color=("#3e706d"),
                                                  border_width=0,
                                                  border_color= "#3e706d",
                                                  image=kitImages['monsgeekm1']['images']['small'],
                                                  text='MG M1')

        self.keyboardkit_frame_switches.append(self.monsgeekm1)
 


        self.nexttime75 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                  command=self.nexttime_75,
                                                  corner_radius=20,
                                                  fg_color=("#3e706d"),
                                                  border_width=0,
                                                  border_color= "#3e706d",
                                                  image=kitImages['nexttime75']['images']['small'], 
                                                  text='NT 75')

        self.keyboardkit_frame_switches.append(self.nexttime75)
 


        self.nj80 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                            command=self.nj_80,
                                            corner_radius=20,
                                            fg_color=("#3e706d"),
                                            border_width=0,
                                            border_color= "#3e706d",
                                            image=kitImages['nj80']['images']['small'],
                                            text='NJ 80')

        self.keyboardkit_frame_switches.append(self.nj80)
 


        self.tm680 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.tm_680,
                                             corner_radius=20,
                                             fg_color=("#3e706d"),
                                             border_width=0,
                                             border_color= "#3e706d",
                                             image=kitImages['tm680']['images']['small'],
                                             text='TM680')
                                             
        self.keyboardkit_frame_switches.append(self.tm680)
 




        # ALL THE KEYCAP SET BUTTONS
        self.dcx9009 = customtkinter.CTkButton(master=self.keycaps_frame,
                                               command=self.dcx_9009,
                                               corner_radius=20,
                                               fg_color=("#3e706d"),
                                               border_width=0,
                                               border_color= "#3e706d",
                                               image=keycapImages['dcx_9009']['images']['small'],
                                               text='9009')

        self.keycaps_frame_switches.append(self.dcx9009)
 


        self.dcxblackonwhite = customtkinter.CTkButton(master=self.keycaps_frame,
                                                       command=self.dcx_black_on_white,
                                                       corner_radius=20,
                                                       fg_color=("#3e706d"),
                                                        border_width=0,
                                                        border_color= "#3e706d",
                                                       image=keycapImages['dcx_bow']['images']['small'],
                                                       text='B.O.W')

        self.keycaps_frame_switches.append(self.dcxblackonwhite)
 


        self.dcxwhiteonblack = customtkinter.CTkButton(master=self.keycaps_frame,
                                                       command=self.dcx_white_on_black,
                                                       corner_radius=20,
                                                       fg_color=("#3e706d"),
                                                       border_width=0,
                                                       border_color= "#3e706d",
                                                       image=keycapImages['dcx_wob']['images']['small'],
                                                       text='W.O.B')

        self.keycaps_frame_switches.append(self.dcxwhiteonblack)
 


        self.dcxcyber = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.dcx_cyber,
                                                corner_radius=20,
                                                fg_color=("#3e706d"),
                                                border_width=0,
                                                border_color= "#3e706d",
                                                image=keycapImages['dcx_cyber']['images']['small'],
                                                text='Cyber')

        self.keycaps_frame_switches.append(self.dcxcyber)
 


        self.dcxhyperfuse = customtkinter.CTkButton(master=self.keycaps_frame,
                                                    command=self.dcx_hyperfuse,
                                                    corner_radius=20,
                                                    fg_color=("#3e706d"),
                                                    border_width=0,
                                                    border_color= "#3e706d",
                                                    image=keycapImages['dcx_hyperfuse']['images']['small'],
                                                    text='DCX HF')

        self.keycaps_frame_switches.append(self.dcxhyperfuse)
 


        self.dcxkeyman = customtkinter.CTkButton(master=self.keycaps_frame,
                                                 command=self.dcx_keyman,
                                                 corner_radius=20,
                                                 fg_color=("#3e706d"),
                                                 border_width=0,
                                                 border_color= "#3e706d",
                                                 image=keycapImages['dcx_keyman']['images']['small'],
                                                 text='Keyman')

        self.keycaps_frame_switches.append(self.dcxkeyman)
 


        self.dcxviolac = customtkinter.CTkButton(master=self.keycaps_frame,
                                                 command=self.dcx_violac,
                                                 corner_radius=20,
                                                 fg_color=("#3e706d"),
                                                 border_width=0,
                                                 border_color= "#3e706d",
                                                 image=keycapImages['dcx_violac']['images']['small'],
                                                 text='Violac')
        self.keycaps_frame_switches.append(self.dcxviolac)
 


        self.gmkarmstrong = customtkinter.CTkButton(master=self.keycaps_frame,
                                                    command=self.gmk_armstrong,
                                                    corner_radius=20,
                                                    fg_color=("#3e706d"),
                                                    border_width=0,
                                                    border_color= "#3e706d",
                                                    image=keycapImages['gmk_armstrong']['images']['small'],
                                                    text='GodS')
        self.keycaps_frame_switches.append(self.gmkarmstrong)
 


        self.gmkbluesamurai = customtkinter.CTkButton(master=self.keycaps_frame,
                                                      command=self.gmk_bluesamurai,
                                                      corner_radius=20,
                                                      fg_color=("#3e706d"),
                                                      border_width=0,
                                                      border_color= "#3e706d",
                                                      image=keycapImages['gmk_bluesamurai']['images']['small'],
                                                      text='BlueS')
        self.keycaps_frame_switches.append(self.gmkbluesamurai)
 


        self.gmkdots = customtkinter.CTkButton(master=self.keycaps_frame,
                                               command=self.gmk_dots,
                                               corner_radius=20,
                                               fg_color=("#3e706d"),
                                               border_width=0,
                                               border_color= "#3e706d",
                                               image=keycapImages['gmk_dots']['images']['small'],
                                               text='Dots')
        self.keycaps_frame_switches.append(self.gmkdots)
 


        self.gmkkaiju = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.gmk_kaiju,
                                                corner_radius=20,
                                                fg_color=("#3e706d"),
                                                border_width=0,
                                                border_color= "#3e706d",
                                                image=keycapImages['gmk_kaiju']['images']['small'],
                                                text='Kaiju')
        self.keycaps_frame_switches.append(self.gmkkaiju)
 

 
        self.gmklaser = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.gmk_laser,
                                                corner_radius=20,
                                                fg_color=("#3e706d"),
                                                border_width=0,
                                                border_color= "#3e706d",
                                                image=keycapImages['gmk_laser']['images']['small'],
                                                text='Laser')
        self.keycaps_frame_switches.append(self.gmklaser)
 
        






        # ALL THE SWITCHE SET BUTTONS
        self.c3kiwi = customtkinter.CTkButton(master=self.switches_frame,
                                              command=self.c3_kiwi,
                                              fg_color=("#703E41"),
                                              image=switchImages['c3_kiwi']['images']['small'],
                                              text='C3 Kiwi',
                                              compound='left',
                                              width=140,
                                              height=45)
        self.switches_frame_switches.append(self.c3kiwi)
 


        self.c3tang = customtkinter.CTkButton(master=self.switches_frame,
                                              command=self.c3_tangerine,
                                              fg_color=("#703E41"),
                                              image=switchImages['c3_tangerine']['images']['small'],
                                              text='C3 Tangerine',
                                              compound='left',
                                              width=140,
                                              height=45)
        self.switches_frame_switches.append(self.c3tang)
 


        self.boxjade = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.box_jade,
                                               fg_color=("#703E41"),
                                               image=switchImages['box_jade']['images']['small'],
                                               text='Box Jade',
                                               compound='left',
                                               width=140,
                                               height=45)
        self.switches_frame_switches.append(self.boxjade)
 


        self.boxnavy = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.box_navy,
                                               fg_color=("#703E41"),
                                               image=switchImages['box_navy']['images']['small'],
                                               text='Box Navy',
                                               compound='left',
                                               width=140,
                                               height=45)
        self.switches_frame_switches.append(self.boxnavy)
 


        self.glopanda = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.holy_panda,
                                                fg_color=("#703E41"),
                                                image=switchImages['holy_panda']['images']['small'],
                                                text='Holy Panda',
                                                compound='left',
                                                width=140,
                                                height=45)
        self.switches_frame_switches.append(self.glopanda)
 


        self.holpanda = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.glorious_panda,
                                                fg_color=("#703E41"),
                                                image=switchImages['glorious_panda']['images']['small'],
                                                text='Glor. Panda',
                                                compound='left',
                                                width=140,
                                                height=45)
        self.switches_frame_switches.append(self.holpanda)
 


        self.gateronblackinkv2 = customtkinter.CTkButton(master=self.switches_frame,
                                                         command=self.gateron_black_ink_v2,
                                                         fg_color=("#703E41"),
                                                         image=switchImages['gateron_ink_black_v2']['images']['small'],
                                                         text='Gateron InkV2',
                                                         compound='left',
                                                         width=140,
                                                         height=45)
        self.switches_frame_switches.append(self.gateronblackinkv2)
 


        self.gateronoilking = customtkinter.CTkButton(master=self.switches_frame,
                                                      command=self.gateron_oil_king,
                                                      fg_color=("#703E41"),
                                                      image=switchImages['gateron_oilking']['images']['small'],
                                                      text='Gateron OilKing',
                                                      compound='left',
                                                      width=140,
                                                      height=45)
        self.switches_frame_switches.append(self.gateronoilking)
 


        self.nkcreams = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.nk_creams,
                                                fg_color=("#703E41"),
                                                image=switchImages['novelkey_cream']['images']['small'],
                                                text='NkCreams',
                                                compound='left',
                                                width=140,
                                                height=45)
        self.switches_frame_switches.append(self.nkcreams)
 


        self.kangwhitev3 = customtkinter.CTkButton(master=self.switches_frame,
                                                   command=self.kang_white_v3,
                                                   fg_color=("#703E41"),
                                                   image=switchImages['ktt_kang_white_v3']['images']['small'],
                                                   text='Kang White V3',
                                                   compound='left', width=140, height=45)
        self.switches_frame_switches.append(self.kangwhitev3)
 


        self.kttgrapefruit = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.ktt_grapefruit,
                                                     fg_color=("#703E41"),
                                                     image=switchImages['ktt_grapefruit']['images']['small'],
                                                     text='KTT Grapefruit',
                                                     compound='left',
                                                     width=140, height=45)
        self.switches_frame_switches.append(self.kttgrapefruit)
 
        self.kttpeach = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.ktt_peach,
                                                fg_color=("#703E41"),
                                                image=switchImages['ktt_peach']['images']['small'],
                                                text='KTT Peach',
                                                compound='left',
                                                width=140, height=45)
        self.switches_frame_switches.append(self.kttpeach)
 


        self.kttstrawberry = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.ktt_strawberry,
                                                     fg_color=("#703E41"),
                                                     image=switchImages['ktt_strawberry']['images']['small'],
                                                     text='KTT Strawberry',
                                                     compound='left',
                                                     width=140,
                                                     height=45)
        self.switches_frame_switches.append(self.kttstrawberry)
 


        self.lavenderpurp = customtkinter.CTkButton(master=self.switches_frame,
                                                    command=self.akko_lavender_purple,
                                                    fg_color=("#703E41"),
                                                    image=switchImages['akko_lavender_purple']['images']['small'],
                                                    text='Akko Purple',
                                                    compound='left',
                                                    width=140,
                                                    height=45)                                                 
        self.switches_frame_switches.append(self.lavenderpurp)
 


        self.radiantred = customtkinter.CTkButton(master=self.switches_frame,
                                                  command=self.akko_radiant_red,
                                                  fg_color=("#703E41"),
                                                  image=switchImages['akko_radiant_red']['images']['small'],
                                                  text='Akko Red',
                                                  compound='left',
                                                  width=140,
                                                  height=45)
        self.switches_frame_switches.append(self.radiantred)
 


        self.rosered = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.akko_rose_red,
                                               fg_color=("#703E41"),
                                               image=switchImages['akko_rose_red']['images']['small'],
                                               text='Akko Rose',
                                               compound='left',
                                               width=140,
                                               height=45)       
        self.switches_frame_switches.append(self.rosered)
 


        self.zealiosv2 = customtkinter.CTkButton(master=self.switches_frame,
                                                 command=self.zealios_v2,
                                                 fg_color=("#703E41"),
                                                 image=switchImages['zealios_v2']['images']['small'],
                                                 text='ZealiosV2',
                                                 compound='left',
                                                 width=140,
                                                 height=45)    
        self.switches_frame_switches.append(self.zealiosv2)
 


        self.kttwinered = customtkinter.CTkButton(master=self.switches_frame,
                                                  command=self.ktt_winered,
                                                  fg_color=("#703E41"),
                                                  image=switchImages['ktt_wine_red']['images']['small'],
                                                  text='KTT WineRed',
                                                  compound='left',
                                                  width=140,
                                                  height=45)     
        self.switches_frame_switches.append(self.kttstrawberry)
 


        self.cherrymxbrown = customtkinter.CTkButton(master=self.switches_frame,
                                                    command=self.cherry_mx_brown,
                                                    fg_color=("#703E41"),
                                                    image=switchImages['cherry_mx_brown']['images']['small'],
                                                    text='Cherry Brown',
                                                    compound='left',
                                                    width=140,
                                                    height=45)       
        self.switches_frame_switches.append(self.cherrymxbrown)
 


        self.cherrymxclear = customtkinter.CTkButton(master=self.switches_frame,
                            command=self.cherry_mx_clear,
                            fg_color=("#703E41"),
                            image=switchImages['cherry_mx_clear']['images']['small'],
                            text='Cherry Clear',
                            compound='left',
                            width=140,
                            height=45)
        self.switches_frame_switches.append(self.cherrymxclear)
 
            



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    



        # THE FUNCTION TO SHOW THE FRAME AFTER YOU CLICK ON START BUTTON

    def show_the_frame(self):

        
        self.start_button.grid_forget()
        self.keeb_button.grid_forget()
        self.start_text.grid_forget()
        self.start_page_bg.grid_forget()
        self.start_frame.grid_forget()
        self.start_page_logos.grid_forget()
        self.start_title.grid_forget()
        self.start_page_logos2.grid_forget()

        self.show_sidebar_button.place(x= 0, y=30)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        self.logo_label.grid(row=0, column=0, padx=20, pady=40)



        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20)
        self.sidebar_button_4.place(x = 45, y = 355)
        self.sidebar_widget.grid(row=4, column=0, padx=20, pady=15)



        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.main_top.grid(row=0, column=1,padx=20, pady=(10, 20))



        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))  
        self.main_switchset_price.place(x= 750, y= 140)


        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 
        self.main_kit_price.place(x= 750, y= 330)


        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))               
        self.main_keycapset_price.place(x= 750, y= 525)



        self.keyboardkit_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.keyboardkit_frame.grid_columnconfigure(0, weight=1)



        self.keycaps_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.keycaps_frame.grid_columnconfigure(0, weight=1)	



        self.switches_frame.grid(row=3, column=1, columnspan=3, sticky="nsew")
        self.switches_frame.grid_columnconfigure(0, weight=1)
        


        self.tofu60.grid(row=1, column=0, padx=10, pady=(0, 20))
        self.tofu65.grid(row=2, column=0, padx=10, pady=(0, 20))
        self.tester68.grid(row=3, column=0, padx=10, pady=(0, 20))
        self.tester84.grid(row=4, column=0, padx=10, pady=(0, 20))
        self.gmk67.grid(row=5, column=0, padx=10, pady=(0, 20))
        self.gas67.grid(row=6, column=0, padx=10, pady=(0, 20))
        self.everglide75.grid(row=7, column=0, padx=10, pady=(0, 20))
        self.mk870.grid(row=8, column=0, padx=10, pady=(0, 20))
        self.monsgeekm1.grid(row=9, column=0, padx=10, pady=(0, 20))
        self.nexttime75.grid(row=10, column=0, padx=10, pady=(0, 20))
        self.nj80.grid(row=11, column=0, padx=10, pady=(0, 20))
        self.tm680.grid(row=12, column=0, padx=10, pady=(0, 20))



        self.dcx9009.grid(row=1, column=0, padx=10, pady=(0, 20))
        self.dcxblackonwhite.grid(row=2, column=0, padx=10, pady=(0, 20))
        self.dcxwhiteonblack.grid(row=3, column=0, padx=10, pady=(0, 20))
        self.dcxcyber.grid(row=4, column=0, padx=10, pady=(0, 20))
        self.dcxhyperfuse.grid(row=5, column=0, padx=10, pady=(0, 20))
        self.dcxkeyman.grid(row=6, column=0, padx=10, pady=(0, 20))
        self.dcxviolac.grid(row=7, column=0, padx=10, pady=(0, 20))
        self.gmkarmstrong.grid(row=8, column=0, padx=10, pady=(0, 20))
        self.gmkbluesamurai.grid(row=9, column=0, padx=10, pady=(0, 20))
        self.gmkdots.grid(row=10, column=0, padx=10, pady=(0, 20))
        self.gmkkaiju.grid(row=11, column=0, padx=10, pady=(0, 20))
        self.gmklaser.grid(row=12, column=0, padx=10, pady=(0, 20))



        self.c3kiwi.grid(row=1, column=0, padx=10, pady=(0, 20))
        self.c3tang.grid(row=1, column=1, padx=10, pady=(0, 20))
        self.boxjade.grid(row=1, column=2, padx=10, pady=(0, 20))
        self.boxnavy.grid(row=1, column=3, padx=10, pady=(0, 20))
        self.glopanda.grid(row=1, column=4, padx=10, pady=(0, 20))
        self.holpanda.grid(row=1, column=5, padx=10, pady=(0, 20))
        self.gateronblackinkv2.grid(row=1, column=6, padx=10, pady=(0, 20))
        self.gateronoilking.grid(row=1, column=7, padx=10, pady=(0, 20))
        self.nkcreams.grid(row=1, column=8, padx=10, pady=(0, 20))
        self.kangwhitev3.grid(row=1, column=9, padx=10, pady=(0, 20))
        self.kttgrapefruit.grid(row=1, column=10, padx=10, pady=(0, 20))
        self.kttpeach.grid(row=1, column=11, padx=10, pady=(0, 20))
        self.kttstrawberry.grid(row=1, column=12, padx=10, pady=(0, 20))
        self.lavenderpurp.grid(row=1, column=13, padx=10, pady=(0, 20))
        self.radiantred.grid(row=1, column=14, padx=10, pady=(0, 20))
        self.rosered.grid(row=1, column=15, padx=10, pady=(0, 20))
        self.zealiosv2.grid(row=1, column=16, padx=10, pady=(0, 20))
        self.kttwinered.grid(row=1, column=17, padx=10, pady=(0, 20))
        self.cherrymxbrown.grid(row=1, column=18, padx=10, pady=(0, 20))
        self.cherrymxclear.grid(row=1, column=19, padx=10, pady=(0, 20))
        

    def show_sidebar(self):
        
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        
        self.main_switchset_price.place(x= 860, y= 140)
        self.main_kit_price.place(x= 860, y= 330)
        self.main_keycapset_price.place(x= 860, y= 525)


        self.logo_label.grid(row=0, column=0, padx=20, pady=40)




        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=20)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=20)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=20)
        self.sidebar_button_4.place(x = 45, y = 355)
        self.sidebar_widget.grid(row=4, column=0, padx=20, pady=15)
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.show_sidebar_button.place_forget()
        self.hide_sidebar_button.place(x=0, y=30)

        
    def hide_sidebar(self):
        
        self.sidebar_frame.grid_forget()
        
        self.logo_label.grid_forget()
        
        self.sidebar_button_1.grid_forget()
        self.sidebar_button_2.grid_forget()
        self.sidebar_button_3.grid_forget()
        self.sidebar_button_4.grid_forget()
        
        self.sidebar_widget.grid_forget()
        
            
        self.main_switchset_price.place(x= 750, y= 140)
        self.main_kit_price.place(x= 750, y= 330)
        self.main_keycapset_price.place(x= 750, y= 525)
        
        self.hide_sidebar_button.place_forget()
        self.show_sidebar_button.place(x=0, y=30)

        
        
    def show_keeb(self):
        
        self.start_button.grid_forget()
        self.keeb_button.grid_forget()
        self.start_text.grid_forget()
        self.start_page_bg.grid_forget()
        self.start_frame.grid_forget()
        self.start_page_logos.grid_forget()
        self.start_title.grid_forget()
        self.start_page_logos2.grid_forget()
        
        self.image = customtkinter.CTkLabel(self,
                                            image= keyboardImages["image0"]["images"]["large"],
                                            text=  keyboards["image0"]["description"],
                                            font= customtkinter.CTkFont(family= "Microsoft New Tai Lue" ,size=20,weight="bold"),
                                            compound= 'top',
                                            pady= 20)
        self.image.place(x = 175, y = 100)
        
        self.next = customtkinter.CTkButton(self,
                                            text=  "Next",
                                            width= 100,
                                            height = 50)
        self.next.place(x = 1150, y = 350)
        
        
        
        
        # all the functions to change the Main_Label's image to the clicked button's keyboard kit
    def tofu_60(self):
        tofu60_link = 'https://kbdfans.com/products/tofu60-2-0'
        tofu60_response  = requests.get(tofu60_link)

        tf60_soup = BeautifulSoup(tofu60_response.content, 'html.parser')
        tofu60_tag = tf60_soup.find('span', {'class': 'theme-money large-title'})

        tofu60_price = tofu60_tag.text.strip()

        self.main_kit.configure(text= 'Tofu 60 2.0',
                                command= lambda: webbrowser.open(keyboard_kits['tofu60']['review_link']),
                                image=kitImages['tofu60']['images']['large'],
                                font=customtkinter.CTkFont(family= "Microsoft New Tai Lue", weight="bold"),
                                height=130,
                                width=350,)
        
        self.main_kit_price.configure(text= tofu60_price,
                                      command= lambda: webbrowser.open(keyboard_kits['tofu60']['link']),    
                                      image= otherImages['buy']['images']['small'],
                                      compound= 'bottom')
        
        #self.main_kit_price.grid(row=0, column=2, rowspan=2,padx=0, pady=0)  (TEST)

    def tofu_65(self):

        tofu65_link = 'https://kbdfans.com/collections/tofu65/products/tofu65-2-0'
        tofu65_response  = requests.get(tofu65_link)

        tf65_soup = BeautifulSoup(tofu65_response.content, 'html.parser')
        tofu65_tag = tf65_soup.find('span', {'class': 'theme-money large-title'})

        tofu65_price = tofu65_tag.text.strip()

        self.main_kit.configure(compound="top",                            
                                command= lambda: webbrowser.open(keyboard_kits['tofu65']['review_link']),
                                image=kitImages['tofu65']['images']['large'],
                                text= 'Tofu 65 2.0',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  command= lambda: webbrowser.open(keyboard_kits['tofu65']['link']),          
                                        text= tofu65_price,
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')

    
    def tester_68(self):

        tester68_link = 'https://www.yunzii.com/products/ciy-tester-68-hot-swappable-transparent-mechanical-keyboard-kit'
        tester68_response  = requests.get(tester68_link)

        tester68_soup = BeautifulSoup(tester68_response.content, 'html.parser')
        tester68_tag = tester68_soup.find('span', {'class': 'money'})

        tester68_price =  tester68_tag.text.strip()

        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['tester68']['review_link']),
                                image=kitImages['tester68']['images']['large'],
                                text= 'Tester 68',
                                height=130,
                                width=350)
        
        self.main_kit_price.configure(  text= tester68_price,
                                        command= lambda: webbrowser.open(keyboard_kits['tester68']['link']),    
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')

    def tester_84(self):

        tester84_link = 'https://www.yunzii.com/products/ciy-tester-84-hot-swappable-transparent-keyboard-kit'
        tester84_response  = requests.get(tester84_link)

        tester84_soup = BeautifulSoup(tester84_response.content, 'html.parser')
        tester84_tag = tester84_soup.find('span', {'class': 'money'})

        tester84_price = tester84_tag.text.strip()

        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['tester84']['review_link']),
                                image=kitImages['tester84']['images']['large'],
                                text= 'Tester 84',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  text= tester84_price,
                                        command= lambda: webbrowser.open(keyboard_kits['tester84']['link']),    
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')


    def gmk_67(self):

        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['gmk67']['review_link']),
                                image=kitImages['gmk67']['images']['large'],
                                text= 'GMK 67',
                                height=130,
                                width=360)

        self.main_kit_price.configure(  text= "$30-$50",
                                        command= lambda: webbrowser.open(keyboard_kits['gmk67']['link']),    
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')

    def gas_67(self):

        gas67_link = 'https://landingpad.shop/products/ciy-gas67-keyboard-diy-kit'
        gas67_response  = requests.get(gas67_link)

        gas67_soup = BeautifulSoup(gas67_response.content, 'html.parser')
        gas67_tag = gas67_soup.find('span', {'class': 'price-item price-item--regular !text-white'})

        gas67_price = gas67_tag.text.strip()


        self.main_kit.configure(compound="top",                            
                                command =  lambda: webbrowser.open(keyboard_kits['gas67']['review_link']),
                                image=kitImages['gas67']['images']['large'],
                                text= 'GAS 67',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  text= gas67_price,
                                        command= lambda: webbrowser.open(keyboard_kits['gas67']['link']),    
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')

    def everglide_75(self):

        eg75_link = 'https://epomaker.com/products/everglide-lite-75-kit?variant=40026310279241'
        eg75_response  = requests.get(eg75_link)

        eg75_soup = BeautifulSoup(eg75_response.content, 'html.parser')
        eg75_tag = eg75_soup.find('span', {'class': 'money'})

        eg75_price = eg75_tag.text.strip()



        self.main_kit.configure(compound="top",                            
                                command =  lambda: webbrowser.open(keyboard_kits['everglide75']['review_link']),
                                image=kitImages['everglide75']['images']['large'],
                                text= 'Everglide Lite 75',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  text= eg75_price,
                                        command= lambda: webbrowser.open(keyboard_kits['everglide75']['link']),   
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')


    def mk_870(self):

        mk_870_link = 'https://kprepublic.com/en-de/products/flesports-mk870-mechanical-keyboard-kit-full-rgb-backlit-led-hot-swappable-socket-nkro-programmable-usb-c-transparent-black-case'
        mk_870_response  = requests.get(mk_870_link)

        mk_870_soup = BeautifulSoup(mk_870_response.content, 'html.parser')
        mk_870_tag = mk_870_soup.find('span', {'class': 'money'})

        mk_870_price = mk_870_tag.text.strip()



        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['mk870']['review_link']),
                                image=kitImages['mk870']['images']['large'],
                                text= 'MK 870',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  text= mk_870_price,
                                        command= lambda: webbrowser.open(keyboard_kits['mk870']['link']),   
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')


    def monsgeek_m1(self):

        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['monsgeekm1']['review_link']),
                                image=kitImages['monsgeekm1']['images']['large'],
                                text= 'Monsgeek M1',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  text= "$99.99",
                                        command= lambda: webbrowser.open(keyboard_kits['monsgeekm1']['link']),   
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')


    def nexttime_75(self):

        nt_75_link = 'https://kprepublic.com/en-de/products/nexttime-x75-75-gasket-mechanical-keyboard-kit-pcb-hot-swappable-switch-lighting-effects-rgb-switch-led-type-c-next-time-75'
        nt_75_response  = requests.get(nt_75_link)

        nt_75_soup = BeautifulSoup(nt_75_response.content, 'html.parser')
        nt_75_tag = nt_75_soup.find('span', {'class': 'money'})

        nt_75_price = nt_75_tag.text.strip()


        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['nexttime75']['review_link']),
                                image=kitImages['nexttime75']['images']['large'],
                                text= 'Next Time 75',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  text= nt_75_price,
                                        command= lambda: webbrowser.open(keyboard_kits['nexttime75']['link']),   
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')


    def nj_80(self):

        nj_80_link = 'https://www.keebmonkey.com/products/nj80'
        nj_80_response  = requests.get(nj_80_link)

        nj_80_soup = BeautifulSoup(nj_80_response.content, 'html.parser')
        nj_80_tag = nj_80_soup.find('span', {'class': 'tlab-currency-format'})

        nj_80_price = nj_80_tag.text.strip()




        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['nj80']['review_link']),
                                image=kitImages['nj80']['images']['large'],
                                text= 'NJ 80',
                                height=130,
                                width=350)

        self.main_kit_price.configure(  text= nj_80_price,
                                        command= lambda: webbrowser.open(keyboard_kits['nj80']['link']),   
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')


    def tm_680(self):


        self.main_kit.configure(compound="top",                            
                                command = lambda: webbrowser.open(keyboard_kits['tm680']['review_link']),
                                image=kitImages['tm680']['images']['large'],
                                text= 'TM 680',
                                height=125,
                                width=350)

        self.main_kit_price.configure(  text= "$45 - $65",
                                        command= lambda: webbrowser.open(keyboard_kits['tm680']['link']),   
                                        image= otherImages['buy']['images']['small'],
                                        compound= 'bottom')










        # all the functions to change the Main_Button's image to the clicked button's keycap set
    def gmk_dots(self):

        dots_link = 'https://oblotzky.industries/products/gmk-dots-2'
        dots_response  = requests.get(dots_link)

        dots_soup = BeautifulSoup(dots_response.content, 'html.parser')
        dots_tag = dots_soup.find('span', {'class': 'product-single__price'})

        dots_price = dots_tag.text.strip()




        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['gmk_dots']['review_link']),
                                        image=keycapImages['gmk_dots']['images']['large'],
                                        text= 'GMK Dots 2.0',
                                        height=130,
                                        width=350)


        self.main_keycapset_price.configure(text= dots_price,
                                            command= lambda: webbrowser.open(keycap_sets['gmk_dots']['link']),   
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')       
    def gmk_armstrong(self):

        dots_link = 'https://oblotzky.industries/products/gmk-dots-2'
        dots_response  = requests.get(dots_link)

        dots_soup = BeautifulSoup(dots_response.content, 'html.parser')
        dots_tag = dots_soup.find('span', {'class': 'product-single__price'})

        dots_price = dots_tag.text.strip()

        self.main_keycapset.configure(  compound="top",                            
                                        command =  lambda: webbrowser.open(keycap_sets['gmk_armgstrong']['review_link']),                                              
                                        image=keycapImages['gmk_armstrong']['images']['large'],
                                        text= 'GMK GodSpeed',
                                        height=130,
                                        width=350)

        self.main_keycapset_price.configure(text= dots_price,
                                            command= lambda: webbrowser.open(keycap_sets['gmk_armstrong']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    def gmk_bluesamurai(self):

        dots_link = 'https://oblotzky.industries/products/gmk-dots-2'
        dots_response  = requests.get(dots_link)

        dots_soup = BeautifulSoup(dots_response.content, 'html.parser')
        dots_tag = dots_soup.find('span', {'class': 'product-single__price'})

        dots_price = dots_tag.text.strip()

        self.main_keycapset.configure(  compound="top",                            
                                        command =  lambda: webbrowser.open(keycap_sets['gmk_bluesamurai']['review_link']),                                               
                                        image=keycapImages['gmk_bluesamurai']['images']['large'],
                                        text= 'GMK Blue Samurai',
                                        height=130,
                                        width=350)


        self.main_keycapset_price.configure(text= dots_price,
                                            command= lambda: webbrowser.open(keycap_sets['gmk_bluesamurai']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def gmk_kaiju(self):

        kaiju_link = 'https://oblotzky.industries/products/gmk-dots-2'
        kaiju_response  = requests.get(kaiju_link)

        kaiju_soup = BeautifulSoup(kaiju_response.content, 'html.parser')
        kaiju_tag = kaiju_soup.find('span', {'id': 'ProductPrice'})

        kaiju_price = kaiju_tag.text.strip()

        self.main_keycapset.configure(  compound="top",                            
                                        command =  lambda: webbrowser.open(keycap_sets['gmk_kaiju']['review_link']),                                             
                                        image=keycapImages['gmk_kaiju']['images']['large'],
                                        text= 'GMK Kaiju',
                                        height=130,
                                        width=350)
 

        self.main_keycapset_price.configure(text= kaiju_price,
                                            command= lambda: webbrowser.open(keycap_sets['gmk_kaiju']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')
    def gmk_laser(self):

        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['gmk_laser']['review_link']),                                              
                                        image=keycapImages['gmk_laser']['images']['large'],
                                        text= 'GMK Laser',
                                        height=130,
                                        width=350)

        self.main_keycapset_price.configure(text= "$150.00",
                                            command= lambda: webbrowser.open(keycap_sets['gmk_laser']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    def dcx_9009(self):

        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['dcx_9009']['review_link']),                                            
                                        image=keycapImages['dcx_9009']['images']['large'],
                                        text= 'DCX 9009',
                                        height=130,
                                        width=350)  

        self.main_keycapset_price.configure(text="$99.00",
                                            command= lambda: webbrowser.open(keycap_sets['dcx_9009']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    def dcx_black_on_white(self):

        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['dcx_bow']['review_link']),                                        
                                        image=keycapImages['dcx_bow']['images']['large'],
                                        text= 'DCX Black On White',
                                        height=130,
                                        width=350)

        self.main_keycapset_price.configure(text= "$79.00",
                                            command= lambda: webbrowser.open(keycap_sets['dcx_bow']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')
    def dcx_white_on_black(self):
        

        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['dcx_wob']['review_link']),                                          
                                        image=keycapImages['dcx_wob']['images']['large'],
                                        text= 'DCX White On Black',
                                        height=130,
                                        width=350)

        self.main_keycapset_price.configure(text= "$79.00",
                                            command= lambda: webbrowser.open(keycap_sets['dcx_wob']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')   
    def dcx_cyber(self):

        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['dcx_cyber']['review_link']),                                             
                                        image=keycapImages['dcx_cyber']['images']['large'],
                                        text= 'DCX Cyber',
                                        height=130,
                                        width=350)   

        self.main_keycapset_price.configure(text= "$99.00",
                                            command= lambda: webbrowser.open(keycap_sets['dcx_cyber']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')
                                 
    def dcx_hyperfuse(self):

        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['dcx_hyperfuse']['review_link']),
                                        image=keycapImages['dcx_hyperfuse']['images']['large'],
                                        text= 'DCX Hyperfuse',
                                        height=130,
                                        width=350)
        
        self.main_keycapset_price.configure(text= "$99.00",
                                            command= lambda: webbrowser.open(keycap_sets['dcx_hyperfuse']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    
    def dcx_keyman(self):

        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['dcx_keyman']['review_link']),
                                        image=keycapImages['dcx_keyman']['images']['large'],
                                        text= 'DCX Keyman',
                                        height=130,
                                        width=350)


        self.main_keycapset_price.configure(text= "$99.00",
                                            command= lambda: webbrowser.open(keycap_sets['dcx_keyman']['link']),  
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')
    def dcx_violac(self):
        
        self.main_keycapset.configure(  compound="top",                            
                                        command = lambda: webbrowser.open(keycap_sets['dcx_violac']['review_link']),                                            
                                        image=keycapImages['dcx_violac']['images']['large'],
                                        text= 'DCX Violac',
                                        height=130,
                                        width=350)   

        self.main_keycapset_price.configure(text= "$99.00",
                                            command= lambda: webbrowser.open(keycap_sets['dcx_violac']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')




        # all the functions to change the Main_Button's image to the clicked button's switch set 
    def c3_kiwi(self):

        c3kiwi_link = 'https://thekey.company/products/c3-equalz-x-tkc-kiwi-switches?variant=39513713606745'
        c3kiwi_response  = requests.get(c3kiwi_link)

        c3kiwi_soup = BeautifulSoup(c3kiwi_response.content, 'html.parser')
        c3kiwi_tag = c3kiwi_soup.find('span', {'class': 'product-single__price'})

        c3kiwi_price = c3kiwi_tag.text.strip()

        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['c3_kiwi']['review_link']),                                           
                                    image=switchImages['c3_kiwi']['images']['large'],
                                    text= 'C3 Kiwi',
                                    height=180,
                                    width=200)

        self.main_switchset_price.configure(text= c3kiwi_price,
                                            command= lambda: webbrowser.open(switch_sets['c3_kiwi']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    def c3_tangerine(self):
        
        c3tang_link = 'https://thekey.company/products/tangerine-switches?variant=40056847827033'
        c3tang_response  = requests.get(c3tang_link)

        c3tang_soup = BeautifulSoup(c3tang_response.content, 'html.parser')
        c3tang_tag = c3tang_soup.find('span', {'class': 'product-single__price'})

        c3tang_price = c3tang_tag.text.strip()


        self.main_switch.configure( compound="top",                            
                                    command =  lambda: webbrowser.open(switch_sets['c3_tangerine']['review_link']),   
                                    image=switchImages['c3_tangerine']['images']['large'],                                          
                                    text= 'C3 Tangerine V2',
                                    height=180,
                                    width=200)

        self.main_switchset_price.configure(text= c3tang_price,
                                            command= lambda: webbrowser.open(switch_sets['c3_tangerine']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def box_jade(self):

        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['box_jade']['review_link']),                                                
                                    image=switchImages['box_jade']['images']['large'],
                                    text= 'Box Jade',
                                    height=180,
                                    width=200)

        self.main_switchset_price.configure(text= "$30.00",
                                            command= lambda: webbrowser.open(switch_sets['box_jade']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    def box_navy(self):

        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['box_navy']['review_link']),                                                
                                    image=switchImages['box_navy']['images']['large'],
                                    text= 'Box Navy',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "Restocking \n Q2 2023",
                                            command= None,
                                            #command= lambda: webbrowser.open(switch_sets['box_navy']['link']), 
                                            #image= otherImages['buy']['images']['small'],                                            
                                            image= None,
                                            compound= 'bottom'
                                            )


    def holy_panda(self):

        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['holy_panda']['review_link']),                                               
                                    image=switchImages['holy_panda']['images']['large'],
                                    text= 'Holy Panda',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$60.00",
                                            command= lambda: webbrowser.open(switch_sets['holy_panda']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def glorious_panda(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['glorious_panda']['review_link']),                                          
                                    image=switchImages['glorious_panda']['images']['large'],
                                    text= 'Glorious Panda',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$40-50",
                                            command= lambda: webbrowser.open(switch_sets['glorious_panda']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def gateron_black_ink_v2(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['gateron_ink_black_v2']['review_link']),                                             
                                    image=switchImages['gateron_ink_black_v2']['images']['large'],
                                    text= 'Gateron Black Ink V2',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$52.00",
                                            command= lambda: webbrowser.open(switch_sets['gateron_ink_black_v2']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def gateron_oil_king(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['gateron_oilking']['review_link']),                                           
                                    image=switchImages['gateron_oilking']['images']['large'],
                                    text= 'Gateron Oil King',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$47.00",
                                            command= lambda: webbrowser.open(switch_sets['gateron_oilking']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    
    def nk_creams(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['novelkey_cream']['review_link']),                                     
                                    image=switchImages['novelkey_cream']['images']['large'],
                                    text= 'Nk Cream',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "Restocking \n Q2 2023",
                                        #   command= lambda: webbrowser.open(switch_sets['novelkey_cream']['link']), 
                                        #   image= otherImages['buy']['images']['small'],
                                            command= None,
                                            image= None,
                                            compound= 'bottom'
                                            )


    def kang_white_v3(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['ktt_kang_white_v3']['review_link']),                                        
                                    image=switchImages['ktt_kang_white_v3']['images']['large'],
                                    text= 'KTT Kang White V3',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$15,60",
                                            command= lambda: webbrowser.open(switch_sets['ktt_kang_white_v3']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def ktt_grapefruit(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['ktt_grapefruit']['review_link']),                                              
                                    image=switchImages['ktt_grapefruit']['images']['large'],
                                    text= 'KTT Grapefruit',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$20.55",
                                            command= lambda: webbrowser.open(switch_sets['ktt_grapefruit']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def ktt_peach(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['ktt_peach']['review_link']),                                                 
                                    image=switchImages['ktt_peach']['images']['large'],
                                    text= 'KTT Peach',
                                    height=180,
                                    width=200)
    
        self.main_switchset_price.configure(text= "$20.55",
                                            command= lambda: webbrowser.open(switch_sets['ktt_peach']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def ktt_strawberry(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['ktt_strawberry']['review_link']),                                             
                                    image=switchImages['ktt_strawberry']['images']['large'],
                                    text= 'KTT Strawberry',
                                    height=180,
                                    width=200)

        self.main_switchset_price.configure(text= "$19.50",
                                            command= lambda: webbrowser.open(switch_sets['ktt_strawberry']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')



    def akko_lavender_purple(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['akko_lavender_purple']['review_link']),                                             
                                    image=switchImages['akko_lavender_purple']['images']['large'],
                                    text= 'Akko CS Lavender Purple',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$22.05",
                                            command= lambda: webbrowser.open(switch_sets['akko_lavender_purple']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def akko_radiant_red(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['akko_radiant_red']['review_link']),                                     
                                    image=switchImages['akko_radiant_red']['images']['large'],
                                    text= 'Akko CS Radiant Red',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$22.05",
                                            command= lambda: webbrowser.open(switch_sets['akko_radiant_red']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

 
    def akko_rose_red(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['akko_rose_red']['review_link']),                                            
                                    image=switchImages['akko_rose_red']['images']['large'],
                                    text= 'Akko CS Rose Red',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$22.05",
                                            command= lambda: webbrowser.open(switch_sets['akko_rose_red']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def zealios_v2(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['zealios_v2']['review_link']),                                         
                                    image=switchImages['zealios_v2']['images']['large'],
                                    text= 'Zealios V2',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$75.00",
                                            command= lambda: webbrowser.open(switch_sets['zealios_v2']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def ktt_winered(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['ktt_wine_red']['review_link']),                                              
                                    image=switchImages['ktt_wine_red']['images']['large'],
                                    text= 'KTT Wine Red',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$19.50",
                                            command= lambda: webbrowser.open(switch_sets['ktt_wine_red']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    def cherry_mx_brown(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['cherry_mx_brown']['review_link']),                                                  
                                    image=switchImages['cherry_mx_brown']['images']['large'],
                                    text= 'Cherry MX Brown',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$42.00",
                                            command= lambda: webbrowser.open(switch_sets['cherry_mx_brown']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')


    def cherry_mx_clear(self):
        self.main_switch.configure( compound="top",                            
                                    command = lambda: webbrowser.open(switch_sets['cherry_mx_clear']['review_link']),                                             
                                    image=switchImages['cherry_mx_clear']['images']['large'],
                                    text= 'Cherry MX Clear',
                                    height=180,
                                    width=200)
        
        self.main_switchset_price.configure(text= "$52.00",
                                            command= lambda: webbrowser.open(switch_sets['cherry_mx_clear']['link']), 
                                            image= otherImages['buy']['images']['small'],
                                            compound= 'bottom')

    


   # Creates an object and uses multiprocessing
if __name__ == "__main__":
    app = App()
    app.mainloop()
