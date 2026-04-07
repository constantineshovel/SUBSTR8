# DISCLAIMER OF LIABILITY:
# This software is provided "as is", without any warranty
# The author is not responsible for any damages resulting from its use
# LICENSE:
# This file is part of SUBSTR8 version 1.0 Assíle
# See the LICENSE file or https://www.gnu.org/licenses/agpl-3.0.html for more details.
# Copyright Costantino Pala © 2025
# This file was created in the framework of a PhD funded by CNR-IRPI-PG and DSCG-UNICA
# Written by me, with coding support and suggestions from ChatGPT and Gemini


import platform
import GUI 
from assetios import parameters

def set_platform():
    sys = platform.system()
    match sys:
        case 'Linux':
            syscode = 1
        case 'Windows':
            syscode = 2
        case 'Darwin':
            syscode = 3
    parameters['os_system'] = syscode
    
def start_app():
    set_platform()
    GUI.GUI()

start_app()
