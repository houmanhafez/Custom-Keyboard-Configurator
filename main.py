from PIL import Image, ImageTk
import PIL
import tkinter.messagebox
import customtkinter
import webbrowser

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme('blue')  # Themes: "blue" (standard), "green", "dark-blue"
tofu60 = customtkinter.CTkImage(light_image=Image.open("Keeb/Tofu60.jpg"),
                                          dark_image=Image.open("Keeb/Tofu60.jpg"),
                                          size=(100, 30))
        
tofu65 = customtkinter.CTkImage(light_image=Image.open("Keeb/Tofu65.jpg"),
                                        dark_image=Image.open("Keeb/Tofu65.jpg"),
                                        size=(100, 30))
    
tester68 = customtkinter.CTkImage(light_image=Image.open("Keeb/tester68.jpg"),
                                          dark_image=Image.open("Keeb/tester68.jpg"),
                                          size=(90, 30))
tester84 = customtkinter.CTkImage(light_image=Image.open("Keeb/Tester84.jpg"),
                                          dark_image=Image.open("Keeb/Tester84.jpg"),
                                          size=(90, 30))
gmk67 = customtkinter.CTkImage(light_image=Image.open("Keeb/gmk67.jpg"),
                                          dark_image=Image.open("Keeb/gmk67.jpg"),
                                          size=(99, 30))
gas67 = customtkinter.CTkImage(light_image=Image.open("Keeb/gas67.jpg"),
                                          dark_image=Image.open("Keeb/gas67.jpg"),
                                          size=(100, 30))
everglide75 = customtkinter.CTkImage(light_image=Image.open("Keeb/Everglide Lite 75.jpg"),
                                          dark_image=Image.open("Keeb/Everglide Lite 75.jpg"),
                                          size=(77, 30))
mk870 = customtkinter.CTkImage(light_image=Image.open("Keeb/MK870.jpg"),
                                          dark_image=Image.open("Keeb/MK870.jpg"),
                                          size=(99, 30))
monsgeekm1 = customtkinter.CTkImage(light_image=Image.open("Keeb/Monsgeek M1.jpg"),
                                          dark_image=Image.open("Keeb/Monsgeek M1.jpg"),
                                          size=(68, 30))
nexttime75 = customtkinter.CTkImage(light_image=Image.open("Keeb/Nexttime 75.jpg"),
                                          dark_image=Image.open("Keeb/Nexttime 75.jpg"),
                                          size=(74, 30))
nj80 = customtkinter.CTkImage(light_image=Image.open("Keeb/NJ80.jpg"),
                                          dark_image=Image.open("Keeb/NJ80.jpg"),
                                          size=(105, 30))
tm680 = customtkinter.CTkImage(light_image=Image.open("Keeb/TM680.jpg"),
                                          dark_image=Image.open("Keeb/TM680.jpg"),
                                          size=(100, 30))





gmk_dots = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkdots.jpg"),
                                          dark_image=Image.open("keycap sets/gmkdots.jpg"),
                                          size=(100, 30))
        
gmk_armstrong = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkarmstrong.jpg"),
                                          dark_image=Image.open("keycap sets/gmkarmstrong.jpg"),
                                          size=(100, 30))

gmk_bluesamurai = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkbluesamurai.jpg"),
                                          dark_image=Image.open("keycap sets/gmkbluesamurai.jpg"),
                                          size=(100, 30))

gmk_kaiju = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkkaiju.jpg"),
                                          dark_image=Image.open("keycap sets/gmkkaiju.jpg"),
                                          size=(100, 30))
        
gmk_laser = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmklaser.jpg"),
                                          dark_image=Image.open("keycap sets/gmklaser.jpg"),
                                          size=(100, 30))
        
dcx_9009 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcx9009.jpg"),
                                          dark_image=Image.open("keycap sets/dcx9009.jpg"),
                                          size=(100, 30))
        
dcx_blackonwhite = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxblackonwhite.jpg"),
                                          dark_image=Image.open("keycap sets/dcxblackonwhite.jpg"),
                                          size=(100, 30))
        
dcx_whiteonblack = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxwhiteonblack.jpg"),
                                          dark_image=Image.open("keycap sets/dcxwhiteonblack.jpg"),
                                          size=(100, 30))
    
dcx_cyber = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxcyber.jpg"),
                                          dark_image=Image.open("keycap sets/dcxcyber.jpg"),
                                          size=(100, 30))
        
dcx_hyperfuse = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxhyperfuse.jpg"),
                                          dark_image=Image.open("keycap sets/dcxhyperfuse.jpg"),
                                          size=(100, 30))
        
dcx_keyman = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxkeyman.jpg"),
                                          dark_image=Image.open("keycap sets/dcxkeyman.jpg"),
                                          size=(100, 30))
        
dcx_violac = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxviolac.jpg"),
                                          dark_image=Image.open("keycap sets/dcxviolac.jpg"),
                                          size=(100, 30))



kttpeach = customtkinter.CTkImage(light_image=Image.open("Switches/kttpeach.jpg"),
                                          dark_image=Image.open("Switches/kttpeach.jpg"),
                                          size=(35, 35))
        

