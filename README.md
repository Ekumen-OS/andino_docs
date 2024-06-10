# Andino Docs

Manages andino ecosystem documentation.

Visit the [website](https://andino-documentation.readthedocs.io/en/latest/) to see all th information.

## Curiosities

- If you want to add images, you can use the relative path directly. If you want to add videos, use always the `_static` directory, as there is where they are placed inside the `html` directory, even though you initially have it inside the `media` folder.
- In this case, no Github Action is required for ReadTheDocs to work, we just need to setup the Webhook on the repository `Settings` to be able to build the documentation automatically every time a push is done or a pull request is merged. This is configured automatically if you are admin on the repo group. If not, refer to [this link](https://docs.readthedocs.io/en/stable/guides/setup/git-repo-manual.html).

## Get README.md

A bash script named `get_readme.sh` is included in the repo to retrieve the latest version of the `README.md` of andino packages to include them in the documentation. You just need to execute the script, it will clone the repo, extract the files and remove the repo:

```sh
chmod +x get_readme.sh
./get_readme.sh
```

## Build documentation locally

**NOTE**: Use a virtual environment if you don't want to keep these requirements in your machine.

### Install sphinx
- Install ``pip``
    ```sh
    sudo apt install python3-pip
    ```
- Install ``dependencies``
    ```sh
    pip install -r docs/requirements.txt
    ```
- Add the /.local/bin path to bash-profile (this allow execution of sphinx-build)
    - Open bash profile with any editor
        ```
        sudo gedit ~/.bash_profile
        ```
    - Add the following line, save and exit.
        ```
        export PATH="/home/$USER/.local/bin:$PATH"
        ```

### Build the project with sphinx

- In the docs folder

    ```sh
    make html
    ```

### Visualize the documentation locally

Your ``index.rst`` has been built into ``index.html``
in your documentation output directory (``_build/html/index.html``).
Open this file in your web browser to see your docs.

If you prefer, you can navigate to `docs/_build/html` and do `python3 -m http.server <port>` and you will be able to open the browser and see the docs at `localhost:<port>`.
