#random pss: len-10 contains atleast 2upp 1dig 1special
import random
import string

alpha = random.choices(string.ascii_uppercase, k=2)
dig = random.choices(string.digits, k=1)
sp = random.choices('!@#$%^&*()-_=+',k=1)

remain = random.choices(string.ascii_letters + string.ascii_uppercase + string.digits + '!@#$%^&*()-_=+', k=6)

password = alpha + dig + sp + remain
random.shuffle(password)

pss_str = ''.join(password)

print(f"password: {pss_str}")