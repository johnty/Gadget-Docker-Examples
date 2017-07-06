# gadget-webserver
Simple example of how to host web content from your device.

#### Dockerfile:
- Start the container from the official Docker arm32v7 slim debian image `arm32v7/debian:stretch-slim`
- Install the light nginx metapackage, without recommended packages (non-essentials), and remove apt's supporting files.
- The contents of the web page get copied into the default web root.

#### gadget.yml:
- `net: "host"`
  - The container has full access to the host's network. In this case, it's purpose was simply to connect port 80.
- `directory: "./"`
  - Specifies to build the container from the `Dockerfile` in the current directory.
- `command: ["/usr/sbin/nginx", "-g", "'daemon off;'"]`
  - Start the nginx process without daemonizing, as we want docker to be able to read the long-term exit code, and restart the `service` if it exits with a failure code.

#### runtime:
- Linux and OSX hosts can now view the web page at 192.168.81.1 (192.168.82.1 for Windows hosts). This will show the web page in the browser of the host computer, using the device's usb ethernet connection.
- Using `gadget shell` and `connmanctl`, users can connect the device to a wifi network. Once connected to the wifi network, any device on the network can access the web page at the device's new ip (run `ifconfig` inside of `gadget shell` to determine the new IP on the wlan0 interface).

