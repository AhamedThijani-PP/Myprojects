import numpy as np
import math
input_dim=2
map_size=(5,5)
learning_rate=0.5
sigma=max(map_size)/2
num_iteration=1000
def initialize_weights(map_size,input_dim):
    return np.random.rand(map_size[0],map_size[1],input_dim)
def euclidean_distance(vec1,vec2):
    return np.linalg.norm(vec1-vec2)
def find_bmu(weights,input_vector):
    min_dist=float('inf')
    bmu_idx=(0,0)
    for i in range(weights.shape[0]):
        for j in range(weights.shape[1]):
            dist=euclidean_distance(weights[i,j],input_vector)
            if dist<min_dist:
                min_dist=dist
                bmu_idx=(i,j)
    return bmu_idx
def update_weights(weights,input_vector,bmu_idx,iteration,num_iterations,learning_rate,sigma):
    lr=learning_rate*(1-iteration/num_iterations)
    sig=sigma*(1-iteration/num_iterations)
    for i in range(weights.shape[0]):
        for j in range(weights.shape[1]):
            dist_to_bmu=euclidean_distance(np.array([i,j]),np.array(bmu_idx))
            influence=math.exp(-dist_to_bmu**2/(2*sig**2)) if sig > 0 else 0
            weights[i,j]+=lr*influence*(input_vector-weights[i,j])
np.random.seed(42)
data=np.random.rand(100,input_dim)
weights=initialize_weights(map_size,input_dim)
for iteration in range(num_iteration):
    input_vector=data[np.random.randint(0,len(data))]
    bmu_idx=find_bmu(weights,input_vector)
    update_weights(weights,input_vector,bmu_idx,iteration,num_iteration,learning_rate,sigma)
print("Training Complete. Final weight matrix:")
print(weights)