# kagglex_showcase

### 1. Running with docker 
<p align="justify">
To run the docker, just type <code>docker run -it -p 8888:8888 gee-community/geemap:latest</code>, but before doing that, we first need to set up the permissions of two directories, where all the dependencies will be mapped, both local and container.
</p>

    cd kagglex_showcase
    sudo chown 5050:5050 kagglex_showcase

</p>

### 1. Running Streamlit app 
<p align="justify">
To run the Streamlit app, just type <code>streamlit run ./Home.py</code>
</p>


### Where to find your Earth Engine token?

- **Windows:** `C:/Users/USERNAME/.config/earthengine/credentials`
- **Linux:** `/home/USERNAME/.config/earthengine/credentials`
- **macOS:** `/Users/USERNAME/.config/earthengine/credentials`
