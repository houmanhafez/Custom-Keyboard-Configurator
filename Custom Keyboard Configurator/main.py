from data import keyboard_kits_reviews, keycap_sets_reviews, switch_sets_reviews, other_links
import time
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
import PIL
import tkinter.messagebox
import customtkinter
import webbrowser



customtkinter.set_appearance_mode("Dark")  # Modes: "System", "Dark", "Light"
customtkinter.set_default_color_theme('blue')  # Themes: "blue", "green", "dark-blue"


#Keyboard Kit Images
tofu60 = customtkinter.CTkImage(Image.open("Keeb/Tofu60.jpg"),
                                          size=(120, 40))
tofu65 = customtkinter.CTkImage(Image.open("Keeb/Tofu65.jpg"),
                                          size=(120, 40))
tester68 = customtkinter.CTkImage(Image.open("Keeb/tester68.jpg"),
                                          size=(110, 40))
tester84 = customtkinter.CTkImage(Image.open("Keeb/Tester84.jpg"),
                                          size=(110, 40))
gmk67 = customtkinter.CTkImage(Image.open("Keeb/gmk67.jpg"),
                                          size=(120, 40))
gas67 = customtkinter.CTkImage(Image.open("Keeb/gas67.jpg"),
                                          size=(120, 40))
everglide75 = customtkinter.CTkImage(Image.open("Keeb/Everglide Lite 75.jpg"),
                                          size=(120, 40))
mk870 = customtkinter.CTkImage(Image.open("Keeb/MK870.jpg"),
                                          size=(120, 40))
monsgeekm1 = customtkinter.CTkImage(Image.open("Keeb/Monsgeek M1.jpg"),
                                          size=(120, 40))
nexttime75 = customtkinter.CTkImage(Image.open("Keeb/Nexttime 75.jpg"),
                                          size=(120, 40))
nj80 = customtkinter.CTkImage(Image.open("Keeb/NJ80.jpg"),
                                          size=(120, 40))
tm680 = customtkinter.CTkImage(Image.open("Keeb/TM680.jpg"),
                                          size=(111, 38))


#Keycap Set Images
gmk_dots = customtkinter.CTkImage(Image.open("keycap sets/gmkdots.jpg"),
                                          size=(125, 35))
gmk_armstrong = customtkinter.CTkImage(Image.open("keycap sets/gmkarmstrong.jpg"),
                                          size=(125, 35))
gmk_bluesamurai = customtkinter.CTkImage(Image.open("keycap sets/gmkbluesamurai.jpg"),
                                          size=(125, 35))
gmk_kaiju = customtkinter.CTkImage(Image.open("keycap sets/gmkkaiju.jpg"),
                                          size=(125, 35))        
gmk_laser = customtkinter.CTkImage(Image.open("keycap sets/gmklaser.jpg"),
                                          size=(120, 35))       
dcx_9009 = customtkinter.CTkImage(Image.open("keycap sets/dcx9009.jpg"),
                                          size=(130, 35))
dcx_blackonwhite = customtkinter.CTkImage(Image.open("keycap sets/dcxblackonwhite.jpg"),
                                          size=(120, 35))
dcx_whiteonblack = customtkinter.CTkImage(Image.open("keycap sets/dcxwhiteonblack.jpg"),
                                          size=(120, 38))
dcx_cyber = customtkinter.CTkImage(Image.open("keycap sets/dcxcyber.jpg"),
                                          size=(125, 37))
dcx_hyperfuse = customtkinter.CTkImage(Image.open("keycap sets/dcxhyperfuse.jpg"),
                                          size=(115, 35))
dcx_keyman = customtkinter.CTkImage(Image.open("keycap sets/dcxkeyman.jpg"),
                                          size=(118, 35))
dcx_violac = customtkinter.CTkImage(Image.open("keycap sets/dcxviolac.jpg"),
                                          size=(120, 35))


#Switch Set Images
kttpeach = customtkinter.CTkImage(Image.open("Switches/kttpeach.jpg"),
                                          size=(40, 40))
gateronblack = customtkinter.CTkImage(Image.open("Switches/Gateronblackinkv2.jpg"),
                                          size=(40, 40))     
gatoilking = customtkinter.CTkImage(Image.open("Switches/gateronoilking.jpg"),
                                          size=(40, 40))      
grapefruit = customtkinter.CTkImage(Image.open("Switches/kttgrapefruit.jpg"),
                                          size=(40, 40))   
kangwhitev3 = customtkinter.CTkImage(Image.open("Switches/Kangwhitev3.jpg"),
                                          size=(40, 40))       
nkcream = customtkinter.CTkImage(Image.open("Switches/kailhcream.jpg"),
                                          size=(40, 40))
holpanda = customtkinter.CTkImage(Image.open("Switches/holypanda.jpg"),
                                          size=(40, 40))       
glopanda = customtkinter.CTkImage(Image.open("Switches/gloriouspanda.jpg"),
                                          size=(40, 40))       
c3tang = customtkinter.CTkImage(Image.open("Switches/c3tangerine.jpg"),
                                          size=(40, 40))
c3kiwi = customtkinter.CTkImage(Image.open("Switches/c3kiwi.jpg"),
                                          size=(40, 40))       
boxnavy= customtkinter.CTkImage(Image.open("Switches/boxnavy.jpg"),
                                          size=(40, 40))      
boxjade = customtkinter.CTkImage(Image.open("Switches/boxjade.jpg"),
                                          size=(40, 40))      
lavenderpurp = customtkinter.CTkImage(Image.open("Switches/lavenderpurple.jpg"),
                                          size=(40, 40))       
radiantred = customtkinter.CTkImage(Image.open("Switches/RadiantRed.jpg"),
                                          size=(40, 40))       
rosered = customtkinter.CTkImage(Image.open("Switches/rosered.jpg"),
                                          size=(40, 40))       
zealiosv2 = customtkinter.CTkImage(Image.open("Switches/zealiosv2.jpg"),
                                          size=(40, 40))       
