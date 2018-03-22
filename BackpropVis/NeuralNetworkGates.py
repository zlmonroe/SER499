import numpy as np
from functools import reduce
import itertools
import tkinter
from BackpropVis.ResizeCanvas import ResizeCanvas

I = np.matrix([[.05, .1, .6]])
w1 = np.matrix([[.15, .25, .5], [.2, .3, .5], [.53, .24, .5]])
b1 = .35
w2 = np.matrix([[.4, .5], [.45, .55], [.25, .1]])
b2 = .6
target = np.matrix([.01, .99])
alpha = .5

sigmoid = lambda x: (1 / (1 + np.exp(-x)))

z1 = I * w1
print("Unbiased hidden layer 1:\n" + str(z1) + "\n")

bz1 = z1 + b1
print("Biased hidden layer 1:\n" + str(bz1) + "\n")

sbz1 = sigmoid(bz1)
print("Sigmoid normalized hidden layer 1:\n" + str(sbz1) + "\n")

z2 = sbz1 * w2
print("Unbiased output layer:\n" + str(z2) + "\n")

bz2 = z2 + b2
print("Biased output layer:\n" + str(bz2) + "\n")

out = sbz2 = sigmoid(bz2)
print("Sigmoid normalized output layer:\n" + str(sbz2) + "\n")

errors = .5 * np.square((target - sbz2))
errorSum = np.sum(errors)
print("Errors:\n" + str(errors) + "\nError Sum:\n" + str(errorSum) + "\n")

# not printed
y = np.round(sbz2)
# Err1 = np.multiply(np.multiply((out - target),(np.multiply(out, (1-out)))),sbz1)
# print("Err1:\n" + str(Err1) + "\n")
# print(-Err1 * alpha + w2[0])


dErrdOut = (out - target)
print("dErr/dOut:\n" + str(dErrdOut) + "\n")
dOutdNet = np.multiply(out, (1 - out))
print("dOut/dNet:\n" + str(dOutdNet) + "\n")
dNetdW = sbz1
print("dNet/dW:\n" + str(dNetdW) + "\n")

# E = np.array([[0.082167041, -0.022602540],[0.082667628, -0.032274024]])
E = np.rot90(dNetdW, -1) * reduce(np.multiply, [dErrdOut, dOutdNet])
print("Error:\n" + str(E) + "\n")
updatedW2 = w2 - alpha * E
print("Updated values:\n" + str(updatedW2) + "\n")
# w5 =  0.082167041
# w6 =  0.082667628
# w7 = -0.022602540
# w8 = -0.032274024

dNetdOut_h = w2

dErrdNet_h = np.multiply(dErrdOut, dOutdNet)
print("dErr/dOut_h:\n"+str(dErrdNet_h)+"\n")

dErrdOut_h = np.multiply(dNetdOut_h, dErrdNet_h)
print("dErr/dOut:\n"+str(dErrdOut_h)+"\n")

dETotaldOut_h = np.asmatrix(np.sum(dErrdOut_h,axis=1).tolist())
print("dETotal/dOut_h:\n"+str(dETotaldOut_h)+"\n")
#print("thingy:" + str([dErrdOut_h, dOutdNet_h, I])+"\n")

dOutdNet_h1 = np.multiply(sbz1, 1 - sbz1)
print("dOut/dNet_h1:\n"+str(dOutdNet_h1)+"\n")

try:
    print([x.shape for x in [dOutdNet_h1, dETotaldOut_h, I]])
    E2 = reduce(np.multiply, [dOutdNet_h1, dETotaldOut_h, I])
except:
    E2 = np.zeros(w1.shape)
print("dErr/dw1:\n", str(E2), "\n")
updatedW1 = w1 - alpha * E2
print("w1':\n"+str(updatedW1)+"\n")




root = tkinter.Tk()
frame = tkinter.Frame(root)
frame.pack(fill=tkinter.BOTH, expand=tkinter.YES)
canvas = ResizeCanvas(frame, width=1200, height=800, bg="white smoke", highlightthickness=0)
canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)

canvas.create_text(100,10,text="alpha:%.5f"%alpha)

layerList = [(I, 0), (sbz1, b1, w1, updatedW1), (sbz2, b2, w2, updatedW2)]
xPad = canvas.winfo_reqwidth() / len(layerList)
startLayer, endLayer = [], []
for layer in range(len(layerList)):
    gap = 1 / (layerList[layer][0].shape[1] * 4) * canvas.winfo_reqheight()
    oval = 1 / (layerList[layer][0].shape[1] * 2) * canvas.winfo_reqheight()
    print("Image gap:", gap, " Image oval size:", oval, " for layer:", layer)

    endLayer = []
    for i in range(layerList[layer][0].shape[1]):
        canvas.create_oval(10 + layer * xPad, gap + i * (gap + oval), 110 + layer * xPad, gap + oval + i * (gap + oval),
                           fill="green")
        endLayer.append((60 + layer * xPad, (i + 1) * gap + (i + .5) * oval))
        canvas.create_text(60 + layer * xPad, i * (gap + oval) + oval,
                           text="I%d\nBias: %.3f" % (i, layerList[layer][1]))
        canvas.create_text(60 + layer * xPad, (i + 1) * (gap + oval) + 20,
                           text="%s:\n%.5f" % ("Sigmoid Output" if layer >= 1 else
                                               "Input", layerList[layer][0].item(i)), justify="center")
    if startLayer:
        print("Circle center:", startLayer)
        comb = list(itertools.product(startLayer, endLayer))
        text = []
        for i in range(len(comb)):
            center = ((comb[i][0][0] + comb[i][1][0]) / 2, (comb[i][0][1] + comb[i][1][1]) / 2 - 40)
            padding = text.count(center) * 80

            fillColor = ["coral","RoyalBlue1","OliveDrab4","dark slate blue", "goldenrod"][i%len(endLayer)]
            canvas.create_line(*comb[i], tags="line", fill=fillColor)
            canvas.create_text(center[0], center[1] + padding, text="w%d: %.5f" % (i, layerList[layer][2].item(i)),
                               fill=fillColor)

            if layer >= 1:
                canvas.create_text(center[0], center[1]+padding+20, text="w%d': %.5f" % (i, layerList[layer][3].item(i)),
                             fill="red")
            text.append(center)

    startLayer = endLayer

for i in range(len(startLayer)):
    x, y = startLayer[i]
    canvas.create_line(x, y, x + xPad - 100, y, tags="line", arrow="last")
    canvas.create_text(x + (xPad / 2) - 5, y - 40, text="Out: %.5f\nExpected: %.5f" %
                                                        (out.item(i), target.item(i)), justify="right")

    canvas.create_line(x + 50, y + 30, x + xPad - 100, y + 30, tags="line", arrow="first")
    canvas.create_text(x + xPad / 2, y + 70, text="Error: %.5f\ndErr/dOut: %.5f\ndOut/dNet: %.5f\ndNet/dW: %.5f" %
                                                  (errors.item(i),
                                                   dErrdOut.item(i),
                                                   dOutdNet.item(i),
                                                   dNetdW.item(i)), justify="right")

canvas.create_text(canvas.winfo_reqwidth() - 100, canvas.winfo_reqheight() - 30, text="Error Sum: %.5f" % errorSum)
canvas.tag_lower("line")
canvas.addtag_all("all")
root.mainloop()
