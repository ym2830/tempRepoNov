
def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    cf = face * couponRate / ppy
    for t in range(1,m*ppy+1):
        pv = (1+y/ppy)**-t
        pvcf = pv * cf
        pvcfsum += pvcf
    bondPrice = pvcfsum + face * pv
    
    return(bondPrice)


# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10