gateronblack = customtkinter.CTkImage(light_image=Image.open("Switches/Gateronblackinkv2.jpg"),
                                          dark_image=Image.open("Switches/Gateronblackinkv2.jpg"),
                                          size=(35, 35))
        
gatoilking = customtkinter.CTkImage(light_image=Image.open("Switches/gateronoilking.jpg"),
                                          dark_image=Image.open("Switches/gateronoilking.jpg"),
                                          size=(35, 35))
        
grapefruit = customtkinter.CTkImage(light_image=Image.open("Switches/kttgrapefruit.jpg"),
                                          dark_image=Image.open("Switches/kttgrapefruit.jpg"),
                                          size=(35, 35))
    
kangwhitev3 = customtkinter.CTkImage(light_image=Image.open("Switches/Kangwhitev3.jpg"),
                                          dark_image=Image.open("Switches/Kangwhitev3.jpg"),
                                          size=(35, 35))
        
nkcream = customtkinter.CTkImage(light_image=Image.open("Switches/kailhcream.jpg"),
                                          dark_image=Image.open("Switches/kailhcream.jpg"),
                                          size=(35, 35))

holpanda = customtkinter.CTkImage(light_image=Image.open("Switches/holypanda.jpg"),
                                          dark_image=Image.open("Switches/holypanda.jpg"),
                                          size=(35, 35))
        
glopanda = customtkinter.CTkImage(light_image=Image.open("Switches/gloriouspanda.jpg"),
                                          dark_image=Image.open("Switches/gloriouspanda.jpg"),
                                          size=(35, 35))
        
c3tang = customtkinter.CTkImage(light_image=Image.open("Switches/c3tangerine.jpg"),
                                          dark_image=Image.open("Switches/c3tangerine.jpg"),
                                          size=(35, 35))
        
c3kiwi = customtkinter.CTkImage(light_image=Image.open("Switches/c3kiwi.jpg"),
                                          dark_image=Image.open("Switches/c3kiwi.jpg"),
                                          size=(35, 35))
        
boxnavy= customtkinter.CTkImage(light_image=Image.open("Switches/boxnavy.jpg"),
                                          dark_image=Image.open("Switches/boxnavy.jpg"),
                                          size=(35, 35))
        
boxjade = customtkinter.CTkImage(light_image=Image.open("Switches/boxjade.jpg"),
                                          dark_image=Image.open("Switches/boxjade.jpg"),
                                          size=(35, 35))
        
lavenderpurp = customtkinter.CTkImage(light_image=Image.open("Switches/lavenderpurple.jpg"),
                                          dark_image=Image.open("Switches/lavenderpurple.jpg"),
                                          size=(35, 35))
        
radiantred = customtkinter.CTkImage(light_image=Image.open("Switches/RadiantRed.jpg"),
                                          dark_image=Image.open("Switches/RadiantRed.jpg"),
                                          size=(35, 35))
        
rosered = customtkinter.CTkImage(light_image=Image.open("Switches/rosered.jpg"),
                                          dark_image=Image.open("Switches/rosered.jpg"),
                                          size=(35, 35))
        
zealiosv2 = customtkinter.CTkImage(light_image=Image.open("Switches/zealiosv2.jpg"),
                                          dark_image=Image.open("Switches/zealiosv2.jpg"),
                                          size=(35, 35))
        
kttwinered = customtkinter.CTkImage(light_image=Image.open("Switches/kttwinered.jpg"),
                                          dark_image=Image.open("Switches/kttwinered.jpg"),
                                          size=(35, 35))
        
kttstrawberry = customtkinter.CTkImage(light_image=Image.open("Switches/kttstrawberry.jpg"),
                                          dark_image=Image.open("Switches/kttstrawberry.jpg"),
                                          size=(35, 35))
        
mxbrown = customtkinter.CTkImage(light_image=Image.open("Switches/cherrymxbrown.jpg"),
                                          dark_image=Image.open("Switches/cherrymxbrown.jpg"),
                                          size=(35, 35))
        
mxclear = customtkinter.CTkImage(light_image=Image.open("Switches/cherrymxclear.jpg"),
                                          dark_image=Image.open("Switches/cherrymxclear.jpg"),
                                          size=(35, 35))
        
















tofu60_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/Tofu60.jpg"),
                                          dark_image=Image.open("Keeb/Tofu60.jpg"),
                                          size=(400, 180))
    
tofu65_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/Tofu65.jpg"),
                                        dark_image=Image.open("Keeb/Tofu65.jpg"),
                                        size=(300, 90))
    
tester68_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/tester68.jpg"),
                                          dark_image=Image.open("Keeb/tester68.jpg"),
                                        size=(300, 90))
tester84_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/Tester84.jpg"),
                                          dark_image=Image.open("Keeb/Tester84.jpg"),
                                        size=(300, 90))
gmk67_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/gmk67.jpg"),
                                          dark_image=Image.open("Keeb/gmk67.jpg"),
                                        size=(300, 90))