kttwinered = customtkinter.CTkImage(Image.open("Switches/kttwinered.jpg"),
                                          size=(40, 40))       
kttstrawberry = customtkinter.CTkImage(Image.open("Switches/kttstrawberry.jpg"),
                                          size=(40, 40))       
mxbrown = customtkinter.CTkImage(Image.open("Switches/cherrymxbrown.jpg"),
                                          size=(40, 40))        
mxclear = customtkinter.CTkImage(Image.open("Switches/cherrymxclear.jpg"),
                                          size=(40, 40))
        


#Keyboard Kit Images for the Main_Frame
tofu60_1 = customtkinter.CTkImage(Image.open("Keeb/Tofu60.jpg"),
                                        size=(360, 150))
tofu65_1 = customtkinter.CTkImage(Image.open("Keeb/Tofu65.jpg"),
                                        size=(360, 150))
tester68_1 = customtkinter.CTkImage(Image.open("Keeb/tester68.jpg"),
                                        size=(360, 140))
tester84_1 = customtkinter.CTkImage(Image.open("Keeb/Tester84.jpg"),
                                        size=(360, 140))
gmk67_1 = customtkinter.CTkImage(Image.open("Keeb/gmk67.jpg"),
                                        size=(360, 140))
gas67_1 = customtkinter.CTkImage(Image.open("Keeb/gas67.jpg"),
                                        size=(360, 150))
everglide75_1 = customtkinter.CTkImage(Image.open("Keeb/Everglide Lite 75.jpg"),
                                        size=(360, 150))
mk870_1 = customtkinter.CTkImage(Image.open("Keeb/MK870.jpg"),
                                        size=(360, 150))
monsgeekm1_1 = customtkinter.CTkImage(Image.open("Keeb/Monsgeek M1.jpg"),
                                        size=(360, 150))
nexttime75_1 = customtkinter.CTkImage(Image.open("Keeb/Nexttime 75.jpg"),
                                        size=(360, 140))
nj80_1 = customtkinter.CTkImage(Image.open("Keeb/NJ80.jpg"),
                                        size=(360, 150))
tm680_1 = customtkinter.CTkImage(Image.open("Keeb/TM680.jpg"),
                                        size=(360, 150))


#Keycap Set Images for the Main_Frame
gmk_dots_1 = customtkinter.CTkImage(Image.open("keycap sets/gmkdots.jpg"),
                                         size=(350, 120))       
gmk_armstrong_1 = customtkinter.CTkImage(Image.open("keycap sets/gmkarmstrong.jpg"),
                                         size=(350, 120))
gmk_bluesamurai_1 = customtkinter.CTkImage(Image.open("keycap sets/gmkbluesamurai.jpg"),
                                         size=(350, 120))
gmk_kaiju_1 = customtkinter.CTkImage(Image.open("keycap sets/gmkkaiju.jpg"),
                                         size=(350, 120))       
gmk_laser_1 = customtkinter.CTkImage(Image.open("keycap sets/gmklaser.jpg"),
                                         size=(350, 120))        
dcx_9009_1 = customtkinter.CTkImage(Image.open("keycap sets/dcx9009.jpg"),
                                         size=(350, 120))        
dcx_blackonwhite_1 = customtkinter.CTkImage(Image.open("keycap sets/dcxblackonwhite.jpg"),
                                         size=(350, 120))        
dcx_whiteonblack_1 = customtkinter.CTkImage(Image.open("keycap sets/dcxwhiteonblack.jpg"),
                                         size=(350, 120))        
dcx_cyber_1 = customtkinter.CTkImage(Image.open("keycap sets/dcxcyber.jpg"),
                                         size=(350, 120))        
dcx_hyperfuse_1 = customtkinter.CTkImage(Image.open("keycap sets/dcxhyperfuse.jpg"),
                                         size=(350, 120))        
dcx_keyman_1 = customtkinter.CTkImage(Image.open("keycap sets/dcxkeyman.jpg"),
                                         size=(350, 120))        
dcx_violac_1 = customtkinter.CTkImage(Image.open("keycap sets/dcxviolac.jpg"),
                                         size=(350, 120))


#Switch set Images for the Main_Frame
kttpeach_1 = customtkinter.CTkImage(Image.open("Switches/kttpeach.jpg"),
                                          size=(100, 90)) 
gateronblack_1 = customtkinter.CTkImage(Image.open("Switches/Gateronblackinkv2.jpg"),
                                          size=(100, 90))      
gatoilking_1 = customtkinter.CTkImage(Image.open("Switches/gateronoilking.jpg"),
                                          size=(100, 90))      
grapefruit_1 = customtkinter.CTkImage(Image.open("Switches/kttgrapefruit.jpg"),
                                          size=(100, 90))   
kangwhitev3_1 = customtkinter.CTkImage(Image.open("Switches/Kangwhitev3.jpg"),
                                          size=(100, 90))       
nkcream_1 = customtkinter.CTkImage(Image.open("Switches/kailhcream.jpg"),
                                          size=(100, 90))
holpanda_1 = customtkinter.CTkImage(Image.open("Switches/holypanda.jpg"),
                                          size=(100, 90))       
glopanda_1 = customtkinter.CTkImage(Image.open("Switches/gloriouspanda.jpg"),
                                          size=(100, 90))        
c3tang_1 = customtkinter.CTkImage(Image.open("Switches/c3tangerine.jpg"),
                                          size=(100, 90))     
c3kiwi_1 = customtkinter.CTkImage(Image.open("Switches/c3kiwi.jpg"),
                                          size=(100, 90))
boxnavy_1= customtkinter.CTkImage(Image.open("Switches/boxnavy.jpg"),
                                          size=(100, 90))
boxjade_1 = customtkinter.CTkImage(Image.open("Switches/boxjade.jpg"),
                                          size=(100, 90))       
lavenderpurp_1 = customtkinter.CTkImage(Image.open("Switches/lavenderpurple.jpg"),
                                          size=(100, 90))       
