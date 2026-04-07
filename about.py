# DISCLAIMER OF LIABILITY:
# This software is provided "as is", without any warranty
# The author is not responsible for any damages resulting from its use
# LICENSE:
# This file is part of SUBSTR8 version 1.0 Assíle
# See the LICENSE file or https://www.gnu.org/licenses/agpl-3.0.html for more details.
# Copyright Costantino Pala © 2025
# This file was created in the framework of a PhD funded by CNR-IRPI-PG and DSCG-UNICA
# Written by me, with coding support and suggestions from ChatGPT and Gemini


import customtkinter as ctk
import os
import sys
from PIL import Image

import customtkinter as ctk
import os
import sys
from PIL import Image

# -------------------------------------------------------------------------
# RESOURCE PATH
# -------------------------------------------------------------------------
def resource_path(relative_path):
    """Obtain the proper path for icons/images, even if executed in an .exe"""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# -------------------------------------------------------------------------
# TEXT CONSTANTS
# -------------------------------------------------------------------------

# 1. Info (Top-Left)
INFO_TEXT = (
    "Software name\n\n"
    "DEVELOPER:\n"
    "[Your Name/Team]\n"
    "[Your Role/Title]\n\n"
    "INSTITUTIONS:\n"
    "[Institution or Company Name]\n"
    "[Department or Division]\n\n"
    "CONTACT:\n"
    "[contact@email.com] \n"
    "powered by SUBSTR8 v.1.0 'Assíle'"
)

# 2. Quick Help (Top-Right)
QUICK_HELP_TEXT = """
Welcome to the Generic Spatial Analysis Platform.

This tool is designed to quickly process spatial data using custom modular pipelines. Buttons in the main interface will darken automatically when the required files are successfully loaded or calculated.

1. PRELIMINARY OPERATIONS:
   • Use "Preliminary Operations" to define your working EPSG and spatial resolution.
   • Ensure grid consistency: Use Resample and Crop tools to align all input files to the smallest extent/resolution.
   • Select the "Processed Files Directory" before starting.

2. INPUT DATA (Left Panel):
   • Load your required datasets (Rasters and Vectors).
   • Configure your scenario using the toggle switches at the top of the interface.

3. PROCESSING (Right Panel):
   • Click the function buttons to execute specific analytical modules.
   • Wait for processes to complete before moving to dependent modules.

4. SUPPORT:
   • Refer to the Bibliography panel for the scientific references and methodologies used in these modules.

"""

# 3. Bibliography (Bottom-Left)
BIBLIOGRAPHY_TEXT = """
[1] Author, A., & Author, B. (Year). Title of the paper. Journal of Spatial Science, 10(2), 100-110.
[2] Author, C. (Year). Another reference for the methodology. Open Source Geospatial Journal, 5(1), 20-35.

Powered by SUBSTR8 version 1.0 Assíle
"""

# 4. License (Bottom-Right)
LICENSE_TEXT = """GNU AFFERO GENERAL PUBLIC LICENSE
                                      Version 3, 19 November 2007

     Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
     Everyone is permitted to copy and distribute verbatim copies
     of this license document, but changing it is not allowed.

[... Insert full AGPL v3 or your preferred Open Source License text here ...]

    DISCLAIMER OF LIABILITY:

    THIS SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
    INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT.
    IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY CLAIM,
    DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE,
    ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

    BY USING THIS SOFTWARE, THE USER AGREES THAT THE AUTHOR SHALL HAVE NO LIABILITY FOR ANY CONSEQUENCES ARISING FROM ITS USE."""

