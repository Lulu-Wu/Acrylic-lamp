import time
from globalVal import globalVal,const
from init import np

def cold_light():
    np.fill((60, 60, 60))
    np.write()
    
def warm_light():
    np.fill((48, 24, 0))
    np.write()

def spring():
    np.fill((0, 80, 8))
    np.write()
    
def summer():
    np.fill((96, 0, 0))
    np.write()
    
def autumn():
    np.fill((96, 12, 0))
    np.write()
    
def winter():
    np.fill((0, 4, 96))
    np.write()
    
def rain_bow_show():
    for i in range(24):
        if globalVal.mode != 6:
            break
        if globalVal.first_rainbow == 1:
            np.fill((4*(i+1), 0, 0))
            np.write()
        else:
            np.fill((4*24, 0, 4*24-4*(i+1)))
            np.write()
        time.sleep(0.2)
    globalVal.first_rainbow = 2
    for i in range(24):
        if globalVal.mode != 6:
            break
        np.fill((4*24, 2*(i+1), 0))
        np.write()
        time.sleep(0.2)
    for i in range(24):
        if globalVal.mode != 6:
            break
        np.fill((4*24, 2*24+2*(i+1), 0))
        np.write()
        time.sleep(0.2)
    for i in range(24):
        if globalVal.mode != 6:
            break
        np.fill((4*24-4*(i+1), 4*24, 0))
        np.write()
        time.sleep(0.2)
    for i in range(24):
        if globalVal.mode != 6:
            break
        np.fill((0, 4*24-4*(i+1), 4*(i+1)))
        np.write()
        time.sleep(0.2)
    for i in range(24):
        if globalVal.mode != 6:
            break
        np.fill((0, 4*(i+1), 4*24))
        np.write()
        time.sleep(0.2)
    for i in range(24):
        if globalVal.mode != 6:
            break
        np.fill((4*(i+1), 4*24-4*(i+1), 4*24))
        np.write()
        time.sleep(0.2)