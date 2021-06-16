import time
import multiprocessing


def job(x, y):
	"""
	:param x:
	:param y:
	:return:
	"""
	return x*y*x*y*x*y*x

def parallel(z):
	"""
    处理多参数传参问题（实际上把参数写成元组，在job函数内再拆成
     x, y = param 也一样
	:param z:
	:return:
	"""
	return job(z[0], z[1])


if __name__ == "__main__":
	time1 = time.time()

	pool = multiprocessing.Pool(2) # 参数缺省的话就是cpu全员上阵

	# 把本来要写成循环的参数, 做成一个list
	data_list=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]

	# 重点就只有下面这一行！！！
	# 用map函数代替循环
	res = pool.map(parallel, data_list)
	time2=time.time()

	print(res)

	pool.close()
	pool.join()

	print('总耗时：' + str(time2 - time1) + 's')