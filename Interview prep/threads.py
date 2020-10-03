import time
import threading


class myThread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter


    def run(self):
        print('starting: ', self.name)
        print_time(self, self.thread_id, 4, False)


def print_time(thread_name,counter, delay,flag):
    while counter > 0:
        if flag:
            thread_name.exit()
        counter -= 1
        time.sleep(delay)
        print('%s %s', thread_name, time.ctime(time.time()))

def two_threads():

    thread_1 = myThread(1, 'one', 5)
    thread_2 = myThread(2, 'two', 3)

    thread_1.start()
    thread_2.start()
two_threads()