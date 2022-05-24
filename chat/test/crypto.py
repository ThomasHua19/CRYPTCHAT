from cryptography.fernet import Fernet 
  
  
key = Fernet.generate_key()
print('clé' ,key)

f = Fernet(key)
print('Clé privé', f)
  
token = f.encrypt(b"Test1234") 
print('Message crypté' ,token) 

d = f.decrypt(token) 
print(d.decode(), 'Message décrypté :') 



test1 = f.encrypt(b'CRYPTCHAT 1234656')
print('Message crypté',test1)

print('Message décrypté',f.decrypt(test1))
