def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i-1)

print(regressiva(3))