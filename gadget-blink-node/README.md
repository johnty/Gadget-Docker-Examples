# gadget-blink-node
Javascript example running on top of [Node](https://nodejs.org/).

#### Dockerfile:
1. Using Docker's new [multi-stage build](https://docs.docker.com/engine/userguide/eng-image/multistage-build/) mechanism, this project starts from `scratch`(a completely empty new container).
2. At this time, there is no official `arm32v7/node` image available from Docker.
3. The pre-built tar file is downloaded, and copied to the root of the empty `scratch` image.
4. The second build stage is started from the slim variant of the official Docker Debian image for arm32v7.
5. The `node` binary is copied from the first image (image `0`), into the `/bin` directory of the final container.
  - There are several more `COPY` commands which are commented out. These hold supporting materials for Node applications (most notably the `npm` binary).
6. The `index.js` and `package.json` files are copied in. In this case, the `package.json` serves no purpose, but developers familiar with `node` and `npm` will likely need it for larger applications (for dependency management, startup, etc).

#### gadget.yml:
- `directory: "./"`
  - Specifies to build the container from the `Dockerfile` in the current directory.
- `binds: ['/sys:/sys']`
  - Mounts the sysfs files required for accessing the filesystem representations of the GPIO pins.
- `command: []`
  - The container's command was previously set in the Dockerfile, so the value remains empty here.

#### index.js:
- Each file and directory is checked to be sure the required filesystem items are available before accessing them.
- All fatal failures return the exit code (1), ensuring that a container created as a `service` will be automatically restarted.
- Further documentation can be found in the comments of the [source itself](https://github.com/NextThingCo/Gadget-Docker-Examples/blob/master/gadget-blink-node/index.js)

