import smtplib
from email.mime.text import MIMEText
# ---------- 1.跟发件相关的参数 ------------------
smtpserver = "smtp.sina.cn"
port = 25
sender = "zhongdd007@sina.com"
psw = "5201314025zdd"
receiver = "841370939@qq.com"
# ---------- 2. 编辑邮件的内容 --------------------
file_path = ""
subject = "这个是主题"
body = '<p> 这个是发送的 163 邮件 </p>' # 定义邮件正文为 html 格式
msg = MIMEText(body, "html", "utf -8")
msg['from'] = sender
msg['to'] = "841370939@qq.com"
msg['subject'] = subject
# ---------- 3. 发送邮件 ---------------------------
smtp = smtplib.SMTP()
smtp.connect(smtpserver) # 连服务器
smtp.login(sender, psw) # 登录
smtp.sendmail(sender, receiver, msg.as_string()) # 发送
smtp.quit() # 关闭