import os

test_input = ['''
178.154.128.0/22
178.154.134.0/23
178.154.147.0/24
178.154.170.0/23
178.154.183.0/24
178.154.128.0/19
178.154.131.0/24
178.154.160.0/19
'''
    , '''178.154.128.0/19
178.154.131.0/24
178.154.160.0/19
'''
    , '''37.209.224.0/20
37.220.80.0/24
37.220.86.0/24
37.220.152.0/21
37.220.176.0/20
37.221.80.0/22
91.237.220.0/22
91.237.230.0/24'''
    , '''37.220.164.100/32'''
              ]


def test_cidr_merge(tmp_path):
    filename = f"{tmp_path}/output_merge.csv"
    test_input_files = []
    for i, test_in in enumerate(test_input):
        f_name = f"{tmp_path}/test_input_{i}"
        tf = open(f_name, "w")
        tf.write(test_in)
        tf.close()
        test_input_files.append(f_name)
        print([x.strip() for x in open(f_name, "r").readlines()])

    res = os.system(f"python3 ip_cidr_merge.py {filename} {' '.join(test_input_files)}")
    assert res == 0

    assert sorted(open(filename, "r").readlines()) == sorted(
        ['37.209.224.0/20\n', '37.220.80.0/24\n', '37.220.86.0/24\n', '37.220.152.0/21\n', '37.220.164.100/32\n',
         '37.220.176.0/20\n', '37.221.80.0/22\n', '91.237.220.0/22\n', '91.237.230.0/24\n', '178.154.128.0/18\n'])
