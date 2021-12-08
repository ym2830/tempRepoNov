def getBondDuration(y, face, couponRate, m):
    pvcfsum = 0
    weightSum = 0
    cf = face * couponRate
    for t in range(1,m+1):
        pv = (1+y)**-t
        pvcf = pv * cf
        weight = t * pvcf
        pvcfsum += pvcf
        weightSum += weight
    pvcfsum = pvcfsum + face * (1+y)**-m
    weightSum = weightSum + m * face * (1+y)**-m
    bondDuration = weightSum/pvcfsum
     
    return(bondDuration)

# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10