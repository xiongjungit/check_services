# 用途
检测服务状态并发送邮件，故障自动恢复。

# 脚本说明

1. conf.py: 读取配置文件
2. ssh.py: 执行远程ssh
3. sendmail.py 发送邮件
4. check.py 检测服务状态，如果检测到服务状态不可用，则发送邮件并启动服务

# 使用方法

```
python check.py
```