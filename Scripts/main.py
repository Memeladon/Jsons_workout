from parse import Parse
from clustering import Clustering
import csv

info = Parse('../Jsons')
data = info.read_mining()
cluster = Clustering(data)
cluster.partitioning_into_clusters()
