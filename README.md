## About
Number generator

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
             -it tigerj/numgen ash \
             -c "time python /usr/src/numgen.py $NUMGEN_NVAL $NUMGEN_KVAL > output.$(date +%m%d%y%H%M%S).txt"

