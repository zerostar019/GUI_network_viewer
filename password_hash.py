import hashlib, os

# Функция шифровки пароля

def encrypt_password(password):
    salt = os.urandom(32)
    
    # generating new key
    key = hashlib.pbkdf2_hmac(
        'sha256',   # Алгоритм хэширования
         password.encode('utf-8'),  # Конвертируется пароль в байты
         salt,  # Предоставляется соль
         10000  # 10000 итераций SHA-256
    )
    
    return (key, salt)

# Функция проверки пароля

def check_password(new_password, old_password, salt):
    new_key = hashlib.pbkdf2_hmac(
        'sha256',
        new_password.encode('utf-8'),
        salt,
        10000
    )
    
    if new_key == old_password:
        return True
        
    else:
        return False
        