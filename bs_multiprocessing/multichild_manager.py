#_*_coding:utf-8 _*_
#!/usr/bin/env python
# $Id$
__author__ = 'archmagece'

import multiprocessing
'''
    @author: archmagece
    @since : 2014-03-07
'''

class WorkerManager():

    def __init__(self, worker_status):
        self.worker_status = worker_status
        self.process_hash = dict()
        pass

    def add_process(self, name, target, args):
        """
        name : process name
        target : target method
        args : arguments tuple ()
        """
        if name not in self.process_hash or not self.process_hash[name].is_alive():
            self.process_hash[name] = multiprocessing.Process(name=name, target=target, args=args)
            self.process_hash[name].start()
            pass
        return self.process_hash[name]
        #pass

    def remove_process(self, name):
        """
        name : process name
        """
        self.process_hash[name].terminate()
        return self.process_hash[name].pop(name)
        #pass

    def count(self):
        """
        process count
        """
        return len(self.process_hash)
        #pass
    pass