gas67_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/gas67.jpg"),
                                          dark_image=Image.open("Keeb/gas67.jpg"),
                                        size=(300, 90))
everglide75_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/Everglide Lite 75.jpg"),
                                          dark_image=Image.open("Keeb/Everglide Lite 75.jpg"),
                                        size=(300, 90))
mk870_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/MK870.jpg"),
                                          dark_image=Image.open("Keeb/MK870.jpg"),
                                        size=(300, 90))
monsgeekm1_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/Monsgeek M1.jpg"),
                                          dark_image=Image.open("Keeb/Monsgeek M1.jpg"),
                                        size=(300, 90))
nexttime75_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/Nexttime 75.jpg"),
                                          dark_image=Image.open("Keeb/Nexttime 75.jpg"),
                                        size=(300, 90))
nj80_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/NJ80.jpg"),
                                          dark_image=Image.open("Keeb/NJ80.jpg"),
                                        size=(300, 90))
tm680_1 = customtkinter.CTkImage(light_image=Image.open("Keeb/TM680.jpg"),
                                          dark_image=Image.open("Keeb/TM680.jpg"),
                                        size=(300, 90))





gmk_dots_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkdots.jpg"),
                                          dark_image=Image.open("keycap sets/gmkdots.jpg"),
                                        size=(300, 90))
        
gmk_armstrong_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkarmstrong.jpg"),
                                          dark_image=Image.open("keycap sets/gmkarmstrong.jpg"),
                                          size=(100, 30))

gmk_bluesamurai_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkbluesamurai.jpg"),
                                          dark_image=Image.open("keycap sets/gmkbluesamurai.jpg"),
                                          size=(100, 30))

gmk_kaiju_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmkkaiju.jpg"),
                                          dark_image=Image.open("keycap sets/gmkkaiju.jpg"),
                                          size=(100, 30))
        
gmk_laser_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/gmklaser.jpg"),
                                          dark_image=Image.open("keycap sets/gmklaser.jpg"),
                                          size=(100, 30))
        
dcx_9009_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcx9009.jpg"),
                                          dark_image=Image.open("keycap sets/dcx9009.jpg"),
                                          size=(100, 30))
        
dcx_blackonwhite_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxblackonwhite.jpg"),
                                          dark_image=Image.open("keycap sets/dcxblackonwhite.jpg"),
                                          size=(100, 30))
        
dcx_whiteonblack_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxwhiteonblack.jpg"),
                                          dark_image=Image.open("keycap sets/dcxwhiteonblack.jpg"),
                                          size=(100, 30))
        
dcx_cyber_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxcyber.jpg"),
                                          dark_image=Image.open("keycap sets/dcxcyber.jpg"),
                                          size=(100, 30))
        
dcx_hyperfuse_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxhyperfuse.jpg"),
                                          dark_image=Image.open("keycap sets/dcxhyperfuse.jpg"),
                                          size=(100, 30))
        
dcx_keyman_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxkeyman.jpg"),
                                          dark_image=Image.open("keycap sets/dcxkeyman.jpg"),
                                          size=(100, 30))
        
dcx_violac_1 = customtkinter.CTkImage(light_image=Image.open("keycap sets/dcxviolac.jpg"),
                                          dark_image=Image.open("keycap sets/dcxviolac.jpg"),
                                          size=(100, 30))




kttpeach_1 = customtkinter.CTkImage(light_image=Image.open("Switches/kttpeach.jpg"),
                                          dark_image=Image.open("Switches/kttpeach.jpg"),
                                          size=(35, 35))
        

gateronblack_1 = customtkinter.CTkImage(light_image=Image.open("Switches/Gateronblackinkv2.jpg"),
                                          dark_image=Image.open("Switches/Gateronblackinkv2.jpg"),
                                          size=(35, 35))
        
gatoilking_1 = customtkinter.CTkImage(light_image=Image.open("Switches/gateronoilking.jpg"),
                                          dark_image=Image.open("Switches/gateronoilking.jpg"),
                                          size=(35, 35))
        
grapefruit_1 = customtkinter.CTkImage(light_image=Image.open("Switches/kttgrapefruit.jpg"),
                                          dark_image=Image.open("Switches/kttgrapefruit.jpg"),
                                          size=(35, 35))
    
kangwhitev3_1 = customtkinter.CTkImage(light_image=Image.open("Switches/Kangwhitev3.jpg"),
                                          dark_image=Image.open("Switches/Kangwhitev3.jpg"),
                                          size=(35, 35))
        
nkcream_1 = customtkinter.CTkImage(light_image=Image.open("Switches/kailhcream.jpg"),
                                          dark_image=Image.open("Switches/kailhcream.jpg"),
                                          size=(35, 35))

holpanda_1 = customtkinter.CTkImage(light_image=Image.open("Switches/holypanda.jpg"),
                                          dark_image=Image.open("Switches/holypanda.jpg"),
                                          size=(35, 35))
        
