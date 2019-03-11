import networkx as nx
import os
import io
import matplotlib.pyplot as plt
from pprint import pprint

def data2graph(data_path,GraphType) :
    """ read the data from the data_path and generate graph instance considering the data indicates nodes or link   
    Args :
        data_path : data path of data files
        GraphType : (GraphType,Network) = (1,MultiDiGraph())
                                        = (2,MultiGraph())
                                        = (3,DiGraph())
                                        = (4,Graph())
    Returns:
        Add nodes and link in nx.Graph instance
    """
    # COMMENT BEGIN(2019/03/05)
    # In the first line of the function comment, do not start with a space. 
    # In the 'Returns' part, you should write what objects the function returns; for now, you have written what function does. This function returns Network, position tuple, so write about it: type and what does the variable contains. 
    # If you write your thesis in Korean, it is recommended to write in Korean, since comments in your code will be re-used in the thesis. 
    # COMMENT END(2019/03/05)
    
    
    if GraphType == 1:
        Network = nx.MultiDiGraph()
    elif GraphType ==2 :
        Network = nx.MultiDiGraph()
    elif GraphType ==3 :
        Network = nx.MultiDiGraph()
    else :
        Network = nx.MultiDiGraph()
        
    fileDirectory = os.path.join(data_path,"Jeju_Island_Node.csv")
    # COMMENT BEGIN(2019/03/05)
    # when using print statement, I suggest to use quiet option so that you can choose whether to see the debug statements. 
    # COMMENT END(2019/03/05)
    
    # print("###"*30, "JejuIsland_NODE is configurated from here")    
    with open(fileDirectory, mode = 'r', encoding = 'utf-8-sig') as nodeData :      
        # 데이터 읽기, data_path 안에 들어있는 Node.txt 라는 파일 읽음
        # todo :
        # node.txt 는 https://nodelink.its.go.kr/ 에서 다운로드 받을 수 있음
        # 이 부분에 대해서 최신 업데이트를 할 수 있도록, 웹크롤링 및 다운로드하는 방법에 대해서 추후 진행 가능        
        # 전처리를 ArcMap을 통해서 걷친 데이터를 가지고 옴.
        # ArcMap에서 Node에 X,Y Position을 추가하였고[POSITION_X][POSITION_Y], 특정지역에 원하는 데이터만(jeju island) csv 형태로 저장
        
        keysOfNodes = nodeData.readline().strip().split(',')
        print("\n", "---"*10, "keysOfNodes is following", "---"*35)
        print(keysOfNodes)

        for idx, readLines in enumerate( nodeData.readlines() ) :
            # print("index is",idx,"readLines are", readLines)
            line = readLines.strip().split(',')
            node_dict = dict( zip (keysOfNodes, line) ) 
            (nodeID, x, y )= (node_dict['NODE_ID'], node_dict['x'] , node_dict['y'] )
            Network.add_node(nodeID, pos = (x,y) )            
            for key, datum in zip(keysOfNodes, line):
                nx.set_node_attributes(Network,key,datum)
                Network.node[nodeID][key] = datum
           
    print("total %d node is loaded to network."%(len(Network.node)))
    # print("\n network node is following")
    # print(Network.node)
    print("###"*30, "JejuIsland_NODE is configurated")
    print("---"*54)

    # '''From here Link loading is begins '''    
    # # print("\n"*3)
    # # print("###"*30, "JejuIsland_Link is configurated from here")

    # fileDirectory = os.path.join(data_path,"Jeju_Island_link.csv")
    # with open(fileDirectory, mode='r', encoding = 'utf-8-sig') as linkData :
        # keysOfLink = linkData.readline().strip().split(',')
        # print("\n", "---"*10, "keysOfLink is following", "---"*35); print(keysOfLink) ;print("---"*54)

        # a = linkData.readlines()        
        # for idx, readLines in enumerate(a) :
            # # print("index is",idx,"readLines are", readLines)            
            # line = readLines.strip().split(',')            
            # Link_dict = dict( zip (keysOfLink, line) ) 
            # (LinkID,F_NODE, T_NODE ) = (Link_dict['LINK_ID'],Link_dict['F_NODE'],Link_dict['T_NODE'])
            # if (F_NODE in Network.node) and (T_NODE in Network.node) :
                    
                # Network.add_edge(F_NODE,T_NODE,**Link_dict)
                # # print(Network.edges)
                # # for key, datum in zip(keysOfLink, line):
                    # # # nx.set_edge_attributes(Network,key,datum)
                    # # # Network.edge[F_NODE,T_NODE][key] = datum
                    # # # Network.edge[F_NODE][T_NODE][key] = datum
                    # # # Network.node[nodeID][key] = datum
                    # # Network.add_edge(F_NODE, T_NODE, **Link_dict)
                    
        # # nx.set_edge_attributes(Network,key,datum)
        # # print(Link_dict)
        
        # # print(Network.edges(data=True))


            # # Network.add_edge(F_NODE,T_NODE,**Link_dict)
            # # print(dir(Network))
            # # for key, datum in zip(keysOfLink, line):
                # # Network.edges[F_NODE][T_NODE][key] = datum

            
    
    # print("total %d link is loaded to network."%(len(Network.edges)))
    # # print("\n network link is following")
    # # print(Network.edges)
    # print("###"*30, "JejuIsland_LINK is configurated")
    # print("---"*54)

    return Network
    # , position
   
    
    
    
if __name__ == '__main__':
    # node and path data must be in the same route        
    data_path = '.\\data'    
    Network = data2graph(data_path,1)    
    print(nx.info(Network))
    print(Network.node(data = True))
    # plt.figure()    
    # pos = nx.get_node_attributes(Network,'pos')
    # f = open("positionOfNodes.txt",'w')
    # i = 1
    # for datum in pos :
        # f.write(datum)
        # if i %2 == 0 :             
            # f.write("\n")
        # else :
            # f.write("\t")
        # i += 1
            
    # f.close
    # print( pos)
    # nx.draw(Network, node_size=5,node_color='pink' )
    # nx.draw_networkx_nodes(Network, pos, node_size=1, node_shape='o', node_color='red')
    # nx.draw_networkx_edges(Network, pos, width=10, alpha=0.8, edge_color='crimson')
    # nx.draw(Network, pos, node_size=10,node_color='blue' )
    # # # # # nx.draw(Network, position, edge_color='black',width=1,linewidths=1,node_size=50,node_color='pink' )
    # plt.axis('off')
    # plt.show()