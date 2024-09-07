import numpy as np
import matplotlib.pyplot as plt


def preset_barplot(data, labels, img_name):
    
    colors = plt.get_cmap('winter')(np.linspace(0.2, 0.7, len(data)))
    plt.bar(range(len(data)), data, tick_label=labels, color=colors)
    
    plt.tick_params(
        axis='y',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        left=False,      # ticks along the bottom edge are off
        right=False,
        labelleft=False) # labels along the bottom edge are off
    
    for i in range(len(data)):
        plt.text(i, data[i]//2, data[i], ha='center', fontsize='large', color='white')
    plt.grid(axis="y", zorder=0)
    ax = plt.gca()
    ax.set_axisbelow(True)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.savefig(img_name, dpi=120, bbox_inches='tight')


def preset_pie(data, labels, img_name):
    colors = plt.get_cmap('winter')(np.linspace(0.2, 0.7, len(data)))
    plt.pie(data, labels=labels, colors=colors, wedgeprops=dict(width=0.3, edgecolor='w'))
    
    plt.savefig(img_name, dpi=120, bbox_inches='tight')


def preset_plot(data, img_name):
    colors = plt.get_cmap('winter')(np.linspace(0.2, 0.7, len(data)))
    
    plt.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,
        labelbottom=False) # labels along the bottom edge are off
    
    ax = plt.gca()
    
    max_tick = max(data)*1.4
    major_ticks = np.arange(0, max_tick, 10)
    ax.set_yticks(major_ticks)
    ax.grid(axis="y", zorder=0)
    ax.set_axisbelow(True)
    
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    
    plt.plot(range(len(data)), data, color=colors[0], marker='o', markersize=8, markeredgecolor='k')
    for i in range(len(data)):
        plt.axvline(i, ymax=float(data[i])/max_tick, color='b')
    plt.gca().fill_between(range(len(data)), data, color=colors[0], alpha=0.5)
    plt.ylim(0, max_tick)
    plt.savefig(img_name, dpi=120, bbox_inches='tight')