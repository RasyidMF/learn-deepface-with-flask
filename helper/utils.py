import os
from dotenv import load_dotenv

# Load env
load_dotenv()
def getEnv(key: str, default: any):
    val = os.getenv(key)
    if val == None or len(val) == 0: return default
    else: return val
    
def isEmpty(any):
    return any == None or any == ""