### This module contains functions to calculate transport (advective, diffusive (some day), horizontal, vertical ) through planes defined in TransportThroughBoxes.ipynb

import numpy as np
 
#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportUPS1(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = 197:, nx = 40
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[197:-1,40],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,40]*area*U[time,:,197:,40]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,40]*area*U[time,:,197:,40]*Tr[time,:,197:-1,40]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportUPS1b(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = :, nx = 40.
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[:-1,40],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,40]*area*U[time,:,:,40]))
            
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,40]*area*U[time,:,:,40]*Tr[time,:,:-1,40]))
            
        return TempTransD
    
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportUPS2(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = 197:, nx = 120
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[197:-1,120],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,120]*area*U[time,:,197:,120]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,120]*area*U[time,:,197:,120]*Tr[time,:,197:-1,120]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportUPS2b(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = :, nx = 120.
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[:-1,120],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,120]*area*U[time,:,:,120]))
            
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,120]*area*U[time,:,:,120]*Tr[time,:,:-1,120]))
            
        return TempTransD
    
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportDWS1(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = 197:, nx = 240
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[197:-1,240],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,240]*area*U[time,:,197:,240]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,240]*area*U[time,:,197:,240]*Tr[time,:,197:-1,240]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportDWS1b(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = :, nx = 240.
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[:-1,240],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,240]*area*U[time,:,:,240]))
            
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,240]*area*U[time,:,:,240]*Tr[time,:,:-1,240]))
            
        return TempTransD
    
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportDWS2(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = 197:, nx = 320
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[197:-1,320],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,320]*area*U[time,:,197:,320]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197:-1,320]*area*U[time,:,197:,320]*Tr[time,:,197:-1,320]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------

def AdvTransportDWS2b(hFacC,dyF,drF,nt,U,Tr=0,transType=0):
    """
    Calculate advective transport of water or tracers through plane UPS1, defined by indices ny = :, nx = 320.
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dyF : Width of cell though cell center in y-dir or across-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               U  : Along-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dyF[:,i]*U[t,:,:,i]*Tr[t,:,:,i]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dyF[:-1,320],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,320]*area*U[time,:,:,320]))
            
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,:-1,320]*area*U[time,:,:,320]*Tr[time,:,:-1,320]))
            
        return TempTransD
    
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportACS1(hFacC,dxF,drF,nt,V,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through plane ACS1, defined by indices ny = 197:, nx = :40
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dxF : Width of cell though cell center in x-dir or along-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               V  : Across-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]*Tr[t,:,i,:]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dxF[197,:40],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,:40]*area*V[time,:,197,:40]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,:40]*area*V[time,:,197,:40]*Tr[time,:,197,:40]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportACS2(hFacC,dxF,drF,nt,V,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through plane ACS2, defined by indices ny = 197:, nx = 40:120
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dxF : Width of cell though cell center in x-dir or along-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               V  : Across-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]*Tr[t,:,i,:]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dxF[197,40:120],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,40:120]*area*V[time,:,197,40:120]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,40:120]*area*V[time,:,197,40:120]*Tr[time,:,197,40:120]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')
        
#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportACS3(hFacC,dxF,drF,nt,V,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through plane ACS3, defined by indices ny = 197:, nx = 120:240, nz = 0:30
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dxF : Width of cell though cell center in x-dir or along-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               V  : Across-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]*Tr[t,:,i,:]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dxF[197,120:240],drF[:30])
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:30,197,120:240]*area*V[time,:30,197,120:240]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:30,197,120:240]*area*V[time,:30,197,120:240]*Tr[time,:30,197,120:240]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')
    
#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportACS4(hFacC,dxF,drF,nt,V,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through plane ACS4, defined by indices ny = 197:, nx = 240:320
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dxF : Width of cell though cell center in x-dir or along-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               V  : Across-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]*Tr[t,:,i,:]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dxF[197,240:320],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,240:320]*area*V[time,:,197,240:320]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,240:320]*area*V[time,:,197,240:320]*Tr[time,:,197,240:320]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportACS5(hFacC,dxF,drF,nt,V,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through plane ACS5, defined by indices ny = 197:, nx = 320:360
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dxF : Width of cell though cell center in x-dir or along-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               V  : Across-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]*Tr[t,:,i,:]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dxF[197,320:-1],drF)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,320:-1]*area*V[time,:,197,320:]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[:,197,320:-1]*area*V[time,:,197,320:]*Tr[time,:,197,320:-1]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')
#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportACS3b(hFacC,dxF,drF,nt,V,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through plane ACS3b, defined by indices ny = 197:, nx = , nz = 30:.
    INPUT: 
            hFacC : Open fraction of bottom cell at cell-center (nz,ny,nx)
              dxF : Width of cell though cell center in x-dir or along-shore (ny,nx).
              drF : Distance between cell interfaces (nz)
               nt : Time number of output files 
               V  : Across-shore component of velocity, unstaggered to cell center grid (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]))
            trans(t) = sum(sum(hFacC[:,:,i]*drF[:]*dxF[i,:]*U[t,:,i,:]*Tr[t,:,i,:]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'

    TempTransD = np.zeros(nt)
    area = np.meshgrid(dxF[197,120:240],drF[30:])
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[30:,197,120:240]*area*V[time,30:,197,120:240]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(hFacC[30:,197,120:240]*area*V[time,30:,197,120:240]*Tr[time,30:,197,120:240]))
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportLID1(rA,WC,nt,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through a lid over the canyon, defined by indices ny = 197:, nx = 120:180, nz = 30
    INPUT: 
               rA : area of cell 
               nt : Time number of output files 
               WC  : Vertical velocity (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(rA[]*WC[]*trac[]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'
    
    SB = 30

    TempTransD = np.zeros(nt)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(rA[197:,120:180]*WC[time,SB,197:,120:180]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(rA[197:,120:180]*WC[time,SB,197:,120:180]*trac[time,SB,197:,120:180])) 
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')

#--------------------------------------------------------------------------------------------------------------------------
       
def AdvTransportLID2(rA,WC,nt,Tr=0,transType=0): 
    """
    Calculate advective transport of water or tracers through a lid over the canyon, defined by indices ny = 197:, nx = 180:240, nz = 30
    INPUT: 
               rA : area of cell 
               nt : Time number of output files 
               WC  : Vertical velocity (nt,nz,ny,nx)
               Tr : Array for any tracer, e.g. temp, sal, NO3. Default is no array.
         transType: Integer to specify if the trasport to calculate is of water (default 0) or tracers (1)
    
    TRANSPORT CALCULATION:
            trans(t) = sum(sum(rA[]*WC[]*trac[]))
    OUTPUT:
            trans (size = nt)
    
    """
    assert type(transType) == int, 'transType is not an integer'
    
    SB = 30

    TempTransD = np.zeros(nt)
    
    if transType == 0:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(rA[197:,180:240]*WC[time,SB,197:,180:240]))  
        
        return TempTransD
    
    elif transType == 1:
        
        for time in range(0,nt,1):
            
            TempTransD[time] = np.sum(np.sum(rA[197:,180:240]*WC[time,SB,197:,180:240]*trac[time,SB,197:,180:240])) 
            
        return TempTransD
   
    else:
        
        print (' transType should be either 0 or 1 ')
    