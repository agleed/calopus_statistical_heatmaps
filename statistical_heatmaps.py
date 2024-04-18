import pickle
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # open probabilities and standard deviations
    fread = open('probabilities.pkl', 'rb')
    probabilities = pickle.load(fread)
    fread = open('stds.pkl', 'rb')
    stds = pickle.load(fread)

    x = np.linspace(0, 1, num=100)

    # take A/cephalic, head = step 1, cephalic presentation, fetal head
    data = probabilities['A/cephalic']['head']
    errors = stds['A/cephalic']['head']

    # generate line plot with error bars
    fig, ax = plt.subplots()
    ax.set_yticklabels([])
    ax.set_yticks([])
    ax.set_xticklabels([])
    ax.set_xticks([])

    # line plot with error bars
    ax.errorbar(x, data, linewidth=2.5, color='red', yerr=errors, ecolor='blue', elinewidth=1, errorevery=5)

    # set y range between 0 and 1
    ax.set_ylim([0, 1])

    # annotate maximum on line plot
    y = np.asarray(data)
    xmax = x[np.argmax(y)]
    ymax = y.max()
    ax.annotate('(' + str(round(ymax, 2)) + ',' + str(round(xmax, 2)) + ')', (xmax, ymax-0.015), fontsize=18) # text +0.1 for all steps except step E
    ax.plot(xmax, ymax, 'rx', mew=1, ms=12) # red cross

    # x-axis title
    ax.set_title('Cephalic', y=1.08, fontsize=18)

    # (last) x-axis label
    ax.set_xticks([0, 0.25, 0.50, 0.75, 0.99])
    ax.set_xticklabels(['0', '25', '50', '75', '100'])
    ax.set_xlabel('% of video sweep', fontsize=18)

    # y-axis label
    ax.set_yticks([0, 0.25, 0.50, 0.75, 0.99])
    ax.set_yticklabels(['0', '0.25', '0.50', '0.75', '1'])
    ax.set_ylabel('Head', fontsize=18)

    
    # generate single heatmap
    fig2, ax2 = plt.subplots()
    data = np.resize(data, (1,len(data)))
    im = ax2.imshow(data, aspect='auto', cmap='viridis', interpolation='nearest', vmin=0, vmax=0.7)

    # remove tick labels and marks
    ax2.set_yticklabels([])
    ax2.set_xticklabels([])
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    fig2.subplots_adjust(right=0.8) # otherwise colorbar is pasted on top of plots
    cbar_ax = fig2.add_axes([0.85, 0.15, 0.05, 0.7])
    fig2.colorbar(im, cax=cbar_ax)

    # x-axis title
    ax2.set_title('Cephalic', y=1.08, fontsize=18)

    # (last) x-axis label
    ax2.set_xticks([0, 25, 50, 75, 99])
    ax2.set_xticklabels(['0', '25', '50', '75', '100'])
    ax2.set_xlabel('% of video sweep', fontsize=18)

    # y-axis label
    ax2.set_ylabel('Head', fontsize=18)

    plt.show()

