def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    pvcfsum = 0
    for(x1,x2) in zip(yc,times):
        pv = (1+x1)**-x2
        pvcf = coupon * pv
        pvcfsum += pvcf
    bondPrice = pvcfsum + face * pv
    return(bondPrice)



# Test values

yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04