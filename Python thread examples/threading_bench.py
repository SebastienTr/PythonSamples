#!/usr/bin/python3

from threading import Thread

def func_with_heavy_calculation():
    i = 0
    while i < 1000000:
        i += 1
        heavy_calc = i % 42


def with_one_thread():
    func_with_heavy_calculation()

def with_two_thread():
    thread_one = Thread(target=func_with_heavy_calculation)
    thread_two = Thread(target=func_with_heavy_calculation)
    thread_one.start()
    thread_two.start()
    thread_one.join()
    thread_two.join()

