# SUBSTR8

Pala, C. (2026). SUBSTR8 - An open platform for building GIS applications (1.0 Assíle). Zenodo. https://doi.org/10.5281/zenodo.19462380

SUBSTR8 is a modular platform designed to build standardized software for spatial analysis.

It is based on a system of six core modules that provide the fundamental functions required for geospatial processing. Rather than being a standalone application, SUBSTR8 acts as a flexible foundation: users can assemble, extend, and integrate the modules to create their own tools, workflows, or executable software.

## 🍸 Philosophy

SUBSTR8 separates **core functionality** from **final implementation**.

- The modules provide the building blocks  
- The user defines how to use them  

This allows complete freedom in:
- building custom applications  
- integrating external software  
- connecting sensors or data streams  
- adapting workflows to specific use cases  

## 🧨 Features

- Modular architecture (6 independent core modules)  
- Designed for spatial analysis and geospatial workflows  
- Compatible with external tools and software  
- Scalable and adaptable to different environments  
- Supports custom pipelines and user-defined applications

## 🎱 Modules

- launcher.py
- GUI.py
- file_manager.py
- dictionaries.py
- plotter.py
- about.py

## 🔥 Use cases

- Environmental and geospatial analysis  
- Integration of satellite and remote sensing data  
- Custom GIS tools and workflows  
- Research-oriented software development  

## 🪩 Status

🚧 Active development

## ✨ Dependencies & Licenses

SUBSTR8 depends on the following open source libraries:

- NumPy (BSD License)
- Dask (BSD License)
- Dask-image (BSD License)
- Rasterio (BSD License)
- GeoPandas (BSD License)
- psutil (BSD License)
- SciPy (BSD License)
- Matplotlib (PSF License)
- Pillow (PIL Software License)
- Requests (Apache 2.0)
- Tkinter (Python License)
- customtkinter (MIT License)

All copyright and license notices for these libraries are retained.
