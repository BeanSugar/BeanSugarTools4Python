#!/usr/bin/env python
#_*_coding:utf-8 _*_
# $Id$
__author__ = 'archmagece'

'''
Created on 2013. 3. 19.

@author: archmagece@gmail.com
'''

import multiprocessing


class Worker(multiprocessing.Process):

    def __init__(self, work_queue, result_queue):

        # base class initialization
        multiprocessing.Process.__init__(self)

        # job management stuff
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.kill_received = False

    def run(self):
        while not self.kill_received:

            # get a task
            try:
                #job = self.work_queue.get_nowait()
                job = self.work_queue.get(2)
            except multiprocessing.Queue.Empty:
                break

            # the actual processing
            print("Starting " + str(job) + " ...")
            #delay = random.randrange(1,10)
            #time.sleep(delay)

            # store the result
            #self.result_queue.put(delay)
            self.result_queue.put(job)

