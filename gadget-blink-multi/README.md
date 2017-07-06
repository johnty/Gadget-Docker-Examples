# gadget-blink-multi
A demonstration of a multiple-container project running all GPIO examples at once.

#### Dockerfile:
 - N/A, as all containers are pulled from [Dockerhub](https://hub.docker.com/r/nextthingco/).

#### gadget.yml:
- `image: "nextthingco/gadget-blink-*"`
  - Specifies which image to pull from Dockerhub ($user/$image-name)
- `directory: ""`
  - As opposed to the single GPIO examples, this gadget.yml will pull all images from Dockerhub, so the `directory` value is left empty.
- `binds: [], capabilites: [], devices: [], and command: []`
  - These values may vary between containers, depending on the implementation of the program.
- `onboot: [] vs services: []`
  - Some containers here were arbitrarily chosen to run as `onboot` containers, simply to show what a large project orchestration may look like

#### runtime:
- A program (`gadget-initc`) will read the gadget.yml file (which is copied to the device on each `gadget [action]`), and launch each container in sequence.
- In this example, `blink-c` will start first, followed by `blink-go`. Each of these processes will fork off, meaning that their order in the gadget.yml alone is not a robust enough method of ensuring that the prior containers have started. For example, if the first container started a program with a RESTful API available on port 80, and a second container strictly accesses that port with some POST/GET requests, the developer should account for the possibility that the RESTful service might not be immediately available.
- Once all `onboot` containers have started, the `service` containers are launched in sequence.
- `onboot` containers differ from `services` in that when an `onboot` container exits, it will not be started until the next boot. `services`, however, will be restarted automatically if they exit with any non-zero return code.

