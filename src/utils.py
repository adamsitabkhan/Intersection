import numpy as np
import numpy.random as rand

def generate_convex_polygon(n=6):
    if n < 3:
        return None
    
    # Generate and sort random X and Y coordinates
    x, y = np.sort(rand.uniform(low=0, high=1, size=(2,n)), axis=1) 
    
    # Isolate the extreme points
    xext, yext = (x[0], x[-1]), (y[0], y[-1]) 
    
    # Randomly divide interior points into two chains
    xint, yint = x[1:-1], y[1:-1]
    rand.shuffle(xint)
    rand.shuffle(yint)
    xint1, xint2 = np.sort(xint[:int((n-1)/2)]), np.sort(xint[int((n-1)/2):]) 
    yint1, yint2 = np.sort(yint[:int((n-1)/2)]), np.sort(yint[int((n-1)/2):])
    xchain1 = np.insert(np.append(xint1, xext[1]), 0, xext[0])
    xchain2 = np.insert(np.append(xint2, xext[1]), 0, xext[0])
    ychain1 = np.insert(np.append(yint1, yext[1]), 0, yext[0])
    ychain2 = np.insert(np.append(yint2, yext[1]), 0, yext[0])
    
    # Extract vector components
    sign = rand.choice([-1,1], 2)
    xcomps = np.concatenate((sign[0]*np.diff(xchain1), -sign[0]*np.diff(xchain2)))
    ycomps = np.concatenate((sign[1]*np.diff(ychain1), -sign[1]*np.diff(ychain2)))
    
    # Randomly combine the x- and Y-components into vectors
    rand.shuffle(xcomps)
    rand.shuffle(ycomps)
    vecs = np.array([ycomps, xcomps])
    angles = np.where(np.arctan2(*vecs) < 0, np.arctan2(*vecs) + 2*np.pi, np.arctan2(*vecs))

    # Lay vectors end to end to create polygon vertices
    points = np.cumsum(vecs[:,np.argsort(angles)], axis=1)[[1,0]]
    points = points.T - np.min(points, axis=1) + np.array([xext[0], yext[0]])
    
    return points


def make_polygon_isotropic(points, sd=0.25):
    from sklearn.decomposition import PCA
    
    pca = PCA(n_components=2)
    points_centered = points - np.mean(points, axis=0)
    pca.fit(points_centered)

    transformed_points = pca.transform(points_centered)
    variance = np.var(transformed_points, axis=0)  # Variance along each principal component
    scaling_factors = sd / np.sqrt(variance)  # Scale to unit variance
    transformed_points_scaled = transformed_points * scaling_factors

    rescaled_points = pca.inverse_transform(transformed_points_scaled) + np.mean(points, axis=0)
    return rescaled_points


def center_polygon(points):
    mid = (np.max(points, axis=0) + np.min(points, axis=0))/2
    return points - mid + np.array([0.5, 0.5])


def transform_polygon(points):
    return center_polygon(make_polygon_isotropic(points))