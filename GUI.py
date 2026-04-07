# DISCLAIMER OF LIABILITY:
# This software is provided "as is", without any warranty
# The author is not responsible for any damages resulting from its use
# LICENSE:
# This file is part of SUBSTR8 version 1.0 Assíle
# See the LICENSE file or https://www.gnu.org/licenses/agpl-3.0.html for more details.
# Copyright Costantino Pala © 2025
# This file was created in the framework of a PhD funded by CNR-IRPI-PG and DSCG-UNICA
# Written by me, with coding support and suggestions from ChatGPT and Gemini


import os
import sys
import customtkinter as ctk
from tkinter import filedialog
import file_manager as manager 
import about 
import assetios 
from assetios import input_tiff, input_shp, output_tiff, parameters 
from functools import partial 
from PIL import Image

# Import your custom processing modules here
# import module_1, module_2, module_3

def resource_path(relative_path): #function useful to automatically load the folder path for the icon
    if getattr(sys, 'frozen', False):  
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def GUI():
    ctk.set_appearance_mode("light")#you could opt for the dark version by tipying 'dark' instead of 'light'
    root = ctk.CTk()
    root.title("SUBSTR8 v1.0 Assíle")#write the name of your software

    sistema = parameters["os_system"]
    if sistema == 2:
        try: root.iconbitmap(resource_path("SUBSTR8_logo.ico")) #put the name of the ico file for your icon. it is useful on windows
        except: pass
    elif sistema == 1:
        try: root.iconbitmap(resource_path("SUBSTR8_logo.png"))   #put the name of the png file for your icon. it is useful on linux    
        except: pass

    dwith = root.winfo_screenwidth()
    dheig = root.winfo_screenheight()
    root.geometry(f"{dwith}x{dheig}")

    panel_color = "#ECEFF1"
    button_color = "#003366" 
    root.configure(bg=panel_color)
    font_style = ("Open Sans", 14, "bold")#font settings... 1: font name, 2: size, 3: text formatting
    font_header = ("Open Sans", 16, "bold") # font settings 1: font name, 2: size, 3: text formatting

    def update_switcher_value(title, value): # function useful to update the switcher status
        parameters[title] = value 

    switcher_config = [ #the number of switchers depends on how much rows are in this dictionary...
        {"title": "Toggle_1", "sx_label": "On", "dx_label": "Off", "true": "Off", "false": "On"}, #row 1
        {"title": "Setting_1", "sx_label": "Default", "dx_label": "Custom", "true": "Custom", "false": "Default"}, #row 2
        {"title": "Setting_2", "sx_label": "Mode A", "dx_label": "Mode B", "true": "Mode B", "false": "Mode A"} #row 3
    ]
    
    switch_colors = ('#00cc66', '#0066FF', '#FF4F00')#the colors for your switchers... it must match the number of rows in the above dictionary!

    def switch_callback(title, switch, true, false):#useful to let the switcher work. it takes the current value and updates it in the assetios dictionary
        current_value = switch.get()
        update_switcher_value(title, current_value)

    top_frame = ctk.CTkFrame(root, fg_color=panel_color)
    top_frame.pack(side="top", padx=0, pady=5, fill="x", expand=False)

    try:
        logo_path = resource_path("SUBSTRAT8_logo.png")  #changes the biggest icon of the GUI
        pil_image = Image.open(logo_path)
        desired_height = 120 #useful to handle the height of the image. the width is changed automatically to preserve proportions.
        aspect_ratio = pil_image.width / pil_image.height
        desired_width = int(desired_height * aspect_ratio)
        logo = ctk.CTkImage(light_image=pil_image, size=(desired_width, desired_height))
        logo_label = ctk.CTkLabel(top_frame, image=logo, text="", fg_color="transparent")
        logo_label.pack(side="left", padx=20, pady=5)#useful if you wish to change the position of the icon
    except Exception:
        ctk.CTkLabel(top_frame, text="SUBSTR8", font=font_header).pack(side="left", padx=20)#if the logo fails to load this text will be prompter instead

    switcher_frame = ctk.CTkFrame(top_frame, fg_color="transparent")
    switcher_frame.pack(side="right", padx=20, pady=5)#handles the position of the switcher block

    for i, config in enumerate(switcher_config):#further switcher configuration.
        single_switch_box = ctk.CTkFrame(switcher_frame, fg_color="transparent")
        single_switch_box.pack(side="left", padx=10) 
        ctk.CTkLabel(single_switch_box, text=config["title"], font=("Open Sans", 12, "bold"), text_color="#555555").pack(side="top", pady=(0,2))
        ctrl_row = ctk.CTkFrame(single_switch_box, fg_color="transparent")
        ctrl_row.pack(side="top")
        ctk.CTkLabel(ctrl_row, text=config["sx_label"], font=("Open Sans", 10)).pack(side="left", padx=5)
        switcher = ctk.CTkSwitch(ctrl_row, text="", onvalue=config["true"], offvalue=config["false"], switch_width=24, switch_height=14, border_width=3, fg_color='grey', progress_color='grey', button_color='#003366', button_hover_color=switch_colors[i], width=30, height=20)
        switcher.pack(side="left", padx=0)
        switcher.configure(command=partial(switch_callback, title=config["title"], switch=switcher, true=config["true"], false=config["false"]))
        ctk.CTkLabel(ctrl_row, text=config["dx_label"], font=("Open Sans", 10)).pack(side="left", padx=5)

    top_frame.grid_columnconfigure(0, weight=1, minsize=200)  
    top_frame.grid_columnconfigure(1, weight=0)  

    def select_outdir():#useful to select the processing directory
        outpath = filedialog.askdirectory(title="Select Output Directory")
        parameters['out_fold'] = outpath

    monitored_buttons = {}#useful if some of the intermediate outputs could also be uploaded without running the dedicated module.. the system checks if the file is loaded or calculated and changes to color button
    TARGET_KEYS = ["Output_Raster_1", "Output_Raster_2"] #buttons to monitor.. 

    def annoadore(window): #useful to let the buttons change the color if the file has been uploded.
        annoa()
        window.after(1000, lambda: annoadore(window))

    def annoa(): 
        READY_COLOR = "#C62828"   #default button color if you didn't selected a file (empty)
        WAIT_COLOR = "#EF5350" #default button color if you selected a file (file selected)
        
        for key in TARGET_KEYS:
            if key in monitored_buttons:
                button = monitored_buttons[key]
                path = assetios.input_tiff.get(key) or assetios.output_tiff.get(key)
                if path is not None:
                    button.configure(fg_color=READY_COLOR)
                else:
                    button.configure(fg_color=WAIT_COLOR)

    def browse(btn_instance, label, ext, f_type, dark_color, dict_key):
        if "Output" in label and "Directory" in label and ext == "function":
            select_outdir()
            if parameters.get('out_fold'): btn_instance.configure(fg_color=dark_color)
            return
        elif label == "Preliminary\nOperations" and ext == "function":
            manager.file_manager()
            return
        elif label == "Help\n&\nAbout" and ext == "function":
             about.about()
             return

        if ext != "function":
            filetypes = (("All files", "*.*"), (f"{f_type} Files", f"*{f_type}"))
            var_name = dict_key
            filename = filedialog.askopenfilename(title=f"Select {var_name}", initialdir="/", filetypes=filetypes)

            if filename: 
                btn_instance.configure(fg_color=dark_color)
                filename = os.path.normpath(filename)
                
                if dict_key in input_tiff:
                    manager.update_assetios(dict_key, filename, ext, 'input')
                elif dict_key in output_tiff:
                    manager.update_assetios(dict_key, filename, ext, 'output')
                elif dict_key in input_shp:
                    manager.update_assetios(dict_key, filename, ext, 'input')
                              
    color_themes = {#for buttons
        "setup":    ("#A0A0A0", "#404040"), #category key: (empty, file selected)
        "group1":   ("#9575CD", "#512DA8"), 
        "group2":   ("#FFA726", "#E65100"), 
        "target":   ("#EF5350", "#C62828"), 
        "default":  (button_color, "#14375e") 
    }

    #left grid

    canvas_frame = ctk.CTkFrame(root, fg_color=panel_color, border_width=0)
    canvas_frame.pack(fill="both", expand=True, padx=0, pady=0)
    canvas = ctk.CTkCanvas(canvas_frame, bg=panel_color, bd=0, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    yscrollbar = ctk.CTkScrollbar(canvas_frame, command=canvas.yview)
    yscrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=yscrollbar.set)
    content_frame = ctk.CTkFrame(canvas, fg_color="transparent")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    def update_scrollregion(event=None):
        canvas.configure(scrollregion=canvas.bbox("all"))
    content_frame.bind("<Configure>", update_scrollregion)

    left_frame = ctk.CTkFrame(content_frame, fg_color=panel_color)
    left_frame.pack(side="left", padx=10, pady=10, fill="both", expand=False)

    left_buttons_text = [#dictionary of buttons... 1 row=1 button
        ("Preliminary\nOperations", "function", "file_manager", "setup", None),#button 1... this is a function button... in order: ''Button text displayed'', ''button type'', ''the function to call'', ''color category key", the key for dictionary in assetios
        ("Select Output\nDirectory", "function", "select_outdir", "setup", "out_fold"), #button 2..
        ("Load\nRaster 1", "tiff", ".tif", "group1", "Input_Raster_1"),#button 3... this is a load file button... in order: "button text displayed", "file type for the assetios dictionary", 'file extension", color category type", "the key for assetios dictionary"
        ("Load\nVector 1", "shp", "shp", "group1", "Input_Vector_1"),
        ("Load\nRaster 2", "tiff", ".tif", "group2", "Input_Raster_2"),
        ("Load\nRaster 3", "tiff", ".tif", "group2", "Input_Raster_3"),
        ("Load Output\nRaster 1", "tiff", ".tif", "target", "Output_Raster_1"),
        ("Load Output\nRaster 2", "tiff", ".tif", "target", "Output_Raster_2"),
        ("Help\n&\nAbout", "function", "about", "default", None)
    ]

    def create_smart_button(index, button_data):#function creating the grid based on the number of rows in left_buttons_text...
        text, ext, f_type, theme_key, dict_key = button_data
        row = index // 3
        col = index % 3
        light_c, dark_c = color_themes.get(theme_key, color_themes["default"])#set and change the color based on the presence of the file
        start_color = light_c
        
        try:
            is_loaded = False
            if dict_key:
                if dict_key in input_tiff and input_tiff[dict_key]: is_loaded = True
                elif dict_key in output_tiff and output_tiff[dict_key]: is_loaded = True
                elif dict_key in input_shp and input_shp[dict_key]: is_loaded = True
                elif dict_key in parameters and parameters[dict_key]: is_loaded = True
            if is_loaded: start_color = dark_c
        except Exception: pass 

        button = ctk.CTkButton(left_frame, text=text, font=font_style, width=120, height=120, fg_color=start_color)
        button.configure(command=lambda: browse(button, text, ext, f_type, dark_c, dict_key))
        button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        if dict_key in TARGET_KEYS:#checks the buttons for the intermediate outputs and changes their color based on the presence or not of the desired output
            monitored_buttons[dict_key] = button

    for i, data in enumerate(left_buttons_text):
        create_smart_button(i, data)

