import numpy as np
import scipy.stats as st
class Error(Exception):
	""" Base class for exceptions in this module"""
	pass
class ArgumentsError(Error):
	""" Exception raised for errors in arguments of Normal Distribution.
	Attributes"
		message -- explanation of the error
	"""
	def __init__(self, message):
		self.message = message;
		print self.message
class Norm:
	'Normal Distribution(mean,cov,cov_type)'
	cov_type = "diag"
	def __init__(self,mean,cov,cov_type):
		self.mean = mean
		self.dimen = self.mean.shape[0]
		self.cov_type = cov_type

		if self.dimen != cov.shape[0]:
			raise ArgumentsError("The dimension of mean and covariance must be consistent.")
		if cov_type != "diag":
			raise ArgumentsError("Covariance type '%s' is currently not supported" % cov_type)

		self.cov_2d = np.diag(cov,k = 0)
		self.i_cov_2d = np.diag(np.divide(1,cov),k=0);
		self.cov_det = np.prod(cov);
		self.left_hand = np.power(2*np.pi,-self.dimen/2)*np.power(np.absolute(self.cov_det),-0.5)
		

	def prob(self,x):
		if len(x.shape) != 1:
			raise ArgumentsError("The x input must be a n-dimentional vecor")
		if x.shape[0] != self.dimen:
			raise ArgumentsError("The input vector is not dimensionally incompatibale")
		
		diff = np.subtract(x,self.mean)
		diffT = diff.transpose()
		exponent = diffT.dot(self.i_cov_2d).dot(diff)*-0.5
		right_hand = np.exp(exponent)
		return self.left_hand*right_hand

# a = Norm(np.array([1.05432,1.3432432]),np.array([0.8,0.5]),"diag")
# print a.prob(np.array([1,1.3]));
# mean = [1.05432,1.3432432]
# cov = [[0.8, 0],[0, 0.5]]
# print st.multivariate_normal.pdf([1,1.3],mean,cov)
