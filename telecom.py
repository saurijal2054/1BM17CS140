class CallDetail:
    def __init__(self,l1,l2,l3,l4):
        self.callingNo = l1
        self.calledNo = l2
        self.duration = l3
        self.typeCall = l4
    def print1(self):
        print(self.callingNo,' ',self.calledNo, ' ',self.duration, ' ' ,self.typeCall)

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):

        list1 = []
        for i in range(len(list_of_call_string)):
            list1 = list_of_call_string[i].split(",")
            callingNo = list1[0]
            calledNo = list1[1]
            duration = list1[2]
            typeCall = list1[3]
            c1 = CallDetail(callingNo,calledNo,duration,typeCall)
            c1.print1()

call1='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD' 
 
list_of_call_string=[call1,call2,call3]
Util().parse_customer(list_of_call_string) 
 
