#PriorityQueue
#encoding:utf-8
from queue import PriorityQueue

#创建优先级队列
pq = PriorityQueue()

#向队列添加数据,并打乱顺序
pq.put("test_queue_05",)
pq.put("test_queue_01")
pq.put("test_queue_04")
pq.put("test_queue_03")
pq.put("test_queue_02")


#获取队列的大小
print("获取队列的大小：",pq.qsize())

#循环获取队列的值
for i in range(pq.qsize()):
    print("循环打印优先级队列值：",pq.get())
