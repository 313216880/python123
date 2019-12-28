'''

Description:
@author: LiuHao
@date 2019年12月9日 下午2:59:38
'''
import smtplib
from email.mime.text import MIMEText

class Sendmail(object):

    def __init__(self, mailHost, mailUser, mailPwd):

        self.mailHost = mailHost;
        self.mailUser = mailUser;
        self.mailPwd = mailPwd;
        self.sendList = [];

#function subject->title
    def setMailInfo(self, sendList,subject, content):
        self.sendList = sendList
        self.content = content;#内容
        self.subject = subject;
        self.msg = MIMEText(self.content)
        self.msg['From'] = self.mailUser #发送者
        self.msg['Subject'] = self.subject #发送主题
        self.msg['To'] = ";".join(self.sendList) #接收者
    def result(self,state,msg):
        result = {}
        result['state'] = state
        result['msg'] = msg
        return result
        
    def sendEmail(self):
        try:
            self.send = smtplib.SMTP()
            self.send.connect(self.mailHost)
            self.send.login(self.mailUser, self.mailPwd)
            self.send.sendmail(self.mailUser, self.sendList, self.msg.as_string())
            return self.result(1,'[*]-----send mail---to' + str(self.sendList) + 'success-----[*]')
        except smtplib.SMTPException as e:
            return self.result(0,e)
#             print (e)
# p = Sendmail('smtp.163.com', '18310876832@163.com', 'll616923')
# p.setMailInfo(['18310876832@163.com','313216880@qq.com'], 'Python SMTP 邮件测试', 'Python 邮件发送测试...')
# print (p.sendEmail())