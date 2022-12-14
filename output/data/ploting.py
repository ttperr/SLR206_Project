import matplotlib.pyplot as plt
import pandas as pd

coarse = pd.read_csv('CoarseGrainedListBasedSet_data.csv')
hOh = pd.read_csv('HandOverHandListBasedSet_data.csv')
lazy = pd.read_csv('LazyLinkedListSortedSet_data.csv')

# Three plots (one per algorithm), with three curves each, for a fixed update ratio 10% and varying list size.

# Plot 1: Coarse Grained

plt.figure()
plt.plot(coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 100)]['threads'], coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 100)]['throughput'], 'r')
plt.plot(coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 1000)]['threads'], coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 1000)]['throughput'], 'g')
plt.plot(coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 10000)]['threads'], coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 10000)]['throughput'], 'b')
plt.xlabel('Threads')
plt.ylabel('Throughput (ops/s)')
plt.title('Performance of the Coarse Grained Algorithm with u = 10%')
plt.semilogy()
plt.grid(True, which="both")
plt.legend(['list size = 100', 'list size = 1000', 'list size = 10000'])
plt.savefig("CoarseGrained_u=10.png", dpi = 600)



# Plot 2: Hand Over Hand

plt.figure()
plt.plot(hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 100)]['threads'], hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 100)]['throughput'], 'r')
plt.plot(hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 1000)]['threads'], hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 1000)]['throughput'], 'g')
plt.plot(hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 10000)]['threads'], hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 10000)]['throughput'], 'b')
plt.xlabel('Threads')
plt.ylabel('Throughput (ops/s)')
plt.title('Performance of the Hand Over Hand Algorithm with u = 10%')
plt.semilogy()
plt.grid(True, which="both")
plt.legend(['list size = 100', 'list size = 1000', 'list size = 10000'])
plt.savefig("HandOverHand_u=10.png", dpi = 600)


# Plot 3: Lazy

plt.figure()
plt.plot(lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 100)]['threads'], lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 100)]['throughput'], 'r')
plt.plot(lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 1000)]['threads'], lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 1000)]['throughput'], 'g')
plt.plot(lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 10000)]['threads'], lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 10000)]['throughput'], 'b')
plt.xlabel('Threads')
plt.ylabel('Throughput (ops/s)')
plt.title('Performance of the Lazy Algorithm with u = 10%')
plt.semilogy()
plt.grid(True, which="both")
plt.legend(['list size = 100', 'list size = 1000', 'list size = 10000'])
plt.savefig("Lazy_u=10.png", dpi = 600)

# Three plots (one per algorithm), with three curves each, for a fixed list size 100 and varying update ratios.

# Plot 1: Coarse Grained

plt.figure()
plt.plot(coarse.loc[(coarse['uratio'] == 0) & (coarse['lsize'] == 100)]['threads'], coarse.loc[(coarse['uratio'] == 0) & (coarse['lsize'] == 100)]['throughput'], 'r')
plt.plot(coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 100)]['threads'], coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 100)]['throughput'], 'g')
plt.plot(coarse.loc[(coarse['uratio'] == 100) & (coarse['lsize'] == 100)]['threads'], coarse.loc[(coarse['uratio'] == 100) & (coarse['lsize'] == 100)]['throughput'], 'b')
plt.xlabel('Threads')
plt.ylabel('Throughput (ops/s)')
plt.title('Performance of the Coarse Grained Algorithm\nwith list size = 100')
plt.grid(True, which="both")
plt.legend(['u = 0%', 'u = 10%', 'u = 100%'])
plt.savefig("CoarseGrained_lsize=100.png", dpi = 600)

# Plot 2: Hand Over Hand

plt.figure()
plt.plot(hOh.loc[(hOh['uratio'] == 0) & (hOh['lsize'] == 100)]['threads'], hOh.loc[(hOh['uratio'] == 0) & (hOh['lsize'] == 100)]['throughput'], 'r')
plt.plot(hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 100)]['threads'], hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 100)]['throughput'], 'g')
plt.plot(hOh.loc[(hOh['uratio'] == 100) & (hOh['lsize'] == 100)]['threads'], hOh.loc[(hOh['uratio'] == 100) & (hOh['lsize'] == 100)]['throughput'], 'b')
plt.xlabel('Threads')
plt.ylabel('Throughput (ops/s)')
plt.title('Performance of the Hand Over Hand Algorithm\nwith list size = 100')
plt.grid(True, which="both")
plt.legend(['u = 0%', 'u = 10%', 'u = 100%'])
plt.savefig("HandOverHand_lsize=100.png", dpi = 600)

# Plot 3: Lazy

plt.figure()
plt.plot(lazy.loc[(lazy['uratio'] == 0) & (lazy['lsize'] == 100)]['threads'], lazy.loc[(lazy['uratio'] == 0) & (lazy['lsize'] == 100)]['throughput'], 'r')
plt.plot(lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 100)]['threads'], lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 100)]['throughput'], 'g')
plt.plot(lazy.loc[(lazy['uratio'] == 100) & (lazy['lsize'] == 100)]['threads'], lazy.loc[(lazy['uratio'] == 100) & (lazy['lsize'] == 100)]['throughput'], 'b')
plt.xlabel('Threads')
plt.ylabel('Throughput (ops/s)')
plt.title('Performance of the Lazy Algorithm\nwith list size = 100')
plt.grid(True, which="both")
plt.legend(['u = 0%', 'u = 10%', 'u = 100%'])
plt.savefig("Lazy_lsize=100.png", dpi = 600)

# One plot, with three curves (one per algorithm), with fixed update ratio 10% and list size 1000.

plt.figure()
plt.plot(coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 1000)]['threads'], coarse.loc[(coarse['uratio'] == 10) & (coarse['lsize'] == 1000)]['throughput'], 'r')
plt.plot(hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 1000)]['threads'], hOh.loc[(hOh['uratio'] == 10) & (hOh['lsize'] == 1000)]['throughput'], 'g')
plt.plot(lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 1000)]['threads'], lazy.loc[(lazy['uratio'] == 10) & (lazy['lsize'] == 1000)]['throughput'], 'b')
plt.xlabel('Threads')
plt.ylabel('Throughput (ops/s)')
plt.title('Comparing performance of all three algorithms\nwith update ratio u = 10% and list size = 1000')
plt.grid(True, which="both")
plt.semilogy()
plt.legend(['Coarse grained', 'Hand Over Hand', 'Lazy'])
plt.savefig('AllAlgorithms_u=10_lsize=1000.png', dpi = 600)