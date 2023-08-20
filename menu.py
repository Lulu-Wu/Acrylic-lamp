# 自定义函数
import time
from globalVal import globalVal
from init import np
import show

def menu():
        if globalVal.mode == 0:
            while True:
                if globalVal.mode != 0:
                    break
                show.cold_light()
            
        elif globalVal.mode == 1:
            while True:
                if globalVal.mode != 1:
                    break
                show.warm_light()
        
        elif globalVal.mode == 2:
            while True:
                if globalVal.mode != 2:
                    break
                show.spring()
            
        elif globalVal.mode == 3:
            while True:
                if globalVal.mode != 3:
                    break
                show.summer()
            
        elif globalVal.mode == 4:
            while True:
                if globalVal.mode != 4:
                    break
                show.autumn()
                
        elif globalVal.mode == 5:
            while True:
                if globalVal.mode != 5:
                    break
                show.winter()
                
        elif globalVal.mode == 6:
            while True:
                if globalVal.mode != 6:
                    break
                show.rain_bow_show()

        

