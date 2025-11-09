#Logic for positioning of edges between Nodes
'''1.)If index of node is odd or position is even then we have its position as (poscount,1)
where poscount increases from 1 to so on and forth.Scaling of pos_count is done to enhance visibility
2.)If index of node is even or position is odd then we have its position as (poscount,-1)
3.)if node is a starting node/number node then its pos is (0,0)
4.)if node is a ending node/1 node then its pos is (pos_count*scaling_factor,0)'''

def positioner(CLG_Nodes):
    position={}
    pos_count=0
    for index in range(len(CLG_Nodes)):
      if index!=0 and index!=len(CLG_Nodes)-1:
        pos_count+=1
        if index%2==0:
          position[CLG_Nodes[index]]=(pos_count*40,-90)
        else:
          position[CLG_Nodes[index]]=(pos_count*40,90)
      if index==0:
          position[CLG_Nodes[index]]=(-100,0)
      if index==len(CLG_Nodes)-1:
          position[CLG_Nodes[index]]=(pos_count*43,0) 
    return position    

