## 暑修資料結構11124228 期末報告第六題
## python queue 陣列（先進先出）、LifoQueue（後進先出）、PriorityQueue（優先及陣列）
# queue 陣列（FIFO）
FIFO 全稱是First Input First Output（先進先出），先進先出簡言之就是在獲取佇列的數據時，優先取佇列前面的數據。
Queue模組中的常用方法：

- Queue.qsize（） 傳回佇列的大小

* Queue.empty（） 如果隊列為空，返回True，反之False

+ Queue.full（） 如果佇列滿了，返回True，反之False

- Queue.full 與 maxsize 大小對應

* Queue.get（[block[， timeout]]）獲取佇列，timeout等待時間

+ Queue.get_nowait（） 相當Queue.get（False）

- Queue.put（item， block=True， timeout=None） 寫入佇列，timeout等待時間

* Queue.put_nowait（item） 相當 Queue.put（item， False）

+ Queue.task_done（） 在完成一項工作之後，Queue.task_done（）函數向任務已經完成的佇列發送一個信號

- Queue.join（） 實際上意味著等到隊列為空，再執行別的操作

導入queue模組的Queue類
```
from queue import Queue
```
創建佇列
```
#创建队列
q = Queue()
```
向佇列添加數據
```
#向队列添加数据
q.put("test_queue_01")
q.put("test_queue_02")
q.put("test_queue_03")
q.put("test_queue_04")
q.put("test_queue_05")
```
獲取佇列的值
```
#获取队列的值
print（“佇列的值：”，q.get（））
```
獲取佇列的大小
```
#获取队列的大小
print("获取队列的大小：",q.qsize())
```
迴圈獲取佇列的值
```
#循环获取队列的值
for i in range(q.qsize()):
    print("循环打印队列值：",q.get())
```
結果
![01]()
# LifoQueue（LIFO）
導入queue模組的Queue類
```
from queue import LifoQueue
```
創建後進先出佇列
```
#创建后进先出队列
lq = LifoQueue()
```
向佇列添加數據
```
#向队列添加数据
lq.put("test_queue_01")
lq.put("test_queue_02")
lq.put("test_queue_03")
lq.put("test_queue_04")
lq.put("test_queue_05")
```
獲取佇列的值
```
#获取队列的值
print("后进先出队列的值：",lq.get())
```
獲取佇列的大小
```
#获取队列的大小
print("获取队列的大小：",lq.qsize())
```
迴圈獲取佇列的值
```
#循环获取队列的值
for i in range(lq.qsize()):
    print("循环打印后进先出队列值：",lq.get())
```
結果
![01]()
# PriorityQueue
數據越小優先順序越高，也就是數據越小優先獲取到
創建優先順序佇列
```
#创建优先级队列
pq = PriorityQueue()
```
向佇列添加數據，並打亂順序
```
#向队列添加数据,并打乱顺序
pq.put("test_queue_05",)
pq.put("test_queue_01")
pq.put("test_queue_04")
pq.put("test_queue_03")
pq.put("test_queue_02")
```
獲取佇列的大小
```
#获取队列的大小
print("获取队列的大小：",pq.qsize())
```
迴圈獲取佇列的值
```
#循环获取队列的值
for i in range(pq.qsize()):
    print("循环打印优先级队列值：",pq.get())
```
結果
![01]()
