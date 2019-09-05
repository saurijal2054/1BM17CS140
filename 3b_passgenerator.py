import string
import random
def randompassword():
    chars=string.printable
    print(string.printable)  
    size=random.randint(8,12)
  
    print("PASSWORD GENERATED")
    return ''.join(random.choice(chars) for x in range(size))
print(randompassword())
