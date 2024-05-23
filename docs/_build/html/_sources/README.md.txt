# Build docs

## Install and use sphinx

**NOTE**: Use a virtual environment if you don't want to keep these requirements in your machine.

### Install sphinx
- Install ``pip``
    ```sh
    sudo apt install python3-pip
    ```
- Install ``sphinx``
    ```sh
    pip install sphinx
    ```
- Install ``myst-parser``
    ```sh
    pip install myst-parser
    ```
    - Install ``sphinx_rtd_theme``
    ```sh
    pip install sphinx_rtd_theme
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

Your ``index.rst`` has been built into ``index.html``
in your documentation output directory (``_build/html/index.html``).
Open this file in your web browser to see your docs.
