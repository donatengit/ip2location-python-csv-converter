import os

def test_no_arguments():
    res = os.system("python3 ip2location-csv-converter.py")
    assert res != 0

def test_one_argument():
    res = os.system("python3 ip2location-csv-converter.py -cidr")
    print(res)
    assert res != 0

def test_two_arguments():
    res = os.system("python3 ip2location-csv-converter.py -cidr sample.csv")
    print(res)
    assert res != 0

def test_three_arguments():
    res = os.system("python3 ip2location-csv-converter.py -cidr -replace sample.csv")
    print(res)
    assert res != 0
