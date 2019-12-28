# -*- coding: UTF-8 -*-
from com.SendEmailUtil import Sendmail
p = Sendmail('smtp.163.com', '18310876832@163.com', 'll616923')
p.setMailInfo(['18310876832@163.com','313216880@qq.com'], 'Python SMTP 邮件测试', 'Python 邮件发送测试...')
print (p.sendEmail())