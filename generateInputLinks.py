import sys
import csv

url = 'https://www.amazon.com/Muse-Brain-Sensing-Headband-Black/product-reviews/B00LOQR37C/ref=cm_cr_arp_d_paging_btm_'
url2 = '?ie=UTF8&pageNumber='


if(len(sys.argv) == 1):
    print 'Program execution method'
    print 'python generateInputLinks.py https://www.amazon.com/Muse-Brain-Sensing-Headband-Black/dp/B00LOQR37C 33'
    print 'python generateInputLinks.py https://www.amazon.com/<Product name >/dp/<Product ID> <Number of page reivews>'
    print 'The url should open the product on the Amazon website'
else:
    argLen = len(sys.argv)
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    dpIndex = str(sys.argv[1]).split('/').index('dp')
    productId = str(sys.argv[1]).split('/')[dpIndex + 1]
    productName = str(sys.argv[1]).split('/')[dpIndex - 1]
    print 'Product ID:', productId
    print 'Product Name:', productName
    pageNo = sys.argv[argLen-1]
    print 'Number of review pages:', pageNo

    f = open('amazonreviewpages.txt', 'w')
    for i in range(1,int(pageNo)+1):
        if(i == int(pageNo)):
            f.write(url + str(i) + url2 + str(i))
        else:
            f.write(url + str(i) + url2 + str(i) + '\n')
    f.close()



with open('amazonreviewpages.txt', 'rU') as file:
    rows = csv.reader(file)
    urls = []
    for row in rows:
        urls.append(row)
        print "'" + row[0] + "'"
    # print list(urls[0])
