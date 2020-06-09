message = 'date=2018-02-26 time=16:03:05 logver=54 devname="VCA-CORP-INET-900D" devid="FG900D3916800019" vd="edge" date=2018-02-26 time=16:03:05 logid="0317013312" type="utm" subtype="webfilter" eventtype="ftgd_allow" level="notice" policyid=2 sessionid=3124901122 user="" srcip=172.17.227.249 srcport=51724 srcintf="portA" dstip=34.228.11.148 dstport=80 dstintf="portB" proto=6 service="HTTP" hostname="pixel.moatads.com" profile="url_filtering" action="passthrough" reqtype="direct" url="/pixel.gif?e=32&amp;q=33&amp;g=34&amp;d=deutschzillowvideo9922410%3AAdRemainingTimeChange%3Aunknown%3Aunknown&amp;i=VPAID2JSWRAPPER1&amp;t=15196609" sentbyte=494 rcvdbyte=0 direction="N/A" msg="URL belongs to an allowed category in policy" method="domain" cat=17 catdesc="Advertising"'


def get_columns(message):
    
    val_begin = val_end = False
    q = 0
    quotes = False
    col = message[0]
    message = message[1:]
    cols = []
    
    for i in range(len(message)):
        if len(message) == i + 1: break

        if not val_begin:
            if val_end:
                if message[i] == ' ':
                    continue
                else:
                    val_end = False
                    col += message[i]
                    continue
            if message[i] == "=":
                val_begin=True
                if message[i+1] == '"':
                        quotes = True
                cols.append(col)
                col = ''
                continue
            else:
                col += message[i]
                continue
        else:
            if quotes:
                if message[i] == '"':
                    q += 1
                if q == 2:
                    val_end = True
                    val_begin = False
                    q = 0
                    quotes = False
                    continue
            elif message[i] == ' ':
                val_end = True
                val_begin = False
                        
    return cols







if __name__ == '__main__':
    cols = get_columns(message)
    print 'hi'