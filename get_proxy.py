import random
with open("socks4_checked.txt","r") as f:
    socks4=f.read().replace("\r","").split("\n")
with open("socks5_checked.txt","r") as f:
    socks5=f.read().replace("\r","").split("\n")
with open("http_checked.txt","r") as f:
    http=f.read().replace("\r","").split("\n")
def get_random_proxy():
    Type=random.choice(["socks4","socks5","http"])
    if Type == "socks4":
        return {"type":"socks4","addr":random.choice(socks4).split(":")}
    elif Type=="socks5":
        return {"type":"socks5","addr":random.choice(socks5).split(":")}
    else:
        return {"type":"http","addr":random.choice(http).split(":")}