# -------------------------------------------------------------------------
# MAIN FUNCTION
# -------------------------------------------------------------------------
def about():
    # Window Creation
    about_window = ctk.CTkToplevel()
    about_window.title("Help & About - Generic Platform v1.0")
    
    # Window settings
    w, h = 1000, 800 
    screen_w = about_window.winfo_screenwidth()
    screen_h = about_window.winfo_screenheight()
    x = (screen_w/2) - (w/2)
    y = (screen_h/2) - (h/2)
    about_window.geometry(f"{int(w)}x{int(h)}+{int(x)}+{int(y)}")
    
    try:
        about_window.iconbitmap(resource_path("icon.ico"))
    except:
        pass

    # Colors
    panel_bg = "#ECEFF1"
    about_window.configure(fg_color=panel_bg)

    # Grid Configuration: 2 Rows x 2 Columns
    about_window.grid_columnconfigure(0, weight=1, uniform="group1") 
    about_window.grid_columnconfigure(1, weight=1, uniform="group1")
    about_window.grid_rowconfigure(0, weight=1)    
    about_window.grid_rowconfigure(1, weight=1)    

    # Fonts
    font_title = ("Open Sans", 16, "bold")
    font_body = ("Open Sans", 12)
    font_mono = ("Consolas", 10)

    # =========================================================================
    # 1. TOP-LEFT: LOGO & INFO
    # =========================================================================
    frame_info = ctk.CTkFrame(about_window, fg_color="transparent")
    frame_info.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Logo
    try:
        img_path = resource_path("logo.png")
        pil_img = Image.open(img_path)
        h_logo = 100
        w_logo = int(h_logo * (pil_img.width / pil_img.height))
        logo_img = ctk.CTkImage(light_image=pil_img, size=(w_logo, h_logo))
        lbl_logo = ctk.CTkLabel(frame_info, image=logo_img, text="")
        lbl_logo.pack(pady=(10, 5))
    except Exception:
        ctk.CTkLabel(frame_info, text="APP LOGO", font=font_title).pack(pady=20)

    # Title
    ctk.CTkLabel(frame_info, text="Generic Platform v1.0", font=("Open Sans", 24, "bold"), text_color="black").pack()
    ctk.CTkLabel(frame_info, text="Powered by [Your Framework]", font=("Open Sans", 12, "italic"), text_color="#00695C").pack(pady=(0, 10))

    # Info Text
    ctk.CTkLabel(frame_info, text=INFO_TEXT, font=font_body, text_color="black", justify="center").pack(padx=10, pady=5)

    # =========================================================================
    # 2. TOP-RIGHT: QUICK HELP
    # =========================================================================
    frame_help = ctk.CTkFrame(about_window, fg_color="white", corner_radius=10, border_width=1, border_color="#CFD8DC")
    frame_help.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    ctk.CTkLabel(frame_help, text="QUICK HELP & WARNINGS", font=font_title, text_color="#003366").pack(pady=(10, 5))
    
    txt_help = ctk.CTkTextbox(frame_help, font=font_body, fg_color="transparent", text_color="#333333", wrap="word")
    txt_help.insert("0.0", QUICK_HELP_TEXT)
    txt_help.configure(state="disabled")
    txt_help.pack(fill="both", expand=True, padx=15, pady=10)

    # =========================================================================
    # 3. BOTTOM-LEFT: BIBLIOGRAPHY
    # =========================================================================
    frame_biblio = ctk.CTkFrame(about_window, fg_color="white", corner_radius=10, border_width=1, border_color="#CFD8DC")
    frame_biblio.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    ctk.CTkLabel(frame_biblio, text="BIBLIOGRAPHY", font=font_title, text_color="#E65100").pack(pady=(10, 5))

    txt_biblio = ctk.CTkTextbox(frame_biblio, font=("Segoe UI", 11), fg_color="transparent", text_color="#333333", wrap="word")
    txt_biblio.insert("0.0", BIBLIOGRAPHY_TEXT)
    txt_biblio.configure(state="disabled")
    txt_biblio.pack(fill="both", expand=True, padx=15, pady=10)

    # =========================================================================
    # 4. BOTTOM-RIGHT: LICENSE
    # =========================================================================
    frame_license = ctk.CTkFrame(about_window, fg_color="white", corner_radius=10, border_width=1, border_color="#CFD8DC")
    frame_license.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    ctk.CTkLabel(frame_license, text="LICENSE AGREEMENT", font=font_title, text_color="#455A64").pack(pady=(10, 5))

    txt_license = ctk.CTkTextbox(frame_license, font=font_mono, fg_color="transparent", text_color="#333333", wrap="word")
    txt_license.insert("0.0", LICENSE_TEXT)
    txt_license.configure(state="disabled")
    txt_license.pack(fill="both", expand=True, padx=15, pady=10)

    # Bring to front
    about_window.lift()
    about_window.focus_force()

if __name__ == "__main__":
    app = ctk.CTk()
    app.withdraw()
    about()
    app.mainloop()
