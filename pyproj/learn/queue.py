from pythonds.basic import Queue
def lastmanwin(alist,num):
    game=Queue()
    for name in alist:
        game.enqueue(name)
    while game.size()>1:
        for _ in range(num):
            game.enqueue(game.dequeue())
        game.dequeue()
    return game.dequeue()

print(lastmanwin(["Bill","David","Susan","Jane","Kent","Brad"],10))