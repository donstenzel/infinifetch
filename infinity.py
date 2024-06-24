#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import vectorize
import time, sys, psutil, platform

                ##################                                                   #################                 
            ###########################                                         ###########################            
         ##################################                                 ##################################         
       ############            ###############                           ###############            ############       
     ##########                      ############                     #############                      #########     
    ########                            ###########                 ###########                            ########    
   #######                                 ###########           ##########                                   ######   
  ######                                      ##########       ##########                                      ######  
  #####                                          #########   #########                                          #####  
 #####                                             #################                                             ##### 
 ####                                                #############                                                #### 
 ####            o-- Infinity --o                      #########                                                  #### 
 ####                                                #############                                                #### 
 #####                                             #################                                             ##### 
  #####                                          #########   #########                                          #####  
  ######                                      ##########       ##########                                      ######  
   #######                                 ###########           ##########                                   ######   
    ########                            ###########                 ###########                            ########    
     ##########                      ############                     #############                      #########     
       ############            ###############                           ###############            ############       
         ##################################                                 ##################################         
            ###########################                                         ###########################            
                ##################                                                   #################                 



GLOBAL_SCALING = 0.4
NUM_POINTS = 1000
NUM_COLORS = 30
NUM_FRAMES = 5000

FOCAL_DISTANCE = 1

HALF_WIDTH = FOCAL_DISTANCE * 2**.5

COLOR_END = "\033[0m"

def cursor(x, y):
    return f"\033[{y};{x}H"

@vectorize
def x(t):
    return (HALF_WIDTH * np.cos(t)) / (np.sin(t) **2 +1)

@vectorize
def y(t):
    return (HALF_WIDTH * np.cos(t) * np.sin(t)) / (np.sin(t) **2 +1)

@vectorize
def round_v(i): return round(i)

def color(frame, index):
    scalar = NUM_POINTS / NUM_COLORS
    return int(((frame + index) % NUM_POINTS) / scalar) +1

def main():
    match sys.argv:
        case [this]:
            scale = GLOBAL_SCALING
            f_count = NUM_FRAMES
        case [this, inpscale]:
            try:
                scale = float(inpscale)
            except:
                print("Usage: ./infinity.py [scale: float = 0.4] [frames: int = 5000]\nNote: some scales may not work because of rounding details and shit")
        case [this, inpscale, frames]:
            try:
                scale = float(inpscale)
                f_count = int(frames)
            except:
                print("Usage: ./infinity.py [scale: float = 0.4] [frames: int = 5000]\nNote: some scales may not work because of rounding details and shit")


    colors = [
        "\033[38;5;231m",
        "\033[38;5;196m",
        "\033[38;5;202m",
        "\033[38;5;208m",
        "\033[38;5;214m",
        "\033[38;5;220m",
        "\033[38;5;226m",
        "\033[38;5;190m",
        "\033[38;5;154m",
        "\033[38;5;118m",
        "\033[38;5;082m",
        "\033[38;5;046m",
        "\033[38;5;047m",
        "\033[38;5;048m",
        "\033[38;5;049m",
        "\033[38;5;050m",
        "\033[38;5;051m",
        "\033[38;5;045m",
        "\033[38;5;039m",
        "\033[38;5;033m",
        "\033[38;5;027m",
        "\033[38;5;021m",
        "\033[38;5;057m",
        "\033[38;5;093m",
        "\033[38;5;129m",
        "\033[38;5;165m",
        "\033[38;5;201m",
        "\033[38;5;200m",
        "\033[38;5;199m",
        "\033[38;5;198m",
        "\033[38;5;197m",
    ]

    colors = colors + colors[::-1] # palindrome so the rainbow looks nice ~

    r = np.linspace(0, 2 * np.pi, num= NUM_POINTS)


    # x range and y range are 
    xs = round_v(x(r) * 100 * scale)
    x_range = max(xs) - min(xs)
    xs = xs + ((x_range / 2) + 2)

    ys = round_v(y(r) *  50 * scale)
    y_range = max(ys) - min(ys)
    ys = ys + ((y_range / 2) + 2)

    mat = np.zeros((int(y_range) +5, int(x_range) +5))
    
    def str_m(m):
        return '\n'.join(''.join(f"{colors[int(elem)]}{"#" if int(elem) > 0 else " "}{COLOR_END}" for elem in row) for row in m)

    def str_at(string, x, y):
        return f"{cursor(x, y)}{string}"

    # clear the screen
    print("\033[2J")
    # init info with empty strings, then fill static entries, then print static entries.
    # info = ["" for _ in range(y_range +5)]

    # os_info = platform.freedesktop_os_release()
    # info[1] = f"\033[38;5;129m-~ Infinity{COLOR_END}"
    # info[2] = f"\033[38;5;129m-~ OS: {os_info["NAME"]}{COLOR_END}"
    # info[3] = f"\033[38;5;129m-~ Release: {platform.release()}{COLOR_END}"
    # info[4] = f"\033[38;5;129m-~ Version: {platform.version()}{COLOR_END}"
    # info[5] = f"\033[38;5;129m-~ Architecture: {platform.machine()}{COLOR_END}"
    
    # # CPU
    # cpufreq = psutil.cpu_freq()
    # info[7] = f"\033[38;5;129m-~ Processor: {platform.processor()}{COLOR_END}"
    # info[8] = f"\033[38;5;129m-~ Physical Cores: {psutil.cpu_count(logical= False)}{COLOR_END}"
    # info[9] = f"\033[38;5;129m-~ Total Cores: {psutil.cpu_count(logical= True)}{COLOR_END}"
    # info[10] = f"\033[38;5;129m-~ Min Frequency: {cpufreq.min:.2f}Mhz{COLOR_END}"
    # info[11] = f"\033[38;5;129m-~ Max Frequency: {cpufreq.max:.2f}Mhz{COLOR_END}"


    frame = 0
    frame_diff = 1
    # for each frame
    while True:
        
        # # print dynamic info every 10th frame
        # if frame % (10 * frame_diff) == 0:
        #     cpufreq = psutil.cpu_freq()
        #     info[12] = f"\033[38;5;129m-~ Current Frequency: {cpufreq.current:.2f}Mhz{COLOR_END}"
        #     info[13] = f"\033[38;5;129m-~ Total CPU Usage: {psutil.cpu_percent()}%"
        #     info[-1] = f"Frame: {frame}"
        #     [print(f"{cursor(i, x_range +6)}{entry}") for i, entry in enumerate(info)]


        # for each point
        for i in range(NUM_POINTS):

            # consider a 5x5 grid centered on that point
            for n in range(-1, 2):
                for m in range(-1, 2):

                    # and set the color according to the frame and how far along the curve
                    mat[int(ys[i]) +n][int(xs[i]) +m] = color(frame + (n + m) * -10, i)
                    # we index the matrix with the point, color is addition modulo NUM_POINTS
                    # and (n + m) * -10 is an offset so it looks a little less solid color

        # then print out the result in the top left corner
        print(f"{cursor(1, 1)}{str_m(mat)}")
        print(str_at("o-- Infinity --o", int(x_range / 4) - 8, int(y_range / 2) +3))

        frame = frame + frame_diff

        time.sleep(1/61) # cursed 'works on my machine' ass pause
        if frame > f_count: break


if __name__ == "__main__":
    main()
