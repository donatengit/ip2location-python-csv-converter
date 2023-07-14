import os

first_lines_expected = [
'"1.6.0.0/15","IN","India"\n',
'"1.8.0.0/16","CN","China"\n',
'"1.9.0.0/16","MY","Malaysia"\n',
'"1.10.0.0/21","CN","China"\n',
'"1.10.10.0/24","AU","Australia"\n',
'"1.10.11.0/24","CN","China"\n',
'"1.10.128.0/17","TH","Thailand"\n',
'"1.11.0.0/16","KR","Korea, Republic of"\n',
'"1.12.0.0/14","CN","China"\n',
'"1.16.0.0/18","KR","Korea, Republic of"\n',
'"1.16.64.0/18","-","-"\n',
'"1.18.116.0/22","KR","Korea, Republic of"\n',
'"1.18.136.0/21","-","-"\n',
'"1.20.0.0/16","TH","Thailand"\n',
]

def test_cidr(tmp_path):
    d = tmp_path / "test_cidr"
    d.mkdir()
    filename = "output_sample.csv"
    print(d)
    res = os.system(f"python3 ip2location-csv-converter.py -cidr -replace sample.csv {d}/{filename}")
    # print(res)

    errors = []

    with open(f"{d}/{filename}", "r") as f:
        for test_case in first_lines_expected:
            line = f.readline()
            if line != test_case:
                errors.append(f"Unexpected result: required {test_case} got {line}")

    assert not errors, "errors occured:\n{}".format("\n".join(errors))
