__author__ = 'archmagece'

import unittest

import multiprocessing
import bs_multiprocessing.multiprocess


class MyTestCase(unittest.TestCase):

    def test_something(self):
        num_jobs = 20
        num_processes = 8

        # run
        # load up work queue
        work_queue = multiprocessing.Queue()
        for job in range(num_jobs):
            work_queue.put(job)

        # create a queue to pass to workers to store the results
        result_queue = multiprocessing.Queue()

        # spawn workers
        for i in range(num_processes):
            worker = bs_multiprocessing.multiprocess.Worker(work_queue, result_queue)
            worker.start()

        # collect the results off the queue
        results = []
        for i in range(num_jobs):
            results.append(str(result_queue.get()))
        print "Result ", results
        self.assertIsNotNone(results)


if __name__ == '__main__':
    unittest.main()
