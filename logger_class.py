class Logger:

    def __init__(self):

        self.msg_dict = {}


    def shouldPrintMessage(self, timestamp, msg):
        if msg not in self.msg_dict:
            self.msg_dict[msg]=timestamp
            return True
        elif timestamp-self.msg_dict[msg] >=10:
            self.msg_dict[msg]=timestamp
            return True
        else:
            return False


loggerObject = Logger()
print(loggerObject.shouldPrintMessage(0,'Sigmoid'))
print(loggerObject.shouldPrintMessage(9,'Sigmoid'))
print(loggerObject.shouldPrintMessage(12,'Sigmoid'))