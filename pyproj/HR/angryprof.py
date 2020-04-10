# Complete the angryProfessor function below.
def angryProfessor(k, a):
    u=len(list(filter(lambda x: (x<2), a)))
    if u>=k:
        return ('YES')
    else:
        return ('NO')