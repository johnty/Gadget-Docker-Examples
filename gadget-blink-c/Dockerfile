FROM debian:stretch-slim as build

WORKDIR / 
RUN apt-get -yqq update 
RUN apt-get install -y crossbuild-essential-armhf git make automake build-essential libtool pkg-config zlib1g-dev
#RUN apt-get install -y liblo-dev
RUN git clone https://github.com/radarsat1/liblo
WORKDIR /liblo
RUN ./autogen.sh; make install
WORKDIR /
RUN git clone https://github.com/malloch/libmapper
WORKDIR /libmapper
RUN export PKG_CONFIG_PATH=/usr/local/pkgconfig
RUN  ./autogen.sh; make install
RUN ./test/testdatabase
WORKDIR /
COPY gpio.c .
RUN arm-linux-gnueabihf-gcc -I/usr/local/include gpio.c -L/usr/local/lib -o gpio -static 

FROM scratch
COPY --from=0 gpio .
CMD ["./gpio"]
