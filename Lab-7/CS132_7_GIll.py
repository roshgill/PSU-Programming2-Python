from import_code import Graph

def print_friends(graph):
    print("\nThe friends list for all users are:")
    graph.printEdges()

    vertex_len = graph.getSize() - 1
    counter = 0
    while counter <= vertex_len:
        print(f"Friends of {graph.getVertex(counter)}:")
        neighbors = graph.getNeighbors(counter)
        for neighbor in neighbors:
            v = neighbor.return_Edge()
            print(f"{graph.getVertex(v)}")
        
        counter += 1


def add_friends(new_user, graph):
    while True:
        friend_num = (int(input("""Please select who you want to add from this list, add one friend at a time, enter -1 to exit
\n0: Peter\n1: Jane\n2: Mark\n3: Cindy\n4: Wendy\n:""")))    
        if friend_num == -1:
            return       
        if friend_num == 0:
            graph.addEdge(new_user, "Peter")
            graph.addEdge("Peter", new_user)
            print("You have friended Peter.")
        elif friend_num == 1:
            graph.addEdge(new_user, "Jane")
            graph.addEdge("Jane", new_user)
            print("You have friended Jane.")
        elif friend_num == 2:
            graph.addEdge(new_user, "Mark")
            graph.addEdge("Mark", new_user)
            print("You have friended Mark.")
        elif friend_num == 3:
            graph.addEdge(new_user, "Cindy")
            graph.addEdge("Cindy", new_user)
            print("You have friended Cindy.")
        elif friend_num == 4:
            graph.addEdge(new_user, "Wendy")
            graph.addEdge("Wendy", new_user)
            print("You have friended Wendy.")
    
def user_start(graph):
    new_user = str(input("Please add new user\n:"))
    graph.addVertex(new_user)
    
    add_friends(new_user, graph)
    print_friends(graph)

def main():
    vertices = ["Peter", "Jane", "Mark", "Cindy", "Wendy"]
    edge = [[0,1],[0,2],
            [1,0],[1,2],[1,3],
            [2,0],[2,1],[2,3],[2,4],
            [3,1],[3,2],[3,4],
            [4,2],[4,3]]
    
    graph = Graph(vertices,edge)
    
    user_start(graph)
    
main()