glopanda_1 = customtkinter.CTkImage(light_image=Image.open("Switches/gloriouspanda.jpg"),
                                          dark_image=Image.open("Switches/gloriouspanda.jpg"),
                                          size=(35, 35))
        
c3tang_1 = customtkinter.CTkImage(light_image=Image.open("Switches/c3tangerine.jpg"),
                                          dark_image=Image.open("Switches/c3tangerine.jpg"),
                                          size=(100, 90))
        
c3kiwi_1 = customtkinter.CTkImage(light_image=Image.open("Switches/c3kiwi.jpg"),
                                          dark_image=Image.open("Switches/c3kiwi.jpg"),
                                          size=(100, 90))
        
boxnavy_1= customtkinter.CTkImage(light_image=Image.open("Switches/boxnavy.jpg"),
                                          dark_image=Image.open("Switches/boxnavy.jpg"),
                                          size=(35, 35))
        
boxjade_1 = customtkinter.CTkImage(light_image=Image.open("Switches/boxjade.jpg"),
                                          dark_image=Image.open("Switches/boxjade.jpg"),
                                          size=(35, 35))
        
lavenderpurp_1 = customtkinter.CTkImage(light_image=Image.open("Switches/lavenderpurple.jpg"),
                                          dark_image=Image.open("Switches/lavenderpurple.jpg"),
                                          size=(35, 35))
        
radiantred_1 = customtkinter.CTkImage(light_image=Image.open("Switches/RadiantRed.jpg"),
                                          dark_image=Image.open("Switches/RadiantRed.jpg"),
                                          size=(35, 35))
        
rosered_1 = customtkinter.CTkImage(light_image=Image.open("Switches/rosered.jpg"),
                                          dark_image=Image.open("Switches/rosered.jpg"),
                                          size=(35, 35))
        
zealiosv2_1 = customtkinter.CTkImage(light_image=Image.open("Switches/zealiosv2.jpg"),
                                          dark_image=Image.open("Switches/zealiosv2.jpg"),
                                          size=(35, 35))
        
kttwinered_1 = customtkinter.CTkImage(light_image=Image.open("Switches/kttwinered.jpg"),
                                          dark_image=Image.open("Switches/kttwinered.jpg"),
                                          size=(35, 35))
        
kttstrawberry_1 = customtkinter.CTkImage(light_image=Image.open("Switches/kttstrawberry.jpg"),
                                          dark_image=Image.open("Switches/kttstrawberry.jpg"),
                                          size=(35, 35))
        
mxbrown_1 = customtkinter.CTkImage(light_image=Image.open("Switches/cherrymxbrown.jpg"),
                                          dark_image=Image.open("Switches/cherrymxbrown.jpg"),
                                          size=(35, 35))
        
