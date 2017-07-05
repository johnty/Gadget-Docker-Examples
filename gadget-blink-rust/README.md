# gadget-blink-rust
Written in [Rustlang](https://www.rust-lang.org/en-US/).

#### Dockerfile:
1. Using Docker's new [multi-stage build](https://docs.docker.com/engine/userguide/eng-image/multistage-build/) mechanism, this project starts with the official Docker `debian:stretch` image.
2. The `crossbuild-essential-armhf` package is installed for `rustc` to use for compiling/linking the binary.
3. [rustup](https://www.rustup.rs/)(Rust's recommended install method for Linux) is used to install the rust toolchain and supporting binaries.
4. The `armv7-unknown-linux-gnueabihf` target is added with `rustup`.
5. The source directory is copied into the image.
6. A configuration file is created for `cargo` to set the desired gcc toolchain for the armv7 target.
7. The source is compiled with `cargo build --target=armv7-unknown-linux-gnueabihf --release`
8. After the first image is successfully built, the second container is created from `arm32v7/debian:stretch-slim` (since we're using the gcc toolchain, a container with libc is still required).
9. The `gpio` binary is copied from the first image (image `0`).

#### gadget.yml:
- `directory: "./"`
  - Specifies to build the container from the `Dockerfile` in the current directory.
- `binds: ['/sys:/sys']`
  - Mounts the sysfs files required for accessing the filesystem representations of the GPIO pins.
- `command: []`
  - The container's command was previously set in the Dockerfile, so the value remains empty here.

#### rustio/:
- A standard scaffolding from `cargo new --bin` was created before hand. This is used for dependency management, compile-time options, etc.
- Each file and directory is checked to be sure the required filesystem items are available before accessing them.
- All fatal failures return the exit code (1), ensuring that a container created as a `service` will be automatically restarted.
- Further documentation can be found in the comments of the [source itself](https://github.com/NextThingCo/Gadget-Docker-Examples/blob/master/gadget-blink-rust/rustio/src/main.rs)

