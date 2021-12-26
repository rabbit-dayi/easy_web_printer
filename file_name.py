import time
import random
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y.%m.%d.%H.%M.%S", time.localtime())+str(random.randint(1,233333)))
