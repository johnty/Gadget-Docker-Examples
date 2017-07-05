# gadget-blink-python
Python GPIO example using the community-run library [CHIP_IO](https://github.com/xtacocorex/CHIP_IO).

#### Dockerfile:
1. This image starts from the `armhf/alpine` image, and installs the dependencies required for building the `CHIP_IO` library.
2. After the build is complete, all the previously required dependencies are removed in the same `RUN` step (this saves space when Docker saves the image state after the `RUN` stage finishes)
3. The `blink.py` file is copied into the image, and the `CMD` is set.

#### gadget.yml:
- `directory: "./"`
  - Specifies to build the container from the `Dockerfile` in the current directory.
- `binds: ['/sys:/sys']`
  - Mounts the sysfs files required for accessing the filesystem representations of the GPIO pins.
- `command: ['python','blink.py']`
  - The container's command was previously set in the Dockerfile, so the value here is not required, but can regardless be set or modified.
- `capabilities: ['SYS_RAWIO']`
  - The `SYS_RAWIO` [capability](http://man7.org/linux/man-pages/man7/capabilities.7.html) is required to have read/write access to device nodes, like `/dev/mem`
- `devices: ['/dev/mem']`
  - This device will be mounted in the running container. This isn't in the other GPIO examples because the `CHIP_IO` library access the kernel's memory locations for the GPIO values rather than the filesystem representations in order to achieve faster read/write speeds.

#### blink.py:
- Each file and directory is checked to be sure the required filesystem items are available before accessing them.
- This example relies on the internal error checking mechanisms of `CHIP_IO` to manage return codes inside the `try:` block.
- View the [source itself](https://github.com/NextThingCo/Gadget-Docker-Examples/blob/master/gadget-blink-python/blink.py)

