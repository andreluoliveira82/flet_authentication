import hashlib

"""
Nota de segurança

É importante notar que essa implementação usa uma abordagem de hash simples sem salting ou stretching, o que pode não ser adequado para uso em produção. Em um cenário real, você deve considerar usar um algoritmo de hash de senha mais seguro como bcrypt, scrypt ou Argon2, que fornecem recursos adicionais de segurança como salting e stretching para proteger contra ataques como ataques de tabela de arco-íris e cracking de senha.

Security note

It's worth noting that this implementation uses a simple hashing approach without salting or stretching, which may not be suitable for production use. In a real-world scenario, you should consider using a more secure password hashing algorithm like bcrypt, scrypt, or Argon2, which provide additional security features like salting and stretching to protect against attacks like rainbow table attacks and password cracking.

"""

def hash_password(password: str) -> str:
    """encrypts the password entered in the parameter

    Args:
        password (str): the password to be hashed

    Returns:
        str: return the hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()
