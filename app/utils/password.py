from logging import getLogger

import bcrypt

password_utils_logger = getLogger('project.password')

def hash_password(password: str) -> bytes:
    password_utils_logger.info('Hashing password')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def password_is_correct(password: bytes, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password, hashed_password)

