from tkinter import *
from tkinter.messagebox import showinfo
from UCS import generateDirectedGraph,UCS_code
import networkx as nx
import matplotlib.pyplot as plt

def djkstra():
    plt.clf()
    lsb_dijkstra.delete(0)
    length1_dijkstra.delete(0)
    directed_weighted_graph=generateDirectedGraph(weighted_edges)
    Bool_ip1 = False
    Bool_ip2 = False
    for i in weighted_edges:
        if input1_dj.get() in i:
            Bool_ip1 = True
        if input2_dj.get() in i:
            Bool_ip2 = True
    if Bool_ip1 ==True and Bool_ip2 == True:
        ucs =UCS_code(directed_weighted_graph,input1_dj.get(), input2_dj.get())
        lsb_dijkstra.insert(0,ucs[0])
        length1_dijkstra.insert(0,ucs[1])
        s1=ucs[0].split('-')
        print(s1)
        list_dj=[]
        if input1_dj.get()!=input2_dj.get():
            for i in range(len(s1)):
                try:
                    list_dj.append([s1[i],s1[i+1]])
                    list_dj.append([s1[i+1],s1[i]])
                except:
                    pass
            for i in list_dj:
                elarge = [(u, v) for (u, v, d) in G.edges(data=True) if u==i[0] and v==i[1]]
                esmall = [(u, v) for (u, v, d) in G.edges(data=True) if u!=i[0] and v!=i[1]]
                pos = nx.spring_layout(G, seed=7) 
                nx.draw_networkx_nodes(G, pos, node_size=700)
                nx.draw_networkx_edges(G, pos, edgelist=esmall, width=1)
                nx.draw_networkx_edges(
                G, pos, edgelist=elarge, width=4, edge_color="r"
                )
                nx.draw(G, pos)
                nx.draw_networkx_edge_labels(G, pos)
                nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
            plt.show()
    else:
        showinfo('Lỗi','Không tìm thấy đường đi!')
        draw_edge()
def delete(event):
    global lsb,i
    possition_list=lsb.curselection()
    lsb.delete(int(possition_list[0]))
    G.remove_edge(weighted_edges[int(possition_list[0])][0],weighted_edges[int(possition_list[0])][1])
    list_position=weighted_edges[int(possition_list[0])]
    for edges in weighted_edges:
        if edges[0]==list_position[0] and edges[1]==list_position[1] and edges[2]==list_position[2] or edges[0]==list_position[1] and edges[1]==list_position[0] and edges[2]==list_position[2]: 
             weighted_edges.remove(edges)
    i-=1
    draw_edge()
    lsb_dijkstra.delete(0)
    length1_dijkstra.delete(0)
def start():
    global i
    weighted_edges.append([input1.get(),input2.get(),float(input3.get())])
    G.add_edge(input1.get(),input2.get(),km=float(input3.get()))
    lsb.insert(END,weighted_edges[i][0]+' đến '+weighted_edges[i][1]+' là '+ str(weighted_edges[i][2])+' km')
    i+=1
    label1_input.delete(0,END)
    label2_input.delete(0,END)
    label3_input.delete(0,END)
    draw_edge()
def draw_edge():
    plt.clf()
    pos = nx.spring_layout(G, seed=7) 
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos,width=1)
    nx.draw_networkx_edges(G, pos,width=1)
    nx.draw(G, pos)
    nx.draw_networkx_edge_labels(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    plt.show()

def request():
    global i
    plt.clf()
    G.clear()
    weighted_edges.clear()
    i=0
    lsb_dijkstra.delete(0)
    length1_dijkstra.delete(0)
    lsb.delete(0,END)
    label1_input.delete(0,END)
    label2_input.delete(0,END)
    label3_input.delete(0,END)
    label1_dijkstra_input.delete(0,END)
    label2_dijkstra_input.delete(0,END)
    plt.show()
window = Tk()
window.title('Tìm đường đi ngắn nhất')
window.geometry("500x600+900+100")
plt.rcParams["figure.figsize"] = (8,6)
weighted_edges=[]
G=nx.Graph()
input1=StringVar()
input2=StringVar()
input3=StringVar()
label1=Label(window,text='Điểm bắt đầu')
label1.place(x=200,y=10)
label1_input=Entry(window,textvariable=input1)
label1_input.place(x=180,y=30)

label2=Label(window,text='Điểm kết thúc')
label2.place(x=200,y=50)
label2_input=Entry(window,textvariable=input2)
label2_input.place(x=180,y=70)

label3=Label(window,text='Độ dài')
label3.place(x=200,y=90)
label3_input=Entry(window,textvariable=input3)
label3_input.place(x=180,y=110)
label3_km=Label(window,text='km')
label3_km.place(x=300,y=110)
plot_button = Button(master = window, 
                     command = start,
                     height = 2, 
                     width = 10,
                     text = "Hiển thị")
plot_button.place(x=200,y=130)

global i,lsb
i=0
label_lsb=Label(window,text='Dữ liệu')
label_lsb.place(x=220,y=180)
lsb=Listbox(window)
lsb.place(x=180,y=200)

bt_delete=Button(window,text='Xóa')
bt_delete.place(x=220,y=370)
bt_delete.bind('<Button-1>',delete)
#----------------------------------------------------------------------------
input1_dj=StringVar()
input2_dj=StringVar()
label_dijkstra=Label(window,text='Tìm Đường đi ngắn nhất')
label_dijkstra.place(x=170,y=400)
label1_dijkstra=Label(window,text='Từ')
label1_dijkstra.place(x=100,y=430)
label1_dijkstra_input=Entry(window,textvariable=input1_dj,width=10)
label1_dijkstra_input.place(x=120,y=430)
#------------------Dijkstra----------------------------------
label2_dijkstra=Label(window,text='Đến')
label2_dijkstra.place(x=190,y=430)
label2_dijkstra_input=Entry(window,textvariable=input2_dj,width=10)
label2_dijkstra_input.place(x=220,y=430)

road_dijkstra=Button(window,text='Tìm',width=7,command=djkstra)
road_dijkstra.place(x=290,y=428)

label3_dijkstra=Label(window,text='Đường')
label3_dijkstra.place(x=100,y=460)
lsb_dijkstra=Listbox(window,height=1)
lsb_dijkstra.place(x=140,y=460)
length_dijkstra=Label(window,text='Dài')
length_dijkstra.place(x=265,y=460)
length1_dijkstra=Listbox(window,height=1,width=10)
length1_dijkstra.place(x=290,y=460)

btn_request = Button(master = window,  
                    command=request,                
                     height = 2, 
                     width = 10,
                     text = "Làm mới")
btn_request.place(x=200,y=480)

window.mainloop()
