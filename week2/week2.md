# Week2

## Task1 : Imprement Hash Table 

### Step1 : Implement `delete()` function 

[x] Implement `delete()` function in [sample code](https://github.com/xharaken/step2/blob/master/hash_table.py)

In this sample code, functions put() and get() are already implemented.


### Step2 : Implement rehashing

[x] Implement `plot()` functions to see if the performance imploves for future implementations


Here, HashTable is too small to put many values. 

```python
class HashTable:

# Initialize the hash table.
def __init__(self):
    # Set the initial bucket size to 97. A prime number is chosen to reduce
    # hash conflicts.
    self.bucket_size = 97
    self.buckets = [None] * self.bucket_size
    self.item_count = 0

```

At this point, the performance is showen in the table below.

```
0 0.429964
1 0.905610
2 1.494375
3 2.437892
4 3.040883
5 4.082451
6 4.641600
7 6.052764
8 6.472566
9 7.040555
10 9.822368
11 10.130135
12 11.322376
13 11.589523
14 12.243068
15 13.475018
16 13.188014
17 14.392471
18 16.440604
19 26.637178
20 17.524026
21 18.356225
22 19.139280
23 19.061131
24 20.917586
25 23.350954
26 25.480513
27 25.056638
28 25.641068
29 26.122916
30 27.301717
31 31.004267
32 32.181343
33 29.272004
34 31.309819
35 39.299112
36 33.369044
37 34.067673
38 36.220920
39 41.200210
40 37.747960
41 40.925630
42 43.681221
43 45.126961
44 42.177296
45 46.038121
46 51.291120
47 47.017898
48 45.261708
49 52.433843
50 51.626996
51 53.052560
52 57.004585
53 51.858914
54 53.692454
55 56.616799
56 53.159730
57 60.417644
58 56.494767
59 57.392025
60 66.760685
61 62.828812
62 67.897762
63 62.927791
64 64.205859
65 64.683427
66 67.623868
67 67.620655
68 69.720894
69 72.448814
70 74.821310
71 76.863297
72 75.574875
73 79.019056
74 100.144539
75 86.816478
76 81.742347
77 82.278338
78 89.465378
79 89.799625
80 95.812679
81 93.099069
82 87.720971
83 91.659335
84 88.078045
85 92.286998
86 104.710605
87 122.157469
88 102.098392
89 120.244320
90 101.289186
91 104.112472
92 114.609117
93 114.299887
94 119.635328
95 132.622807
96 125.148661
97 120.045058
98 129.840983
99 250.208446
```

Even after implementing new hashTable, time doesn't change that much
```
def rehashOrLeave(self):
        
        sizeRate = self.item_count / self.bucket_size
        
        if 0.3 < sizeRate:
            new_size = self.bucket_size // 2
            self.makeRehashTable(new_size)
            
        elif sizeRate < 0.7:
            new_size = self.bucket_size * 5
            self.makeRehashTable(new_size)
            
        return
```



### STEP3 :Improve Hash function



```
def calculate_hash(key):
    assert type(key) == str
    # Note: This is not a good hash function. Do you see why?
    hash = 0
    for i in range(len(key)):
        hash += ord(key[i]) * i
    return hash
```


-> 1/2倍になった

```
0 0.215556
1 0.411271
2 0.649769
3 0.942337
4 1.270887
5 1.590098
6 1.959919
7 2.221562
8 2.544933
9 3.182119
10 3.190971
11 3.602216
12 3.848090
13 4.216606
14 4.571966
15 5.167963
16 5.488303
17 5.718835
18 6.070940
19 7.257226
20 7.190357
21 7.610456
22 7.885680
23 8.210770
24 8.562949
25 8.848904
26 9.461035
27 10.564566
28 10.237998
29 10.050473
30 11.075520
31 11.969582
32 11.861138
33 11.876590
34 12.540232
35 13.642652
```



## Task2 
 