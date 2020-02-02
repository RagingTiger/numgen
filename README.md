## About
Number generator

## Introduction
This is a simple number generator, written in Python 3, that will create all possible permutations 
of `n-elements` in a string of `k-elements` where the digits `0 - 9` are the only elements used.
The below example shows `n = 2` and `k = 2`:
```
$ N=2; K=2
$ python3 numgen.py $N $K
00
01
10
11
```
The next axample shows `n = 3` and `k = 2`:
```
$ N=3; K=2
$ python3 numgen.py $N $K
00
10
20
01
11
21
02
12
22
```
Since only digits `0-9` are used, then the max number of elements `n` is limited to 10:
```
$ N=11; K=1
$ python3 numgen.py $N $K
Maximum value of n is 10. Please try again.
```

## Docker
Build image with accompanying docker file and use as follows

### Build
```
$ docker build -t numgen .
```

### Run
```
$ NUMGEN_NVAL=10; NUMGEN_KVAL=2
$ docker run -d \
             --name numgen.$(date +%m%d%y%H%M%S) \
             -v $PWD:/home/numgen \
             -it numgen ash \
             -c "time python /usr/src/numgen.py $NUMGEN_NVAL $NUMGEN_KVAL > output.$(date +%m%d%y%H%M%S).txt"
```

### Logs
```
# How to view the time results
$ docker logs -f numgen.013120140955
real    0m 0.04s
user    0m 0.03s
sys     0m 0.00s
```

## Output File
Output file will have format similar to `output.013120140955.txt` where the `013120140955` is the
date the file was generated
