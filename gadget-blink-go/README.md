# gadget-blink-go
Written in [Golang](https://golang.org/).

#### Dockerfile:
1. Using Docker's new [multi-stage build](https://docs.docker.com/engine/userguide/eng-image/multistage-build/) mechanism, this project starts with the official Docker `golang` image.
2. The source content is copied into the container.
3. Go natively supports cross compilation for arm Linux. This is enabled with the variables `GOOS=linux GOARCH=arm`
4. After the first image is successfully built, the second container is created from scratch (pure Go code is statically linked by default).
5. The `gpio` binary is copied from the first image (image `0`).

#### gadget.yml:
- `directory: "./"`
  - Specifies to build the container from the `Dockerfile` in the current directory.
- `binds: ['/sys:/sys']`
  - Mounts the sysfs files required for accessing the filesystem representations of the GPIO pins.
- `command: []`
  - The container's command was previously set in the Dockerfile, so the value remains empty here.

#### gpio.go:
- Each file and directory is checked to be sure the required filesystem items are available before accessing them.
- All fatal failures return the exit code (1), ensuring that a container created as a `service` will be automatically restarted.
- Further documentation can be found in the comments of the [source itself](https://github.com/NextThingCo/Gadget-Docker-Examples/blob/master/gadget-blink-go/gpio.go)

