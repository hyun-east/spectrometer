import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv("results_log.csv")

plt.plot(df['WaveLength'], df['r005none'], label='r005none')
plt.plot(df['WaveLength'], df['y005none'], label='y005none')
plt.plot(df['WaveLength'], df['y005small'], label='y005small')

plt.legend()
plt.show()