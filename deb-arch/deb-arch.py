import os

def GetDebDownloadURL(pkgname):
    r = os.popen("apt-get install --reinstall --print-uris -qq "+ pkgname +" | cut -d\"'\" -f2")
    deburl = r.read()
    r.close()
    return deburl

def DownloadDeb(pkgname):
    os.popen("aria2c -s20 -x16 -k1M -c \""+GetDebDownloadURL(pkgname+"\"")
