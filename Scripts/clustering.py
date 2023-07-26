import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


class Clustering:
    def __init__(self, info):
        self.data = info

    def partitioning_into_clusters(self):
        numeric_data = np.zeros((len(self.data), len(self.data[0])))

        kmeans = KMeans(n_clusters=3)
        kmeans.fit(numeric_data)
        labels = kmeans.labels_

        plt.scatter(numeric_data[:, 0], numeric_data[:, 1], c=labels)
        plt.xlabel('Feature 1')
        plt.ylabel('Feature 2')
        plt.show()

        """
        numeric_data = np.array([[r['Aborted_clients'], r['Latency']] for r in self.data])
        kmeans = KMeans(n_clusters=3)
        kmeans.fit(numeric_data)
        labels = kmeans.labels_

        for i in range(3):
            cluster_data = [numeric_data[j] for j in range(len(numeric_data)) if labels[j] == i]
            cluster_data = list(zip(*cluster_data))
            plt.scatter(cluster_data[0], cluster_data[1])
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title('Cluster ' + str(i))
            plt.show()
        """