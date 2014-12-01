The links below are to static renderings of the notebooks via
[nbviewer.ipython.org](http://nbviewer.ipython.org/).
Descriptions below the links are from the first cell of the notebooks
(if that cell contains Markdown or raw text).

* ##[3DBathymetry.ipynb](http://nbviewer.ipython.org/urls/bitbucket.org/canyonsubc/BuildCanyon/raw/tip/Bathymetry/3DBathymetry.ipynb)  
    
    Generate 3D bathymetry graphics from binary file prepared for MITgcm submarine canyon simulations  
    ---------------------------------------------------------------------------------------  

* ##[GenerateNonUniformBathymetry360x360.ipynb](http://nbviewer.ipython.org/urls/bitbucket.org/canyonsubc/BuildCanyon/raw/tip/Bathymetry/GenerateNonUniformBathymetry360x360.ipynb)  
    
    Non-uniform grid 360x360  
    ==============================  
    This ipy-notebook generates a bathymetry file (as well as delx and dely files) with non uniform resolution. Minimum resolution is 200 m near the canyon (along shore and across shore). This notebook is based on the functions *make_arbitrary_topo_smooth*, *tanktopo*, *canyontopo* and *widthprofile* which were originally written by S. Allen, and modified by T. Howatt and J. Spurgin (They have been translated form python to matlab and here to python again).   
    They have to be loaded from the module BathyPythonTools.py  
      
    

