import hashlib

s="我爱你"
md5=hashlib.md5()
md5.update(s.encode('utf-8'))
print(md5.hexdigest())

md5=hashlib.md5(b'salt')
md5.update(s.encode('utf-8'))
print(md5.hexdigest())

sha1=hashlib.sha1()
sha1.update(s.encode('utf-8'))
print(sha1.hexdigest())