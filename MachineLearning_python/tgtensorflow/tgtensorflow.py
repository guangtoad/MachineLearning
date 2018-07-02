
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
class tgtensorflow(object):
	"""docstring for ClassName"""
	data_mnist = 0
	def __init__(self):
		print('tgtensorflow init')
		self._name = '1'
		pass
	def readmnist(self):
		print('read mnist for MNIST_data/')
		self.data_mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
		return self.data_mnist
	def infomnist(self):
		# 查看训练数据的大小
		print(self.data_mnist.train.images.shape)  # (55000, 784)
		print(self.data_mnist.train.labels.shape)  # (55000, 10)

		# 查看验证数据的大小
		print(self.data_mnist.validation.images.shape)  # (5000, 784)
		print(self.data_mnist.validation.labels.shape)  # (5000, 10)

		# 查看测试数据的大小
		print(self.data_mnist.test.images.shape)  # (10000, 784)
		print(self.data_mnist.test.labels.shape)  # (10000, 10)
		pass
	def getmnist(self):
		if self.data_mnist == 0:
			self.readmnist()
		# 	pass
		return self.data_mnist
		pass
def main():
	print('test tensorflow')
	# selectIndex = input('选择')
	print(selectIdex)
	pass
if __name__ == '__main__':
	main()