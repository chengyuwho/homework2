# queue 佇列（FIFO）
#encoding:utf-8
from queue import Queue

#创建队列
q = Queue()

#向队列添加数据
q.put("test_queue_01")
q.put("test_queue_02")
q.put("test_queue_03")
q.put("test_queue_04")
q.put("test_queue_05")

#获取队列的值
print("队列的值：",q.get())

#获取队列的大小
print("获取队列的大小：",q.qsize())

#循环获取队列的值
for i in range(q.qsize()):
    print("循环打印队列值：",q.get())
