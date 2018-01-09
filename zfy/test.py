import os
import codecs
def joseph(total, begins, count):
    queue = range(1, total + 1)
    death = (begins + count - 2) % len(queue)
    for times in range(total - 1):
        print ('out: ', queue[death])
        del queue[death]
        death = (death + count -1) % len(queue)
    print ('survivor: ', queue[0])
    

def get_input(input_path):
    with open(input_path) as f:
        rows = f.read().split("\n")
        if len(rows):
            pass
        print (rows)
    
if __name__ == '__main__':
    get_input("a.in")