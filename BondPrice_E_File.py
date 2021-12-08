
def getBondPrice_E(face, couponRate, m, yc):
    coupon = face * couponRate
    pvcfsum = 0
    for t,x in enumerate(yc):
        pv = (1+x)**-(t+1)
        pvcf = coupon * pv
        pvcfsum += pvcf
    bondPrice = pvcfsum + face * pv
    return(bondPrice)



# Test values

yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5
