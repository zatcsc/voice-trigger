from norm import ArgumentsError
from norm import Norm
import numpy as np
class GMM:
	def __init__(self,n,weights,gaussian_components):
		self.n = n
		if self.n != weights.shape[0] or self.n != gaussian_components.shape[0]:
			raise ArgumentsError("The array length shoud be consistent")
		if np.sum(weights) != 1 :
			raise ArgumentsError("Sum of components' weight must be 1")
		if not isinstance(gaussian_components[0],Norm):
			raise ArgumentsError("Gaussian components should be instance of Norm class")
		self.weights = weights
		self.gaussian_components = gaussian_components
	def prob(self,x):
		x = np.array(x);
		if len(x.shape) != 1:
			raise ArgumentsError("Invalid input: input should be %s-dimensional vecotr",self.n)
		prob = 0;
		for i in range(self.n):
			prob = prob + self.weights[i]*self.gaussian_components[i].prob(x)
		print prob
		return prob


a = GMM(3,np.array([0.3,0.25,0.45]),np.array([Norm(np.array([1.05432,1.3432432]),np.array([0.8,0.5]),"diag"), Norm(np.array([1.05432,1.3432432]),np.array([0.8,0.5]),"diag"), Norm(np.array([1.05432,1.3432432]),np.array([0.8,0.5]),"diag")]))
a.prob([2,2]);

