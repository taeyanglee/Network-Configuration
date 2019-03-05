import networkx as nx
import os
import io
import matplotlib.pyplot as plt
from pprint import pprint

def data2graph(data_path) :
    """ read the data from the data_path and generate graph instance considering the data indicates nodes or link   
    Args :
        data_path : data path of data files                
    Returns:
        Add nodes or link in nx.Graph instance
    """
    


    # Network = nx.Graph()               
    Network = nx.MultiDiGraph()               
    fileDirectory = os.path.join(data_path,"JejuIsland_NODE.csv")

    print("###"*30, "JejuIsland_NODE is configurated from here")    
    with open(fileDirectory, mode = 'r', encoding = 'utf-8-sig') as nodeData :
        # 한글이 들어있는 데이터에 대해서 아래와 같은 오류코드가 나오게 되지만
        # UnicodeDecodeError: 'cp949' codec can't decode byte 0x80 in position 284: illegal multibyte sequence
        # encoding = utf-8-sig 설정으로 이 부분에 대한 오류를 고칠 수 있음
       
        # 데이터 읽기, data_path 안에 들어있는 Node.txt 라는 파일 읽음
        # node.txt 는 https://nodelink.its.go.kr/ 에서 다운로드 받을 수 있음
        # 이 부분에 대해서 최신 업데이트를 할 수 있도록, 웹크롤링 및 다운로드하는 방법에 대해서 추후 진행 가능        
        # 전처리를 ArcMap을 통해서 걷친 데이터를 가지고 옴.
        # ArcMap에서 Node에 X,Y Position을 추가하였고, 특정지역에 원하는 데이터만(jeju island) csv 형태로 꺼내옴

        keysOfNodes = nodeData.readline().strip().split(',')
        print("\n", "---"*10, "keysOfNodes is following", "---"*35)
        print(keysOfNodes)
        # print("---"*54)
        
        a = nodeData.readlines()
        position =  dict()
        for idx, readLines in enumerate(a ) :
            # print("index is",idx,"readLines are", readLines)
            line = readLines.strip().split(',')
            node_dict = dict( zip (keysOfNodes, line) ) 
            (nodeID, x, y )= (node_dict['NODE_ID'], node_dict['POINT_X'] , node_dict['POINT_Y'] )
            Network.add_node(nodeID, pos = (x,y) )            
            position[nodeID] = [x,y]

            for key, datum in zip(keysOfNodes, line):
                Network.node[nodeID][key] = datum
            # 이렇게 짜게 되면 Point_X와 Point_Y 의 데이터가 중첩되서 들어가지만, position을 사용하려면 어쩔수 없음.
            # 다른 방법으로 짜는 방법도 고려해 볼 것.
            

    print("total %d node is loaded to network."%(len(Network.node)))
    # print("\n network node is following")
    print(Network.node)
    print("###"*30, "JejuIsland_NODE is configurated")
    print("---"*54)


    # '''From here Link loading is begins '''
    
    # print("\n"*3)
    # print("###"*30, "JejuIsland_Link is configurated from here")

    # fileDirectory = os.path.join(data_path,"JejuIsland_Link.csv")
    # with open(fileDirectory, mode='r', encoding = 'utf-8-sig') as linkData :
        # keysOfLink = linkData.readline().strip().split(',')
        # print("\n", "---"*10, "keysOfLink is following", "---"*35)
        # print(keysOfLink)
        # print("---"*54)

        # # LINK_ID, F_NODE, T_NODE
        # a = linkData.readlines()        
        # for idx, readLines in enumerate(a) :
            # # print("index is",idx,"readLines are", readLines)            
            # line = readLines.strip().split(',')
            # Link_dict = dict( zip (keysOfLink, line) ) 
            # (LinkID,F_NODE, T_NODE ) = (Link_dict['LINK_ID'],Link_dict['F_NODE'],Link_dict['T_NODE'])
            # if (F_NODE in Network.node) and (T_NODE in Network.node) :
                    
                # Network.add_edge(F_NODE,T_NODE,**Link_dict)
                # # print(Link_dict)
                # # for key, datum in zip(keysOfLink, line):
                    # # Network.add_edges[F_NODE][T_NODE][key] = datum


            # # Network.add_edge(F_NODE,T_NODE,**Link_dict)
            # # print(dir(Network))
            # # for key, datum in zip(keysOfLink, line):
                # # Network.edges[F_NODE][T_NODE][key] = datum

            
    
    # print("total %d link is loaded to network."%(len(Network.edges)))
    # # print("\n network link is following")
    # # print(Network.edges)
    # print("###"*30, "JejuIsland_LINK is configurated")
    # print("---"*54)

    return Network, position

    
    
    
    
if __name__ == '__main__':
    # node and path data must be in the same route        
    data_path = '.\\data'    
    (Network, position) = data2graph(data_path)
    
    print(nx.info(Network))
    plt.figure()    
    pos = nx.get_node_attributes(Network,'pos')
    f = open("positionOfNodes.txt",'w')
    i = 1
    for datum in pos :
        f.write(datum)
        if i %2 == 0 :             
            f.write("\n")
        else :
            f.write("\t")
        i += 1
            
    f.close
    # print( pos)
    # nx.draw(Network, node_size=5,node_color='pink' )
    # # nx.draw(Network, position, node_size=5,node_color='pink' )
    # # # nx.draw(Network, position, edge_color='black',width=1,linewidths=1,node_size=50,node_color='pink' )
    # plt.axis('on')

    # plt.show()