mxclear_1 = customtkinter.CTkImage(light_image=Image.open("Switches/cherrymxclear.jpg"),
                                          dark_image=Image.open("Switches/cherrymxclear.jpg"),
                                          size=(35, 35))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # ALL THE PICTURES NEEDED FOR THE LABELS AND SO ON
        
        # THE WINDOW
        self.title("Custom Keyboard Configurator")
        self.geometry(f"{1200}x{810}")
        self.iconbitmap("icons/icon.ico")


        # THE 4X4 GRID LAYOUT
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # SIDEBAR FRAME WITH THE WIDGETS
        self.lines = customtkinter.CTkButton(self, command=self.click,text= '-\n-\n-')

        self.sidebar_frame = customtkinter.CTkFrame(self,
                                                    width=120,
                                                    corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                 text="Keeb Configurator", 
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


        new_tab = customtkinter.CTkImage(light_image=Image.open("icons/newtab.png"),
                                          dark_image=Image.open("icons/newtab.png"),
                                          size=(20, 20))
        
        widget0 = customtkinter.CTkImage(light_image=Image.open("icons/zoo65.png"),
                                        dark_image=Image.open("icons/zoo65.png"),
                                          size=(200, 170))
        
        widget1 = customtkinter.CTkImage(light_image=Image.open("icons/order.png"),
                                        dark_image=Image.open("icons/order.png"),
                                          size=(200, 170))
        
      #  self.tab = customtkinter.CTkButton(self,
     #                                      fg_color=("#468499"),
   #                                         command=self.show_sidebar_frame,                         
    #                                        text= 'Menu',
      #                                      font=customtkinter.CTkFont(weight="bold"),
      #                                      width=70)
#
     #   self.tab.grid(row=0, column=34, rowspan= 4)

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,
                                                        fg_color=("#468499"),
                                                        command=self.kit_guide,                         
                                                        image=new_tab,
                                                        text= 'ㅤㅤKitsㅤGuideㅤㅤ',
                                                        font=customtkinter.CTkFont(weight="bold"),
                                                        width=170)

        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=15)
                                   
                                   
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,
                                                        fg_color=("#468499"),
                                                        command=self.switches_guide,
                                                        image=new_tab,
                                                        text= 'ㅤSwitches Guideㅤ',
                                                        font=customtkinter.CTkFont(weight="bold"),
                                                        width=170)
        
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=15)


        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,
                                                        fg_color=("#468499"),
                                                        command=self.mod_guide,
                                                        image=new_tab,
                                                        text= 'ㅤㅤMods Guideㅤㅤ',
                                                        font=customtkinter.CTkFont(weight="bold"),
                                                        width=170)
        
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=15)


        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,
                                                        fg_color=("gray17"),
                                                        hover_color=("gray17"),
                                                        corner_radius= 0,
                                                        command=self.mod_guide,
                                                        image=widget0, 
                                                        text="", 
                                                        height=220,
                                                        width=180)
        
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=15)
        

        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                            text="Appearance Mode:",
                                                            anchor="w")
        
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       fg_color=("#468499"),
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))



        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                    text="UI Scaling:",
                                                    anchor="w")
        
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               fg_color=("#468499"),
                                                               values=["100%", "110%", "120%","130%"],
                                                               command=self.change_scaling_event)
        
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        







        #self.main_frame = customtkinter.CTkFrame(self,
       #                             height= 10, 
        #                            width= 10,
       #                             fg_color="Blue")
        #self.main_frame.grid(row=0, column=1, rowspan=5)


        # THE MAIN LABEL WITH THE MAIN FUNCTIONS ETC.
        self.main_top = customtkinter.CTkLabel(self,
                                               text="Your Config:",
                                               anchor=customtkinter.N,
                                               font=customtkinter.CTkFont(size=20, weight="bold"), 
                                               height= 340, 
                                               width= 100,)

        self.main_top.grid(row=0, column=1,padx=20, pady=(10, 20))

        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    text= 'Choose a Switch',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))    


        self.main_kit = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",
                                                        
                                                    hover_color=("#242424"),
                                                    image=tofu65_1,
                                                    text= 'Tofu 65',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_kit.grid(row=0, column=1, rowspan=2,padx=0, pady=(10, 20))    


        self.main_keycapset = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",
                                                    hover_color=("#242424"),
                                                    image=gmk_dots_1,
                                                    text= 'GMK Dots',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        
        self.main_keycapset.grid(row=1, column=1,padx=0, pady=(10, 20))                

        

        # ALL THE SCROLLABLE FRAMES (SWITCHES), (KEYCAPS) and (KEYBOARD KITS)
        self.keyboardkit_frame = customtkinter.CTkScrollableFrame(self,
                                                                  label_text="Keyboard Kits",
                                                                  label_font=customtkinter.CTkFont(weight="bold"),
                                                                  height= 300)

        self.keyboardkit_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.keyboardkit_frame.grid_columnconfigure(0, weight=1)
        self.keyboardkit_frame_switches = []


        self.keycaps_frame = customtkinter.CTkScrollableFrame(self,
                                                              label_text="Keycaps",
                                                              label_font=customtkinter.CTkFont(weight="bold"), 
                                                              height= 300)

        self.keycaps_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.keycaps_frame.grid_columnconfigure(0, weight=1)
        self.keycaps_frame_switches = []



        self.switches_frame = customtkinter.CTkScrollableFrame(self,
                                                               label_text="Switches",
                                                               label_font=customtkinter.CTkFont(weight="bold"),
                                                               orientation="horizontal",
                                                               height=55)


        self.switches_frame.grid(row=3, column=1, columnspan=3, sticky="nsew")
        self.switches_frame.grid_columnconfigure(0, weight=1)
        self.switches_frame_switches = []







        # ALL THE KEYBOARD KITS 
        self.tofu60 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                              command=self.button_event,
                                              image=tofu60,
                                              text='Tofu60')

        self.tofu60.grid(row=1, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.tofu60)
        self.appearance_mode_optionemenu.set("Dark")


        self.tofu65 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                              command=self.button_event,
                                              image=tofu65,
                                              text='Tofu65')

        self.tofu65.grid(row=2, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.tofu65)
        self.appearance_mode_optionemenu.set("Dark")



        self.tester68 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                command=self.button_event,
                                                image=tester68,
                                                text='Tester68')

        self.tester68.grid(row=3, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.tester68)
        self.appearance_mode_optionemenu.set("Dark")



        self.tester84 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                command=self.button_event,
                                                image=tester84,
                                                text='Tester84')

        self.tester84.grid(row=4, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.tester84)
        self.appearance_mode_optionemenu.set("Dark")



        self.gmk67 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.button_event,
                                             image=gmk67,
                                             text='Gmk 67')

        self.gmk67.grid(row=5, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.gmk67)
        self.appearance_mode_optionemenu.set("Dark")



        self.gas67 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.button_event,image=gas67,
                                             text='Gas 67')

        self.gas67.grid(row=6, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.gas67)
        self.appearance_mode_optionemenu.set("Dark")



        self.everglide75 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                   command=self.button_event,
                                                   image=everglide75,
                                                   text='Everglide75')

        self.everglide75.grid(row=7, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.everglide75)
        self.appearance_mode_optionemenu.set("Dark")



        self.mk870 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.button_event,
                                             image=mk870,
                                             text='MK 870')

        self.mk870.grid(row=8, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.mk870)
        self.appearance_mode_optionemenu.set("Dark")



        self.monsgeekm1 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                  command=self.button_event,
                                                  image=monsgeekm1,
                                                  text='MonsGeekM1')

        self.monsgeekm1.grid(row=9, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.monsgeekm1)
        self.appearance_mode_optionemenu.set("Dark")



        self.nexttime75 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                                  command=self.button_event,
                                                  image=nexttime75, 
                                                  text='Nexttime 75')

        self.nexttime75.grid(row=10, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.nexttime75)
        self.appearance_mode_optionemenu.set("Dark")



        self.nj80 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                            command=self.button_event,
                                            image=nj80,
                                            text='NJ 80')

        self.nj80.grid(row=11, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.nj80)
        self.appearance_mode_optionemenu.set("Dark")



        self.tm680 = customtkinter.CTkButton(master=self.keyboardkit_frame,
                                             command=self.button_event,
                                             image=tm680,
                                             text='TM680')
                                             
        self.tm680.grid(row=12, column=0, padx=10, pady=(0, 20))
        self.keyboardkit_frame_switches.append(self.tm680)
        self.appearance_mode_optionemenu.set("Dark")








        # ALL THE KEYCAPS
        self.dcx9009 = customtkinter.CTkButton(master=self.keycaps_frame,
                                               command=self.button_event,
                                               image=dcx_9009,
                                               text='DCX 9009')

        self.dcx9009.grid(row=1, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.dcx9009)
        self.appearance_mode_optionemenu.set("Dark")



        self.dcxblackonwhite = customtkinter.CTkButton(master=self.keycaps_frame,
                                                       command=self.button_event,
                                                       image=dcx_whiteonblack,
                                                       text='DCX White')

        self.dcxblackonwhite.grid(row=2, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.dcxblackonwhite)
        self.appearance_mode_optionemenu.set("Dark")



        self.dcxwhiteonblack = customtkinter.CTkButton(master=self.keycaps_frame,
                                                       command=self.button_event,
                                                       image=dcx_blackonwhite,
                                                       text='DCX Black')

        self.dcxwhiteonblack.grid(row=3, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.dcxwhiteonblack)
        self.appearance_mode_optionemenu.set("Dark")



        self.dcxcyber = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.button_event,
                                                image=dcx_cyber,
                                                text='DCX Cyber')

        self.dcxcyber.grid(row=4, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.dcxcyber)
        self.appearance_mode_optionemenu.set("Dark")



        self.dcxhyperfuse = customtkinter.CTkButton(master=self.keycaps_frame,
                                                    command=self.button_event,
                                                    image=dcx_hyperfuse,
                                                    text='DCX Hyperfuse')

        self.dcxhyperfuse.grid(row=5, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.dcxhyperfuse)
        self.appearance_mode_optionemenu.set("Dark")



        self.dcxkeyman = customtkinter.CTkButton(master=self.keycaps_frame,
                                                 command=self.button_event,
                                                 image=dcx_keyman,
                                                 text='DCX Keyman')

        self.dcxkeyman.grid(row=6, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.dcxkeyman)
        self.appearance_mode_optionemenu.set("Dark")



        self.dcxviolac = customtkinter.CTkButton(master=self.keycaps_frame,
                                                 command=self.button_event,
                                                 image=dcx_violac,
                                                 text='DCX Violac')
        self.dcxviolac.grid(row=7, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.dcxviolac)
        self.appearance_mode_optionemenu.set("Dark")



        self.gmkarmstrong = customtkinter.CTkButton(master=self.keycaps_frame,
                                                    command=self.button_event,
                                                    image=gmk_armstrong,
                                                    text='GMK Armstrong')

        self.gmkarmstrong.grid(row=8, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.gmkarmstrong)
        self.appearance_mode_optionemenu.set("Dark")



        self.gmkbluesamurai = customtkinter.CTkButton(master=self.keycaps_frame,
                                                      command=self.button_event,
                                                      image=gmk_bluesamurai,
                                                      text='GMK BlueSamurai')

        self.gmkbluesamurai.grid(row=9, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.gmkbluesamurai)
        self.appearance_mode_optionemenu.set("Dark")



        self.gmkdots = customtkinter.CTkButton(master=self.keycaps_frame,
                                               command=self.button_event,
                                               image=gmk_dots,
                                               text='GMK Dots')

        self.gmkdots.grid(row=10, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.gmkdots)
        self.appearance_mode_optionemenu.set("Dark")



        self.gmkkaiju = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.button_event,
                                                image=gmk_kaiju,
                                                text='GMK Kaiju')

        self.gmkkaiju.grid(row=11, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.gmkkaiju)
        self.appearance_mode_optionemenu.set("Dark")



        self.gmklaser = customtkinter.CTkButton(master=self.keycaps_frame,
                                                command=self.button_event,
                                                image=gmk_laser,
                                                text='GMK Laser')

        self.gmklaser.grid(row=12, column=0, padx=10, pady=(0, 20))
        self.keycaps_frame_switches.append(self.gmklaser)
        self.appearance_mode_optionemenu.set("Dark")

        






        # ALL THE SWITCHES
        self.c3kiwi = customtkinter.CTkButton(master=self.switches_frame,
                                              command=self.c3kiwi,
                                              fg_color=("#420420"),
                                              image=c3kiwi,
                                              text='C3 Kiwi',
                                              compound='left',
                                              width=140,
                                              height=45)

        self.c3kiwi.grid(row=1, column=0, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.c3kiwi)
        self.appearance_mode_optionemenu.set("Dark")



        self.c3tang = customtkinter.CTkButton(master=self.switches_frame,
                                              command=self.c3tangerine,
                                              fg_color=("#420420"),
                                              image=c3tang,
                                              text='C3 Tangerine',
                                              compound='left',
                                              width=140,
                                              height=45)

        self.c3tang.grid(row=1, column=1, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.c3tang)
        self.appearance_mode_optionemenu.set("Dark")



        self.boxjade = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.button_event,
                                               fg_color=("#420420"),
                                               image=boxjade,
                                               text='Box Jade',
                                               compound='left',
                                               width=140,
                                               height=45)

        self.boxjade.grid(row=1, column=2, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.boxjade)
        self.appearance_mode_optionemenu.set("Dark")



        self.boxnavy = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.button_event,
                                               fg_color=("#420420"),
                                               image=boxnavy,
                                               text='Box Navy',
                                               compound='left',
                                               width=140,
                                               height=45)

        self.boxnavy.grid(row=1, column=3, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.boxnavy)
        self.appearance_mode_optionemenu.set("Dark")



        self.glopanda = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.button_event,
                                                fg_color=("#420420"),
                                                image=glopanda,
                                                text='Holy Panda',
                                                compound='left',
                                                width=140,
                                                height=45)

        self.glopanda.grid(row=1, column=4, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.glopanda)
        self.appearance_mode_optionemenu.set("Dark")



        self.holpanda = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.button_event,
                                                fg_color=("#420420"),
                                                image=holpanda,
                                                text='Glor. Panda',
                                                compound='left',
                                                width=140,
                                                height=45)

        self.holpanda.grid(row=1, column=5, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.holpanda)
        self.appearance_mode_optionemenu.set("Dark")



        self.gateronblackinkv2 = customtkinter.CTkButton(master=self.switches_frame,
                                                         command=self.button_event,
                                                         fg_color=("#420420"),
                                                         image=gateronblack,
                                                         text='Gateron InkV2',
                                                         compound='left',
                                                         width=140,
                                                         height=45)

        self.gateronblackinkv2.grid(row=1, column=6, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.gateronblackinkv2)
        self.appearance_mode_optionemenu.set("Dark")



        self.gateronoilking = customtkinter.CTkButton(master=self.switches_frame,
                                                      command=self.button_event,
                                                      fg_color=("#420420"),
                                                      image=gatoilking,
                                                      text='Gateron OilKing',
                                                      compound='left',
                                                      width=140,
                                                      height=45)

        self.gateronoilking.grid(row=1, column=7, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.gateronoilking)
        self.appearance_mode_optionemenu.set("Dark")



        self.nkcreams = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.button_event,
                                                fg_color=("#420420"),
                                                image=nkcream,
                                                text='NkCreams',
                                                compound='left',
                                                width=140,
                                                height=45)

        self.nkcreams.grid(row=1, column=8, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.nkcreams)
        self.appearance_mode_optionemenu.set("Dark")



        self.kangwhitev3 = customtkinter.CTkButton(master=self.switches_frame,
                                                   command=self.button_event,
                                                   fg_color=("#420420"),
                                                   image=kangwhitev3,
                                                   text='Kang White V3',
                                                   compound='left', width=140, height=45)

        self.kangwhitev3.grid(row=1, column=9, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.kangwhitev3)
        self.appearance_mode_optionemenu.set("Dark")



        self.kttgrapefruit = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.button_event,
                                                     fg_color=("#420420"),
                                                     image=grapefruit,
                                                     text='KTT Grapefruit',
                                                     compound='left',
                                                     width=140, height=45)

        self.kttgrapefruit.grid(row=1, column=10, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.kttgrapefruit)
        self.appearance_mode_optionemenu.set("Dark")

        self.kttpeach = customtkinter.CTkButton(master=self.switches_frame,
                                                command=self.button_event,
                                                fg_color=("#420420"),
                                                image=kttpeach,
                                                text='KTT Peach',
                                                compound='left',
                                                width=140, height=45)

        self.kttpeach.grid(row=1, column=11, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.kttpeach)
        self.appearance_mode_optionemenu.set("Dark")



        self.kttstrawberry = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.button_event,
                                                     fg_color=("#420420"),
                                                     image=kttstrawberry,
                                                     text='KTT Strawberry',
                                                     compound='left',
                                                     width=140,
                                                     height=45)

        self.kttstrawberry.grid(row=1, column=12, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.kttstrawberry)
        self.appearance_mode_optionemenu.set("Dark")



        self.lavenderpurp = customtkinter.CTkButton(master=self.switches_frame,
                                                    command=self.button_event,
                                                    fg_color=("#420420"),
                                                    image=lavenderpurp,
                                                    text='Akko Purple',
                                                    compound='left',
                                                    width=140,
                                                    height=45)
                                                    
        self.lavenderpurp.grid(row=1, column=13, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.lavenderpurp)
        self.appearance_mode_optionemenu.set("Dark")



        self.radiantred = customtkinter.CTkButton(master=self.switches_frame,
                                                  command=self.button_event,
                                                  fg_color=("#420420"),
                                                  image=radiantred,
                                                  text='Akko Red',
                                                  compound='left',
                                                  width=140,
                                                  height=45)

        self.radiantred.grid(row=1, column=14, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.radiantred)
        self.appearance_mode_optionemenu.set("Dark")



        self.rosered = customtkinter.CTkButton(master=self.switches_frame,
                                               command=self.button_event,
                                               fg_color=("#420420"),
                                               image=rosered,
                                               text='Akko Rose',
                                               compound='left',
                                               width=140,
                                               height=45)
        
        self.rosered.grid(row=1, column=15, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.rosered)
        self.appearance_mode_optionemenu.set("Dark")



        self.zealiosv2 = customtkinter.CTkButton(master=self.switches_frame,
                                                 command=self.button_event,
                                                 fg_color=("#420420"),
                                                 image=zealiosv2,
                                                 text='ZealiosV2',
                                                 compound='left',
                                                 width=140,
                                                 height=45)
        
        self.zealiosv2.grid(row=1, column=16, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.zealiosv2)
        self.appearance_mode_optionemenu.set("Dark")



        self.kttwinered = customtkinter.CTkButton(master=self.switches_frame,
                                                  command=self.button_event,
                                                  fg_color=("#420420"),
                                                  image=kttwinered,
                                                  text='KTT WineRed',
                                                  compound='left',
                                                  width=140,
                                                  height=45)
        
        self.kttwinered.grid(row=1, column=17, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.kttstrawberry)
        self.appearance_mode_optionemenu.set("Dark")



        self.cherrymxbrown = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.button_event,
                                                     fg_color=("#420420"),
                                                     image=mxbrown,
                                                     text='Cherry Brown',
                                                     compound='left',
                                                     width=140,
                                                     height=45)
        
        self.cherrymxbrown.grid(row=1, column=18, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.cherrymxbrown)
        self.appearance_mode_optionemenu.set("Dark")



        self.cherrymxclear = customtkinter.CTkButton(master=self.switches_frame,
                                                     command=self.button_event,
                                                     fg_color=("#420420"),
                                                     image=mxclear,
                                                     text='Cherry Clear',
                                                     compound='left',
                                                     width=140,
                                                     height=45)
        
        self.cherrymxclear.grid(row=1, column=19, padx=10, pady=(0, 20))
        self.switches_frame_switches.append(self.cherrymxclear)
        self.appearance_mode_optionemenu.set("Dark")




        # ALL THE FUNCTIONS FOR THE INPUT AND CLICK EVENTS ETC. 
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def show_sidebar_frame(self):
        pass
        

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3tangerine(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3tang_1,
                                                    text= 'C3 Tangerine V2',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def button_event(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
    
    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))

    def c3kiwi(self):
        self.main_switch = customtkinter.CTkButton(self,
                                                    fg_color=("#242424"),
                                                    compound="top",                            
                                                    hover_color=("#242424"),
                                                    image=c3kiwi_1,
                                                    text= 'C3 Kiwi',
                                                    font=customtkinter.CTkFont(weight="bold"),
                                                    height=180,
                                                    width=400)
        self.main_switch.grid(row=0, column=1,padx=0, pady=(10, 20))
    def click(self):
        pass
    #def __init__(self):

        super().__init__()


        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{780}")

        self.textbox = customtkinter.CTkTextbox(self, width=0)
        self.textbox.grid(row=3, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Welcome to Keeb Configurator\n\n" + "Choose a Keyboard kit in your budget, choose the switches you like and  a keycap set and find out the price. You can also learn about mods that are generally available for the kit.\n\n")

    def sd(self, event= None):
        if self.cget("state") != "disabled": #Ignore click if button is disabled
            self.toggleState *= -1
            if self.toggleState == -1:
                self.config(image = self.clickedImage)
            else:
                self.config(image = self.unclickedImage)

    def kit_guide(self):
        url = 'https://www.youtube.com/watch?v=Sm1DVbyeDiI'
        webbrowser.open_new_tab(url)

    def switches_guide(self):
        url= 'https://www.youtube.com/watch?v=-Ln9rA_usoY'
        webbrowser.open_new_tab(url)
    
    def mod_guide(self):
        url= 'https://www.youtube.com/watch?v=xY9z0RLitbA'
        webbrowser.open_new_tab(url)
    # MULTIPROCESSING :D
if __name__ == "__main__":
    app = App()
    app.mainloop()
