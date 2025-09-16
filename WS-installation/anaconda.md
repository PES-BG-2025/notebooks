# Comandos de Anaconda

# Muestra los entornos/ambientes disponibles
```
$ conda env list
```

# Muestra paquetes instalados en el entorno activo
```
$ conda list
```

# Para instalar numpy
```
$ conda install numpy
```

# Crear un ambiente aparte
```
$ conda create --name prog1 python=3.9 numpy
```

# Cambiar de ambiente
```
$ conda activate prog1
$ python
```

```
$ conda activate base
$ python
```

# Ver la versión de numpy dentro de Python 
```python
>>> import numpy as np 
>>> np.__version__
```

# Instalar jupyter en el entorno
```
$ conda install jupyter
```

# Correr (abrir) Jupyter
```
$ jupyter-notebook
```

# Correr (abrir) Jupyterlab
```
$ jupyter-lab
```