import receipt
import math
def reward_receipt( when_receipt , receiptnum ):
    reward_list=receipt.rtmonth(when_receipt)
    for i in range(len(reward_list)):
        reward_list[i]=int(reward_list[i])
    receiptnum=int(receiptnum)
    if receiptnum==reward_list[0]:
        return 10000000
    if receiptnum==reward_list[1]:
        return 2000000
    for i in range(2,5):
        if receiptnum==reward_list[i]:
            return 200000
        if receiptnum%pow(10,7)==reward_list[i]%pow(10,7):
            return 40000
        if receiptnum%pow(10,6)==reward_list[i]%pow(10,6):
            return 10000
        if receiptnum%pow(10,5)==reward_list[i]%pow(10,5):
            return 4000
        if receiptnum%pow(10,4)==reward_list[i]%pow(10,4):
            return 1000
        if receiptnum%pow(10,3)==reward_list[i]%pow(10,3):
            return 200
    for i in range(5,len(reward_list)):
        if receiptnum%pow(10,3)==reward_list[i]:
            return 200
    return 0

