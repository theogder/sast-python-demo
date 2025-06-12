import os 
def insecure(): 
password = os.getenv('DB_PASSWORD') 
print("Connecting with password:", password) 
def unused_code(): 
return "This is never used" 
insecure()