radiantred_1 = customtkinter.CTkImage(Image.open("Switches/RadiantRed.jpg"),
                                          size=(100, 90))       
rosered_1 = customtkinter.CTkImage(Image.open("Switches/rosered.jpg"),
                                          size=(100, 90))        
zealiosv2_1 = customtkinter.CTkImage(Image.open("Switches/zealiosv2.jpg"),
                                          size=(100, 90))        
kttwinered_1 = customtkinter.CTkImage(Image.open("Switches/kttwinered.jpg"),
                                          size=(100, 90))
kttstrawberry_1 = customtkinter.CTkImage(Image.open("Switches/kttstrawberry.jpg"),
                                          size=(100, 90))
mxbrown_1 = customtkinter.CTkImage(Image.open("Switches/cherrymxbrown.jpg"),
                                          size=(100, 90))    
mxclear_1 = customtkinter.CTkImage(Image.open("Switches/cherrymxclear.jpg"),
                                          size=(100, 90))

#icons and backgrounds
start_bg = customtkinter.CTkImage(Image.open("icons/start_bg.jpg"),
                                          size=(1400, 900))
github_logo = customtkinter.CTkImage(Image.open("icons/github.png"),
                                          size=(60, 60))
new_tab = customtkinter.CTkImage(Image.open("icons/newtab.png"),
                                          size=(20, 20))
widget0 = customtkinter.CTkImage(Image.open("icons/zoo65.png"),
                                          size=(210, 170))

def load_keyboard_kit_Review(key):  
            webbrowser.open_new_tab(keyboard_kits_reviews[key])
def load_keycap_set_Review(key):
            webbrowser.open_new_tab(keycap_sets_reviews[key])
def load_switch_set_Review(key):    
            webbrowser.open_new_tab(switch_sets_reviews[key])
def load_other_link_Review(key):
            webbrowser.open_new_tab(other_links[key])

        
