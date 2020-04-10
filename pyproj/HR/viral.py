def viralAdvertising(n):
    shared=5
    val=0
    for i in range(n):
        res= abs(shared//2)
        shared=res*3
        val+=res
    return val  