import matplotlib.pyplot as plt
from IPython import display
import matplotlib
matplotlib.use('TkAgg')

_fig, _ax = plt.subplots() 
plt.ion()

def plot(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(_fig)
    _ax.clear()
    _ax.set_title('Training...')
    _ax.set_xlabel('Number of Games')
    _ax.set_ylabel('Score')
    _ax.plot(scores, label='Score')
    _ax.plot(mean_scores, label='Mean Score')
    _ax.set_ylim(ymin=0)
    if len(scores) > 0:
        _ax.text(len(scores)-1, scores[-1], str(scores[-1]))
    if len(mean_scores) > 0:
        _ax.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    _ax.legend()
    plt.show(block=False)
    plt.pause(0.1)