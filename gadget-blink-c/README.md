# gadget-blink-c
A gnu89 compatible C example of GPIO usage, easily translatable to C++. 

#### Dockerfile:
1. Using Docker's new [multi-stage build](https://docs.docker.com/engine/userguide/eng-image/multistage-build/) mechanism, this project starts the `debian:stretch-slim` image, and uses the cross-building toolchain package `crossbuild-essential-armhf`.
2. The source content is copied into the container.
3. The source is compiled with the `arm-linux-gnueabihf-gcc` compiler
  - The `static` flag is given to build all dependencies into the binary, this permits the final container to be built from scratch.
  - Be sure to check the licenses of any dependencies, and whether those conflict with your project's license.
  - When using other libraries, the armhf versions of those will need to be installed. Debian offers their "[Multiarch](https://wiki.debian.org/Multiarch/HOWTO)" system for this purpose.
  - Using non-standard-lib packages may also require the use of additional [linker](https://gcc.gnu.org/onlinedocs/gcc-6.3.0/gcc/Link-Options.html#Link-Options) and/or [include](https://gcc.gnu.org/onlinedocs/gcc-6.3.0/gcc/Directory-Options.html#Directory-Options) flags.
4. After the first image is successfully built, the second container is created from scratch.
5. The `gpio` binary is copied from the first image (image `0`).

#### gadget.yml:
- `directory: "./"`
  - Specifies to build the container from the `Dockerfile` in the current directory.
- `binds: ['/sys:/sys']`
  - Mounts the sysfs files required for accessing the filesystem representations of the GPIO pins.
- `command: []`
  - The container's command was previously set in the Dockerfile, so the value remains empty here.

#### gpio.c:
- Each file and directory is checked to be sure the required filesystem items are available before accessing them.
- All fatal failures return the exit code (1), ensuring that a container created as a `service` will be automatically restarted.
- Further documentation can be found in the comments of the [source itself](https://github.com/NextThingCo/Gadget-Docker-Examples/blob/master/gadget-blink-c/gpio.c)
