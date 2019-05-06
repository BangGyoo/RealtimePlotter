#!/usr/bin/env python3
'''
Real-time plot demo using sine waves.

Copyright (C) 2015 Simon D. Levy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
'''

from realtime_plot import RealtimePlotter
import numpy as np

# Simple example with threading

class _SinePlotter(RealtimePlotter):
    
    def __init__(self):
        RealtimePlotter.__init__(self, [(-10,+10),(50,100)], 
                yticks = [(-10,0,+30),(0,50,100)],
                styles = ['r-','g-'], 
                ylabels=['Temperature','humidity'])
        self.timer = 0
        self.xcurr = 13
        self.huminity = 60

    def getValues(self):

        s = self._getRow(1)
        c = self._getRow(2)
	
        from time import sleep
        sleep(1)
        return  s,c, s, c

    def _getRow(self, row):

        #size = len(self.x)

        #angle = 2*np.pi*(float(self.xcurr)%size)/size
        '''
        if self.xcurr is 0.5 :
            self.xcurr = 0
        elif self.xcurr is 0 :
            self.xcurr = -0.5
        else :
            self.xcurr = 0.5
'''
        return self.xcurr if row is 1 else self.huminity

def _update(plotter):

    from time import sleep
    import random

    while True:
        if (0 == plotter.timer%10) :
             plotter.xcurr += random.randint(-1,1)
        plotter.huminity += random.randint(-1,1)
        plotter.timer += 5
        sleep(10)

if __name__ == '__main__':

    import threading

    plotter = _SinePlotter()

    thread = threading.Thread(target=_update, args = (plotter,))
    thread.daemon = True
    thread.start()

    plotter.start()
 