#MAIN CLASS 
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        


        # THE WINDOW

        self.title("Custom Keyboard Configurator")
        self.geometry(f"{1300}x{900}")
        self.iconbitmap("icons/icon.ico")
        self.resizable(False, False)

        # SIDEBAR FRAME WITH THE WIDGETS 
        
        self.sidebar_frame = customtkinter.CTkFrame(self,
                                                    width=120,
                                                    corner_radius=5)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                 text="Keeb Configurator",
                                                 compound= 'left', 
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))


        
        '''    widget1 = customtkinter.CTkImage(Image.open("icons/order.png"),
                                        dark_image=Image.open("icons/order.png"),
                                          size=(200, 170))'''

        # START PAGE WITH THE WIDGETS

        self.start_frame = customtkinter.CTkFrame(self,
                                                    height= 900,
                                                    width= 400,
                                                    corner_radius=0)
        self.start_frame.grid(row=0, column=1)


        self.start_page_bg = customtkinter.CTkLabel(self.start_frame,
                                                 image= start_bg,
                                                 text="")
        self.start_page_bg.grid(row=0, column= 1)

        self.start_page_logos = customtkinter.CTkButton(self.start_frame,
                                                image= github_logo,
                                                command =  lambda: other_links("github_account"),
                                                fg_color=("#121214"),
                                                bg_color=("#121214"),
                                                hover_color=("#121214"),
                                                 text="")
        self.start_page_logos.grid(row=0, column= 1)
        self.start_page_logos.place(x = 0, y = 820)


        self.start_button = customtkinter.CTkButton(self.start_frame,
                                            fg_color=("#f19dbb"),
                                            bg_color=("Black"),
                                            hover_color=("#b0e0e6"),
                                            text= 'Start',
                                            command=self.show_the_frame,
                                            font=customtkinter.CTkFont(size=20, weight="bold"),
                                            height= 65,
                                            width=130)
        self.start_button.grid(row=2, column=1, columnspan= 4, rowspan= 4)
        self.start_button.place(x = 600, y = 700)


        self.start_textbox = customtkinter.CTkTextbox(self.start_frame, 
                                                      width=750,
                                                      height= 230,
                                                      font=customtkinter.CTkFont(family= "Courier" ,size=20,weight="bold"),
                                                      fg_color='transparent')
        self.start_textbox.grid(row=0, column=1, pady=100)
        self.start_textbox.place(x = 300, y = 200)
        self.start_textbox.insert("0.0", "ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤWelcome to Keeb Configurator\n\n" +
                                   "ㅤㅤㅤㅤㅤㅤㅤㅤChoose a Keyboard kit in your budget\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤChoose the switches you like\nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤChoose a keycap set \nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤSee the prices \nㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤListen to a sound test \n\nㅤㅤㅤㅤㅤ watch recommended reviews and learn about mods. ")




        # SIDEBAR BUTTONS
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("#f19dbb"),
                                                hover_color=("#b0e0e6"),
                                                border_color= ("#f19dbb"),
                                                command =  lambda: load_other_link_Review("kits_guide"),                        
                                                image=new_tab,
                                                border_width=2,
                                                corner_radius=20,
                                                text= 'ㅤㅤKitsㅤGuideㅤㅤ',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                width=170)                   
                                   
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("#f19dbb"),
                                                hover_color=("#b0e0e6"),
                                                border_color= ("#f19dbb"),
                                                command =  lambda: load_other_link_Review("switches_guide"),
                                                image=new_tab,
                                                border_width=2,
                                                corner_radius=20,
                                                text= 'ㅤSwitches Guideㅤ',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                width=170)
        
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("#f19dbb"),
                                                hover_color=("#b0e0e6"),
                                                border_color= ("#f19dbb"),
                                                command =  lambda: load_other_link_Review("mods_guide"),
                                                image=new_tab,
                                                border_width=2,
                                                corner_radius=20,
                                                text= 'ㅤㅤMods Guideㅤㅤ',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                width=170)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,
                                                fg_color=("gray17"),
                                                hover_color=("gray17"),
                                                border_width=2,
                                                corner_radius=20,
                                                command =  lambda: load_other_link_Review("widget_link"),
                                                image=widget0, 
                                                text="", 
                                                height=220,
                                                width=180)
        
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                    text="UI Scaling:",

                                                    anchor="w")
        
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,

                                                               values=["100%", "105%", "115%"],
                                                               command=self.change_scaling_event)


        # THE MAIN LABEL WITH THE MAIN FUNCTIONS ETC.
        self.main_top = customtkinter.CTkLabel(self,
                                               text="Your Config:",
                                               anchor=customtkinter.N,
                                               font=customtkinter.CTkFont(size=20, weight="bold"), 
                                               height= 340, 
                                               width= 100,)


        self.main_switch = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                text= 'Choose a Switch',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=180,
                                                width=400)
        



        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",
                                                hover_color=("#242424"),
                                                text= 'Choose a Keyboard Kit',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=180,
                                                width=400)


        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",
                                                hover_color=("#242424"),
                                                text= 'Choose a Keycap Set',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=180,
                                                width=400)
        
 
        # ALL THE SCROLLABLE FRAMES (SWITCHES), (KEYCAPS) and (KEYBOARD KITS)
        self.keyboardkit_frame = customtkinter.CTkScrollableFrame(self,
                                                label_text="Keyboard Kits",
                                                label_font=customtkinter.CTkFont(weight="bold"),
                                                width= 220,
                                                height= 300)
        self.keyboardkit_frame_switches = []


        self.keycaps_frame = customtkinter.CTkScrollableFrame(self,
                                                        label_text="Keycaps",
                                                        label_font=customtkinter.CTkFont(weight="bold"), 
                                                        height= 300)
        self.keycaps_frame_switches = []

        self.switches_frame = customtkinter.CTkScrollableFrame(self,
                                                               label_text="Switches (Prices are for 70 Switches)",
                                                               label_font=customtkinter.CTkFont(weight="bold"),
                                                               orientation="horizontal",
                                                               height=55)
        self.switches_frame_switches = []




        # ALL THE KEYBOARD KITS BUTTONS 
        self.tofu60 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                              command=self.tofu_60,
                                              image=tofu60,
                                              corner_radius=20,
                                              border_width=2,
                                              border_color= "#8a2be2",
                                              text='Tofu60')
        self.keyboardkit_frame_switches.append(self.tofu60)



        self.tofu65 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                              command=self.tofu_65,
                                              corner_radius=20,
                                              border_width=2,
                                              border_color= "#8a2be2",
                                              image=tofu65,
                                              text='Tofu65')
        self.keyboardkit_frame_switches.append(self.tofu65)
 


        self.tester68 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                command=self.tester_68,
                                                corner_radius=20,
                                                border_width=2,
                                                border_color= "#8a2be2",
                                                image=tester68,
                                                text='Tester68')
        self.keyboardkit_frame_switches.append(self.tester68)


        self.tester84 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                command=self.tester_84,
                                                corner_radius=20,
                                                border_width=2,
                                                border_color= "#8a2be2",
                                                image=tester84,
                                                text='Tester84')

        self.keyboardkit_frame_switches.append(self.tester84)


        self.gmk67 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.gmk_67,
                                            corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                             image=gmk67,
                                             text='Gmk 67')

        self.keyboardkit_frame_switches.append(self.gmk67)


        self.gas67 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                            command=self.gas_67,
                                            corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",    
                                            image=gas67,
                                            text='GAS 67')

        self.keyboardkit_frame_switches.append(self.gas67)


        self.everglide75 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                   command=self.everglide_75,
                                                   corner_radius=20,
                                                    border_width=2,
                                                    border_color= "#8a2be2",
                                                   image=everglide75,
                                                   text='EG 75')

        self.keyboardkit_frame_switches.append(self.everglide75)
 


        self.mk870 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.mk_870,
                                             corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                             image=mk870,
                                             text='MK 870')

        self.keyboardkit_frame_switches.append(self.mk870)
 


        self.monsgeekm1 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                  command=self.monsgeek_m1,
                                                  corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                  image=monsgeekm1,
                                                  text='MG M1')

        self.keyboardkit_frame_switches.append(self.monsgeekm1)
 


        self.nexttime75 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                  command=self.nexttime_75,
                                                  corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                  image=nexttime75, 
                                                  text='NT 75')

        self.keyboardkit_frame_switches.append(self.nexttime75)
 


        self.nj80 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                            command=self.nj_80,
                                            corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                            image=nj80,
                                            text='NJ 80')

        self.keyboardkit_frame_switches.append(self.nj80)
 


        self.tm680 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.tm_680,
                                             corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                             image=tm680,
                                             text='TM680')
                                             
        self.keyboardkit_frame_switches.append(self.tm680)
 




        # ALL THE KEYCAP SET BUTTONS
        self.dcx9009 = customtkinter.CTkButton(master=self.keycaps_frame,
                                               command=self.dcx_9009,
                                               corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                               image=dcx_9009,
                                               text='9009')

        self.keycaps_frame_switches.append(self.dcx9009)
 


        self.dcxblackonwhite = customtkinter.CTkButton(master=self.keycaps_frame,
                                                       command=self.dcx_black_on_white,
                                                       corner_radius=20,
                                                        border_width=2,
                                                        border_color= "#8a2be2",
                                                       image=dcx_blackonwhite,
                                                       text='B.O.W')

        self.keycaps_frame_switches.append(self.dcxblackonwhite)
 


        self.dcxwhiteonblack = customtkinter.CTkButton(master=self.keycaps_frame,
                                                       command=self.dcx_white_on_black,
                                                       corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                       image=dcx_whiteonblack,
                                                       text='W.O.B')

        self.keycaps_frame_switches.append(self.dcxwhiteonblack)
 


        self.dcxcyber = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.dcx_cyber,
                                                corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                image=dcx_cyber,
                                                text='Cyber')

        self.keycaps_frame_switches.append(self.dcxcyber)
 


        self.dcxhyperfuse = customtkinter.CTkButton(master=self.keycaps_frame,
                                                    command=self.dcx_hyperfuse,
                                                    corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                    image=dcx_hyperfuse,
                                                    text='DCX HF')

        self.keycaps_frame_switches.append(self.dcxhyperfuse)
 


        self.dcxkeyman = customtkinter.CTkButton(master=self.keycaps_frame,
                                                 command=self.dcx_keyman,
                                                 corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                 image=dcx_keyman,
                                                 text='Keyman')

        self.keycaps_frame_switches.append(self.dcxkeyman)
 


        self.dcxviolac = customtkinter.CTkButton(master=self.keycaps_frame,
                                                 command=self.dcx_violac,
                                                 corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                 image=dcx_violac,
                                                 text='Violac')
        self.keycaps_frame_switches.append(self.dcxviolac)
 


        self.gmkarmstrong = customtkinter.CTkButton(master=self.keycaps_frame,
                                                    command=self.gmk_armstrong,
                                                    corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                    image=gmk_armstrong,
                                                    text='GodS')

        self.keycaps_frame_switches.append(self.gmkarmstrong)
 


        self.gmkbluesamurai = customtkinter.CTkButton(master=self.keycaps_frame,
                                                      command=self.gmk_bluesamurai,
                                                      corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                      image=gmk_bluesamurai,
                                                      text='BlueS')

        self.keycaps_frame_switches.append(self.gmkbluesamurai)
 


        self.gmkdots = customtkinter.CTkButton(master=self.keycaps_frame,
                                               command=self.gmk_dots,
                                               corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                               image=gmk_dots,
                                               text='Dots')

        self.keycaps_frame_switches.append(self.gmkdots)
 


        self.gmkkaiju = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.gmk_kaiju,
                                                corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                image=gmk_kaiju,
                                                text='Kaiju')

        self.keycaps_frame_switches.append(self.gmkkaiju)
 


        self.gmklaser = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.gmk_laser,
                                                corner_radius=20,
                                            border_width=2,
                                            border_color= "#8a2be2",
                                                image=gmk_laser,
                                                text='Laser')

        self.keycaps_frame_switches.append(self.gmklaser)
 
        






        # ALL THE SWITCHE SET BUTTONS
        self.c3kiwi = customtkinter.CTkButton(master=self.switches_frame,
                                              command=self.c3_kiwi,
                                              fg_color=("#420420"),
                                              image=c3kiwi,
                                              text='C3 Kiwi',
                                              compound='left',
                                              width=140,
                                              height=45)

        self.switches_frame_switches.append(self.c3kiwi)
 


        self.c3tang = customtkinter.CTkButton(master=self.switches_frame,
                                              command=self.c3_tangerine,
                                              fg_color=("#420420"),
                                              image=c3tang,
                                              text='C3 Tangerine',
                                              compound='left',
                                              width=140,
                                              height=45)

        self.switches_frame_switches.append(self.c3tang)
 


        self.boxjade = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.box_jade,
                                               fg_color=("#420420"),
                                               image=boxjade,
                                               text='Box Jade',
                                               compound='left',
                                               width=140,
                                               height=45)

        self.switches_frame_switches.append(self.boxjade)
 


        self.boxnavy = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.box_navy,
                                               fg_color=("#420420"),
                                               image=boxnavy,
                                               text='Box Navy',
                                               compound='left',
                                               width=140,
                                               height=45)

        self.switches_frame_switches.append(self.boxnavy)
 


        self.glopanda = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.holy_panda,
                                                fg_color=("#420420"),
                                                image=holpanda,
                                                text='Holy Panda',
                                                compound='left',
                                                width=140,
                                                height=45)

        self.switches_frame_switches.append(self.glopanda)
 


        self.holpanda = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.glorious_panda,
                                                fg_color=("#420420"),
                                                image=glopanda,
                                                text='Glor. Panda',
                                                compound='left',
                                                width=140,
                                                height=45)

        self.switches_frame_switches.append(self.holpanda)
 


        self.gateronblackinkv2 = customtkinter.CTkButton(master=self.switches_frame,
                                                         command=self.gateron_black_ink_v2,
                                                         fg_color=("#420420"),
                                                         image=gateronblack,
                                                         text='Gateron InkV2',
                                                         compound='left',
                                                         width=140,
                                                         height=45)

        self.switches_frame_switches.append(self.gateronblackinkv2)
 


        self.gateronoilking = customtkinter.CTkButton(master=self.switches_frame,
                                                      command=self.gateron_oil_king,
                                                      fg_color=("#420420"),
                                                      image=gatoilking,
                                                      text='Gateron OilKing',
                                                      compound='left',
                                                      width=140,
                                                      height=45)

        self.switches_frame_switches.append(self.gateronoilking)
 


        self.nkcreams = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.nk_creams,
                                                fg_color=("#420420"),
                                                image=nkcream,
                                                text='NkCreams',
                                                compound='left',
                                                width=140,
                                                height=45)

        self.switches_frame_switches.append(self.nkcreams)
 


        self.kangwhitev3 = customtkinter.CTkButton(master=self.switches_frame,
                                                   command=self.kang_white_v3,
                                                   fg_color=("#420420"),
                                                   image=kangwhitev3,
                                                   text='Kang White V3',
                                                   compound='left', width=140, height=45)

        self.switches_frame_switches.append(self.kangwhitev3)
 


        self.kttgrapefruit = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.ktt_grapefruit,
                                                     fg_color=("#420420"),
                                                     image=grapefruit,
                                                     text='KTT Grapefruit',
                                                     compound='left',
                                                     width=140, height=45)

        self.switches_frame_switches.append(self.kttgrapefruit)
 
        self.kttpeach = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.ktt_peach,
                                                fg_color=("#420420"),
                                                image=kttpeach,
                                                text='KTT Peach',
                                                compound='left',
                                                width=140, height=45)

        self.switches_frame_switches.append(self.kttpeach)
 


        self.kttstrawberry = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.ktt_strawberry,
                                                     fg_color=("#420420"),
                                                     image=kttstrawberry,
                                                     text='KTT Strawberry',
                                                     compound='left',
                                                     width=140,
                                                     height=45)

        self.switches_frame_switches.append(self.kttstrawberry)
 


        self.lavenderpurp = customtkinter.CTkButton(master=self.switches_frame,
                                                    command=self.akko_lavender_purple,
                                                    fg_color=("#420420"),
                                                    image=lavenderpurp,
                                                    text='Akko Purple',
                                                    compound='left',
                                                    width=140,
                                                    height=45)
                                                    
        self.switches_frame_switches.append(self.lavenderpurp)
 


        self.radiantred = customtkinter.CTkButton(master=self.switches_frame,
                                                  command=self.akko_radiant_red,
                                                  fg_color=("#420420"),
                                                  image=radiantred,
                                                  text='Akko Red',
                                                  compound='left',
                                                  width=140,
                                                  height=45)

        self.switches_frame_switches.append(self.radiantred)
 


        self.rosered = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.akko_rose_red,
                                               fg_color=("#420420"),
                                               image=rosered,
                                               text='Akko Rose',
                                               compound='left',
                                               width=140,
                                               height=45)
        
        self.switches_frame_switches.append(self.rosered)
 


        self.zealiosv2 = customtkinter.CTkButton(master=self.switches_frame,
                                                 command=self.zealios_v2,
                                                 fg_color=("#420420"),
                                                 image=zealiosv2,
                                                 text='ZealiosV2',
                                                 compound='left',
                                                 width=140,
                                                 height=45)
        
        self.switches_frame_switches.append(self.zealiosv2)
 


        self.kttwinered = customtkinter.CTkButton(master=self.switches_frame,
                                                  command=self.ktt_winered,
                                                  fg_color=("#420420"),
                                                  image=kttwinered,
                                                  text='KTT WineRed',
                                                  compound='left',
                                                  width=140,
                                                  height=45)
        
        self.switches_frame_switches.append(self.kttstrawberry)
 


        self.cherrymxbrown = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.cherry_mx_brown,
                                                     fg_color=("#420420"),
                                                     image=mxbrown,
                                                     text='Cherry Brown',
                                                     compound='left',
                                                     width=140,
                                                     height=45)
        
        self.switches_frame_switches.append(self.cherrymxbrown)
 


        self.cherrymxclear = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.cherry_mx_clear,
                                                     fg_color=("#420420"),
                                                     image=mxclear,
                                                     text='Cherry Clear',
                                                     compound='left',
                                                     width=140,
                                                     height=45)
        
        self.switches_frame_switches.append(self.cherrymxclear)
 
            





        # ALL THE FUNCTIONS FOR THE INPUT AND CLICK EVENTS ETC. 
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    



        # THE FUNCTION TO SHOW THE FRAME AFTER YOU CLICK ON START BUTTON

    def show_the_frame(self):

        
        self.start_button.grid_forget()
        self.start_textbox.grid_forget()
        self.start_page_bg.grid_forget()
        self.start_frame.grid_forget()
        self.start_page_logos.grid_forget()
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)



        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)



        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))



        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=15)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=15)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=15)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=15)



        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.main_top.grid(row=0, column=1,padx=20, pady=(10, 20))



        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))  



        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 



        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))               



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




        # all the functions to change the Main_Label's image to the clicked button's keyboard kit
    def tofu_60(self):
        tofu60_link = 'https://kbdfans.com/products/tofu60-2-0'
        tofu60_response  = requests.get(tofu60_link)

        tf60_soup = BeautifulSoup(tofu60_response.content, 'html.parser')
        tofu60_tag = tf60_soup.find('span', {'class': 'theme-money large-title'})

        tofu60_price = tofu60_tag.text.strip()

        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command= lambda: load_keyboard_kit_Review("tofu60"),
                                                image=tofu60_1,
                                                text= 'Tofu 60 2.0',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 
        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= tofu60_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)



    def tofu_65(self):

        tofu65_link = 'https://kbdfans.com/collections/tofu65/products/tofu65-2-0'
        tofu65_response  = requests.get(tofu65_link)

        tf65_soup = BeautifulSoup(tofu65_response.content, 'html.parser')
        tofu65_tag = tf65_soup.find('span', {'class': 'theme-money large-title'})

        tofu65_price = tofu65_tag.text.strip()

        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command= lambda: load_keyboard_kit_Review("tofu65"),
                                                image=tofu65_1,
                                                text= 'Tofu 65 2.0',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= tofu65_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)

    
    def tester_68(self):

        tester68_link = 'https://www.yunzii.com/products/ciy-tester-68-hot-swappable-transparent-mechanical-keyboard-kit'
        tester68_response  = requests.get(tester68_link)

        tester68_soup = BeautifulSoup(tester68_response.content, 'html.parser')
        tester68_tag = tester68_soup.find('span', {'class': 'money'})

        tester68_price =  tester68_tag.text.strip()

        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("tester68"),
                                                image=tester68_1,
                                                text= 'Tester 68',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= tester68_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)

    def tester_84(self):

        tester84_link = 'https://www.yunzii.com/products/ciy-tester-84-hot-swappable-transparent-keyboard-kit'
        tester84_response  = requests.get(tester84_link)

        tester84_soup = BeautifulSoup(tester84_response.content, 'html.parser')
        tester84_tag = tester84_soup.find('span', {'class': 'money'})

        tester84_price = tester84_tag.text.strip()

        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("tester84"),
                                                image=tester84_1,
                                                text= 'Tester 84',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= tester84_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)


    def gmk_67(self):

        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("gmk67"),
                                                image=gmk67_1,
                                                text= 'GMK 67',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$30-$50",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)

    def gas_67(self):

        gas67_link = 'https://landingpad.shop/products/ciy-gas67-keyboard-diy-kit'
        gas67_response  = requests.get(gas67_link)

        gas67_soup = BeautifulSoup(gas67_response.content, 'html.parser')
        gas67_tag = gas67_soup.find('span', {'class': 'price-item price-item--regular !text-white'})

        gas67_price = gas67_tag.text.strip()


        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("gas67"),
                                                image=gas67_1,
                                                text= 'Gas 67',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= gas67_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)

    def everglide_75(self):

        eg75_link = 'https://epomaker.com/products/everglide-lite-75-kit?variant=40026310279241'
        eg75_response  = requests.get(eg75_link)

        eg75_soup = BeautifulSoup(eg75_response.content, 'html.parser')
        eg75_tag = eg75_soup.find('span', {'class': 'money'})

        eg75_price = eg75_tag.text.strip()



        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("everglide75"),
                                                image=everglide75_1,
                                                text= 'Everglide Lite 75',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= eg75_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)


    def mk_870(self):

        mk_870_link = 'https://kprepublic.com/en-de/products/flesports-mk870-mechanical-keyboard-kit-full-rgb-backlit-led-hot-swappable-socket-nkro-programmable-usb-c-transparent-black-case'
        mk_870_response  = requests.get(mk_870_link)

        mk_870_soup = BeautifulSoup(mk_870_response.content, 'html.parser')
        mk_870_tag = mk_870_soup.find('span', {'class': 'money'})

        mk_870_price = mk_870_tag.text.strip()



        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("mk870"),
                                                image=mk870_1,
                                                text= 'MK 870',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= mk_870_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)


    def monsgeek_m1(self):

        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("monsgeekm1"),
                                                image=monsgeekm1_1,
                                                text= 'Monsgeek M1',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$99.99",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)


    def nexttime_75(self):

        nt_75_link = 'https://kprepublic.com/en-de/products/nexttime-x75-75-gasket-mechanical-keyboard-kit-pcb-hot-swappable-switch-lighting-effects-rgb-switch-led-type-c-next-time-75'
        nt_75_response  = requests.get(nt_75_link)

        nt_75_soup = BeautifulSoup(nt_75_response.content, 'html.parser')
        nt_75_tag = nt_75_soup.find('span', {'class': 'money'})

        nt_75_price = nt_75_tag.text.strip()


        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("nexttime75"),
                                                image=nexttime75_1,
                                                text= 'Next Time 75',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= nt_75_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)


    def nj_80(self):

        nj_80_link = 'https://www.keebmonkey.com/products/nj80'
        nj_80_response  = requests.get(nj_80_link)

        nj_80_soup = BeautifulSoup(nj_80_response.content, 'html.parser')
        nj_80_tag = nj_80_soup.find('span', {'class': 'tlab-currency-format'})

        nj_80_price = nj_80_tag.text.strip()




        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("nj80"),
                                                image=nj80_1,
                                                text= 'NJ 80',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= nj_80_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)


    def tm_680(self):


        self.main_kit = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keyboard_kit_Review("tm680"),
                                                image=tm680_1,
                                                text= 'TM 680',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20)) 

        self.main_switch_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$45 - $65",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_switch_price.place(x= 320, y= 330)










        # all the functions to change the Main_Label's image to the clicked button's keycap set
    def gmk_dots(self):

        dots_link = 'https://oblotzky.industries/products/gmk-dots-2'
        dots_response  = requests.get(dots_link)

        dots_soup = BeautifulSoup(dots_response.content, 'html.parser')
        dots_tag = dots_soup.find('span', {'class': 'product-single__price'})

        dots_price = dots_tag.text.strip()




        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("gmk_dots"),
                                                image=gmk_dots_1,
                                                text= 'GMK Dots 2.0',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= dots_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)

    def gmk_armstrong(self):

        dots_link = 'https://oblotzky.industries/products/gmk-dots-2'
        dots_response  = requests.get(dots_link)

        dots_soup = BeautifulSoup(dots_response.content, 'html.parser')
        dots_tag = dots_soup.find('span', {'class': 'product-single__price'})

        dots_price = dots_tag.text.strip()

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("gmk_armstrong"),                                                
                                                image=gmk_armstrong_1,
                                                text= 'GMK GodSpeed',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= dots_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)



    def gmk_bluesamurai(self):

        dots_link = 'https://oblotzky.industries/products/gmk-dots-2'
        dots_response  = requests.get(dots_link)

        dots_soup = BeautifulSoup(dots_response.content, 'html.parser')
        dots_tag = dots_soup.find('span', {'class': 'product-single__price'})

        dots_price = dots_tag.text.strip()

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("gmk_bluesamurai"),                                                
                                                image=gmk_bluesamurai_1,
                                                text= 'GMK Blue Samurai',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20)) 

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= dots_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)



    def gmk_kaiju(self):

        kaiju_link = 'https://oblotzky.industries/products/gmk-dots-2'
        kaiju_response  = requests.get(kaiju_link)

        kaiju_soup = BeautifulSoup(kaiju_response.content, 'html.parser')
        kaiju_tag = kaiju_soup.find('span', {'id': 'ProductPrice'})

        kaiju_price = kaiju_tag.text.strip()

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("gmk_kaiju"),                                                
                                                image=gmk_kaiju_1,
                                                text= 'GMK Kaiju',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))  

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= kaiju_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)


    def gmk_laser(self):

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("gmk_laser"),                                               
                                                image=gmk_laser_1,
                                                text= 'GMK Laser',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))   

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$150",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)



    def dcx_9009(self):

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("dcx_9009"),                                                
                                                image=dcx_9009_1,
                                                text= 'DCX 9009',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text="$99",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)



    def dcx_black_on_white(self):

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("dcx_bow"),                                                
                                                image=dcx_blackonwhite_1,
                                                text= 'DCX Black On White',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$79",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)



    def dcx_white_on_black(self):
        

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("dcx_wob"),                                                
                                                image=dcx_whiteonblack_1,
                                                text= 'DCX White On Black',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    


        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$79",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)

    
    def dcx_cyber(self):

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("dcx_cyber"),                                                
                                                image=dcx_cyber_1,
                                                text= 'DCX Cyber',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$99",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)


                                 
    def dcx_hyperfuse(self):

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("dcx_hyperfuse"),
                                                image=dcx_hyperfuse_1,
                                                text= 'DCX Hyperfuse',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$99",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)



    
    def dcx_keyman(self):

        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("dcx_keyman"), 
                                                image=dcx_keyman_1,
                                                text= 'DCX Keyman',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    


        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$99",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)


    def dcx_violac(self):
        
        self.main_keycapset = customtkinter.CTkButton(self,
                                                fg_color=("#242424"),
                                                compound="top",                            
                                                hover_color=("#242424"),
                                                command =  lambda: load_keycap_set_Review("dcx_violac"),                                                
                                                image=dcx_violac_1,
                                                text= 'DCX Violac',
                                                font=customtkinter.CTkFont(weight="bold"),
                                                height=130,
                                                width=350)
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))    

        self.main_keycapset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$99",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=100)
        self.main_keycapset_price.place(x= 320, y= 525)






        # all the functions to change the Main_Label's image to the clicked button's switch set 
    def c3_kiwi(self):

        c3kiwi_link = 'https://thekey.company/products/c3-equalz-x-tkc-kiwi-switches?variant=39513713606745'
        c3kiwi_response  = requests.get(c3kiwi_link)

        c3kiwi_soup = BeautifulSoup(c3kiwi_response.content, 'html.parser')
        c3kiwi_tag = c3kiwi_soup.find('span', {'class': 'product-single__price'})

        c3kiwi_price = c3kiwi_tag.text.strip()

        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("c3kiwi"),                                               
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= c3kiwi_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)

    def c3_tangerine(self):
        
        c3tang_link = 'https://thekey.company/products/tangerine-switches?variant=40056847827033'
        c3tang_response  = requests.get(c3tang_link)

        c3tang_soup = BeautifulSoup(c3tang_response.content, 'html.parser')
        c3tang_tag = c3tang_soup.find('span', {'class': 'product-single__price'})

        c3tang_price = c3tang_tag.text.strip()


        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("c3tang"),
                                                    image=c3tang_1,                                          
                                                    text= 'C3 Tangerine V2',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= c3tang_price,
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def box_jade(self):

        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("box_jade"),                                              
                                                    image=boxjade_1,
                                                    text= 'Box Jade',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$30",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)

    def box_navy(self):

        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("box_navy"),                                              
                                                    image=boxnavy_1,
                                                    text= 'Box Navy',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "Restocking \n Q2 2023",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def holy_panda(self):

        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("holy_panda"),                                             
                                                    image=holpanda_1,
                                                    text= 'Holy Panda',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$60",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def glorious_panda(self):

        
        glopanda_link = 'https://epomaker.com/products/epomaker-mmd-holy-panda-switch-set?variant=39913910566985'
        glopanda_response  = requests.get(glopanda_link)

        glopanda_soup = BeautifulSoup(glopanda_response.content, 'html.parser')
        glopanda_tag = glopanda_soup.find('span', {'class': 'money'})

        glopanda_price = glopanda_tag.text.strip()


        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("glo_panda"),                                              
                                                    image=glopanda_1,
                                                    text= 'Glorious Panda',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$40-50",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def gateron_black_ink_v2(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("gateron_ink_v2"),                                           
                                                    image=gateronblack_1,
                                                    text= 'Gateron Black Ink V2',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$52",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def gateron_oil_king(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("gateron_oilking"),                                               
                                                    image=gatoilking_1,
                                                    text= 'Gateron Oil King',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$47",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)

    
    def nk_creams(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("nk_cream"),                                        
                                                    image=nkcream_1,
                                                    text= 'Nk Cream',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "Restocking \n Q2 2023",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def kang_white_v3(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("ktt_kw_v3"),                                            
                                                    image=kangwhitev3_1,
                                                    text= 'KTT Kang White V3',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$15,60",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def ktt_grapefruit(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("ktt_grapefruit"),                                                
                                                    image=grapefruit_1,
                                                    text= 'KTT Grapefruit',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$20.55",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def ktt_peach(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("ktt_peach"),                                               
                                                    image=kttpeach_1,
                                                    text= 'KTT Peach',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$20.55",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def ktt_strawberry(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("ktt_strawberry"),                                              
                                                    image=kttstrawberry_1,
                                                    text= 'KTT Strawberry',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$19.50",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def akko_lavender_purple(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("akko_lavender_purple"),                                                
                                                    image=lavenderpurp_1,
                                                    text= 'Akko CS Lavender Purple',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$22.05",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def akko_radiant_red(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("akko_radiant_red"),                                        
                                                    image=radiantred_1,
                                                    text= 'Akko CS Radiant Red',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$22.05",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def akko_rose_red(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("akko_rose_red"),                                              
                                                    image=rosered_1,
                                                    text= 'Akko CS Rose Red',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$22.05",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def zealios_v2(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("zealios_v2"),                                              
                                                    image=zealiosv2_1,
                                                    text= 'Zealios V2',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$75",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def ktt_winered(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("ktt_wine_red"),                                             
                                                    image=kttwinered_1,
                                                    text= 'KTT Wine Red',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$19.50",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)

    def cherry_mx_brown(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("cherry_mx_brown"),                                                
                                                    image=mxbrown_1,
                                                    text= 'Cherry MX Brown',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$42",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)


    def cherry_mx_clear(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                command =  lambda: load_switch_set_Review("cherry_mx_clear"),                                             
                                                    image=mxclear_1,
                                                    text= 'Cherry MX Clear',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
        self.main_switchset_price = customtkinter.CTkLabel(self,
                                                fg_color=("#242424"),                      
                                                text= "$70",
                                                font=customtkinter.CTkFont(size=20, weight="bold"),
                                                height=80,
                                                width=120)
        self.main_switchset_price.place(x= 320, y= 140)



   # Creates an object and uses multiprocessing
if __name__ == "__main__":
    app = App()
    app.mainloop()