class SnakeQueue:
    def __init__(self,vertex=0,distance=0):
        self.vertex=vertex
        self.distance=distance

    def moves(self,N,arr):
        visited=[False]*(N)
        visited[0]=True
        #print(visited)
        queue=[]
        queue.append(SnakeQueue(0,0))
        q=SnakeQueue()
        while queue:
            q=queue.pop(0)
            q_vertex=q.vertex
            q_distance=q.distance
            if(q_vertex==N-1):
                break
            j=q_vertex+1
            while(j <= q_vertex+6 and j < N):
                if(visited[j]==False):
                    q_new=SnakeQueue()
                    q_new.distance=q_distance+1
                    visited[j]=True
                    if(arr[j] != -1):
                        q_new.vertex=q_vertex
                    else:
                        q_new.vertex=j
                    queue.append(q_new)
                j+=1
        return q.distance

if __name__=="__main__":
    N = 30
    arr=[-1]*N
    # Ladders
    arr[2]=21
    arr[4]=7
    arr[10]=25
    arr[19]=28
    # Snakes
    arr[26]=0
    arr[20]=8
    arr[16]=3
    arr[18]=6
    ob=SnakeQueue()
    print(ob.moves(N,arr))
