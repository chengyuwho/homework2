#LifoQueue
#encoding:utf-8
from queue import LifoQueue

#创建后进先出队列
lq = LifoQueue()

#向队列添加数据
lq.put("test_queue_01")
lq.put("test_queue_02")
lq.put("test_queue_03")
lq.put("test_queue_04")
lq.put("test_queue_05")

#获取队列的值
print("后进先出队列的值：",lq.get())

#获取队列的大小
print("获取队列的大小：",lq.qsize())

#循环获取队列的值
for i in range(lq.qsize()):
    print("循环打印后进先出队列值：",lq.get())
