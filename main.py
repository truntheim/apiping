from fastapi import FastAPI, status, HTTPException
from scapy.all import IP, ICMP, sr1, raw, randstring

app = FastAPI()

@app.get("/api/ping")
async def ping(f_ipadd: str, f_timeout: int = 1, f_length: int = 56, f_count: int = 1):
    icmp_packet = IP(dst=f_ipadd)/ICMP()/raw(randstring(length=f_length))
    replies = 0
    for x in range(f_count):
        ans = sr1(icmp_packet,timeout=f_timeout)
        if ans != None:
            replies += 1

    if replies == 0:
        raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail="Not pingable.")
    else:
        return { "status": "success", "sent": f_count, "received": replies }
