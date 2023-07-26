import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


class Clustering:
    def __init__(self, info):
        self.data = info

    def partitioning_into_clusters(self):
        numeric_data = np.zeros((len(self.data), len(self.data[0])))

        for i, item in enumerate(self.data):
            for j, key in enumerate(item):
                try:
                    numeric_data[i][j] = float(item[key])
                except ValueError:
                    continue

        kmeans = KMeans(n_clusters=3)
        kmeans.fit(numeric_data)
        labels = kmeans.labels_

        self.plot_clusters(numeric_data, labels)

        # """
        # for i in range(3):
        #     cluster_data = [numeric_data[j] for j in range(len(numeric_data)) if labels[j] == i]
        #     cluster_data = list(zip(*cluster_data))
        #     plt.scatter(cluster_data[0], cluster_data[1])
        #     plt.xlabel('Data Point Index')
        #     plt.ylabel('Data')
        #     plt.title('Cluster ' + str(i))
        #     plt.colorbar(label='Latency (ms)')
        #     plt.show()
        # """

    @staticmethod
    def plot_clusters(numeric_data, labels):
        plt.scatter(numeric_data[:, 0], numeric_data[:, 1], c=labels, cmap='viridis')
        plt.xlabel('Latency')
        plt.ylabel('Data Point Index')
        plt.colorbar(label='Latency (ms)')
        plt.show()

