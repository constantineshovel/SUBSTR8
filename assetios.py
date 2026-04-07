# DISCLAIMER OF LIABILITY:
# This software is provided "as is", without any warranty
# The author is not responsible for any damages resulting from its use
# LICENSE:
# This file is part of SUBSTR8 version 1.0 Assíle
# See the LICENSE file or https://www.gnu.org/licenses/agpl-3.0.html for more details.
# Copyright Costantino Pala © 2025
# This file was created in the framework of a PhD funded by CNR-IRPI-PG and DSCG-UNICA
# Written by me, with coding support and suggestions from ChatGPT and Gemini

#Assetios holds dictionaries and general settings allowing them to be available to every module. Assetios = settings, configuration, in Sardinian obviously :)
#File_manager.py has a function useful to update the following dictionaries.

import os

import os

parameters = {
    "os_system": None, 
    "cores": os.cpu_count(), 
    "resolution": None, 
    "epsg": None, 
    "out_fold": None, 
    "Setting_1": "Default", 
    "Setting_2": "Mode_A", 
    "Toggle_1": "Off" 
}

input_tiff = { 
    "Input_Raster_1": None,
    "Input_Raster_2": None,
    "Input_Raster_3": None,
    "Optional_Raster": None
}

input_shp = {
    "Input_Vector_1": None,
    "Input_Vector_2": None
}

output_tiff = {
    "Output_Raster_1": None,
    "Output_Raster_2": None,
    "Output_Raster_3": None,
    "Final_Map": None
}
