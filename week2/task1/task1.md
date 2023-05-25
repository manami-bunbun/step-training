# Task1 : Imprement Hash Table 

> Implement a hash table from scratch
> "Implement Python's dictionary from scratch" :)
> Hint 1: Implement delete(key)
> Hint 2: Implement rehashing
> Hint 3: Improve the hash function
> Your goal is to make the hash table work with mostly O(1) without depending on the number of items in the hash table



## 回答

[improved_hash_table.py](https://github.com/manami-bunbun/step-training/blob/main/week2/task1/improved_hash_table.py)

* [Step1 : Implement `delete()` function](#step1--implement-delete-function)
* [Step2 :Improve Hash function](#step2-improve-hash-function)
* [Step3 : Implement rehashing](#step3--implement-rehashing)
* [Step4 : Analysis & Improve](#step4--analysis--improve)

---


## Step1 : Implement `delete()` function 

**Code**  [initial_hash_table.py(sample code + delete())](https://github.com/manami-bunbun/step-training/blob/main/week2/task1/initial_hash_table.py)



[x] Implement `delete()` function in [sample code](https://github.com/xharaken/step2/blob/master/hash_table.py)

In this sample code, functions put() and get() are already implemented.

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
```


## Step2 :Improve Hash function


```python
def calculate_hash(key):
    assert type(key) == str
    # Note: This is not a good hash function. Do you see why?
    hash = 0
    for i in range(len(key)):
         hash += ord(key[i]) * i # Change!!!
    return hash
```


->とりあえず1/2倍になった

```
0 0.215556
1 0.411271
2 0.649769
3 0.942337
4 1.270887
5 1.590098
```

-> step3の後にまた変更


## Step3 : Implement rehashing

**Code** 

[improved_hash_table.py](https://github.com/manami-bunbun/step-training/blob/main/week2/task1/improved_hash_table.py)


[x] Implement `plot()` functions to see if the performance imploves for future implementations

```python
  def makeRehashTable(self, new_size):
    
        prev_hashTable = self.buckets
        new_hashTable = HashTable(new_size)
            
        for item in prev_hashTable:
            while item:
                new_hashTable.reappend(item)
                item = item.next
        
        self.bucket_size = new_hashTable.bucket_size
        self.buckets = new_hashTable.buckets
        self.item_count = new_hashTable.item_count 
        
        return
    
    def rehashOrLeave(self):
        
        sizeRate = self.item_count / self.bucket_size
        
        if 0.3 > sizeRate:
            new_size = self.bucket_size // 2 +1
            self.makeRehashTable(new_size)
            
        elif sizeRate > 0.7:
            new_size = self.bucket_size * 2 +1 
            self.makeRehashTable(new_size)
            
        return
```


## Step4 : Analysis & Improve 

[Data](https://github.com/manami-bunbun/step-training/blob/main/week2/task1/ComparisonData)

![Step3のreHash前後の比較](https://github.com/manami-bunbun/step-training/blob/main/week2/task1/ComparisonOfHashTable.png)

-> rehashは機能している


**hashの計算の仕方**
`hash += ord(key[i]) * i`だと、偶数になるなど衝突の可能性がまだ高い
-> `hash = hash*[素数]+ord(key[i])` にしてみた

![Step4のfunction関数比較](https://github.com/manami-bunbun/step-training/blob/main/week2/task1/ComparisonOfHashFunction.png)


```text
// 素数 : iteration, time

3 : 64,6.62539005279541
17 : 64,4.981743097305298
29 : 64,3.7304770946502686
43 : 64,4.317616939544678
97 : 64,4.449876070022583
499 : 64,4.738770008087158
```


-> `hash = hash*29+ord(key[i])` が最終回答


-> 最適な素数を求めるには...?(ここ不完全燃焼)
