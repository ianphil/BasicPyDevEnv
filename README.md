# Basic Container Based Python Developer Environment

The contents of this repo contain a simple boiler plate repo. The magic is in the `.devcontainer` folder. This folder configures a remote connection to a container. This container becomes the development environment for yourself and VSCode. Basically it boots up a container, mounts your folder into that container, connects VSCode to the VSCodeServer running in the container. This means everything you do inside your IDE is in the container. We've verified this configuration using Windows 7, Windows 10, OSX Mojave & Catalina, and Fedora 30.

![image](https://user-images.githubusercontent.com/17349002/68078504-390f8a00-fdad-11e9-9c12-84d4a50b8e07.png)

More detail about [Developing inside a Container](https://code.visualstudio.com/docs/remote/containers)

# Usage

We use SSH for our git push/pulls. Create a .ssh folder in the root of this repo, put valid keys in this folder. This is the only real requirement. Then...

Open VSCode and in the bottom right click the green "remote connection" `><` button. Select `open remote container folder` and browse to this repo. VSCode will do the rest.