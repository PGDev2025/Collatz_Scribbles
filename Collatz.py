#Returns all the node points or nodes for the graph after computing the collatz sequence for input number
def Collatz_Graph(Number):
    if Number==1:
        return [1]
    CLGraph=[]
    Temp=Number
    while Temp!=1:
        CLGraph.append(Temp)
        if Temp%2==0:
            Temp=Temp//2
        else:
            Temp=3*Temp+1
    CLGraph.append(1)
    return CLGraph

