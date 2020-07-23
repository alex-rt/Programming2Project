from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib,base64
import matplotlib.animation as animation
from matplotlib import style
# Create your views here.

def home(request):

    style.use('fivethirtyeight')

    fig = plt.figure(figsize=(20,10))
    plt.title('Casos de COVID\nSecretaria de salud')
    ax1 = fig.add_subplot(1,1,1)
    plt.xlabel('Comunicado')
    plt.ylabel('Casos Confirmados')
    ax1.grid( color='b', linestyle='-', linewidth=.5)

    plt.legend('u')
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

    def animate(i):
        graph_data = open('C:\\Users\\alexr\\Desktop\\ccodes\\example.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(str(x))
                ys.append(int(y))

        ax1.plot(xs, ys,'r-',label='First Line')

    ani = animation.FuncAnimation(fig, animate,interval=1000)
    #ani.save('./test.gif', writer='imagemagick')
    fig.savefig('./test.png')

#CONERTING TO IMAGE
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string= base64.b64encode(buf.read())
    uri=urllib.parse.quote(string)
    return render(request,'home.html',{'data':uri})