#right button grid

    right_frame = ctk.CTkFrame(content_frame, fg_color=panel_color)
    right_frame.pack(side="right", padx=10, pady=10, fill="x", expand=False, anchor="n")

    def buttfunction(label):#let the buttons work
        if label == "Execute\nModule 1": 
            pass # module_1.run()
        elif label == "Execute\nModule 2":
            pass # module_2.run()
        elif label == "Generate\nFinal Map":
            pass # final_module.run()
            
    right_buttons_text = [#function, color. 1 row = 1 button
        ("Execute\nModule 1", "#512DA8"),            
        ("Execute\nModule 2", "#E65100"), 
    ]

    btn_height_right = 128 #button height.. it is the same for both left and right buttons grids

    for i, (textr, btn_col) in enumerate(right_buttons_text): #generates the right grid based on the number of rows in right_buttons_text
        row = i // 2  
        col = i % 2   
        button = ctk.CTkButton(right_frame, text=textr, font=font_style, width=120, height=btn_height_right, fg_color=btn_col, command=lambda label=textr: buttfunction(label))
        button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

#the button for the ending of the framework
    final_button = ctk.CTkButton(right_frame, text="Generate\nFinal Map", font=font_style, width=120, height=btn_height_right, fg_color="#C62828", command=lambda: buttfunction("Generate\nFinal Map"))
    final_button.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")

    annoadore(root)
    root.mainloop()
