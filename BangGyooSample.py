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
        RealtimePlotter.__init__(self, [(-1,+1)], 
                
                window_name='Sinewave demo',
                yticks = [(-1,0,+1)],
                styles = ['r--'], 
                ylabels=['Sin'])

        self.xcurr = 0

    def getValues(self):

        s = self._getRow(1)
        c = self._getRow(2)

        return  s,c, s, c

    def _getRow(self, row):

        #size = len(self.x)

        #angle = 2*np.pi*(float(self.xcurr)%size)/size
        
        if self.xcurr is 0.5 :
            self.xcurr = 0
        elif self.xcurr is 0 :
            self.xcurr = -0.5
        else :
            self.xcurr = 0.5

        print(self.xcurr)
        
        return self.xcurr


def _update(plotter):

    from time import sleep

    while True:

        
        sleep(.0001)

if __name__ == '__main__':

    import threading

    plotter = _SinePlotter()

    thread = threading.Thread(target=_update, args = (plotter,))
    thread.daemon = True
    thread.start()

    plotter.start()
 
