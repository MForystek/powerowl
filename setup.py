from setuptools import setup, find_namespace_packages

"""
                                                    
########     #######    ##      ##   ########   ########      ^___^     ##      ##   ##       
##     ##   ##     ##   ##  ##  ##   ##         ##     ##    ##   ##    ##  ##  ##   ##       
##     ##   ##     ##   ##  ##  ##   ##         ##     ##   ## O O ##   ##  ##  ##   ##       
########    ##     ##   ##  ##  ##   ######     ########    ##  V  ##   ##  ##  ##   ##       
##          ##     ##   ##  ##  ##   ##         ##   ##     ##     ##   ##  ##  ##   ##       
##          ##     ##   ##  ##  ##   ##         ##    ##     ##   ##    ##  ##  ##   ##       
##           #######     ###  ###    ########   ##     ##     #####      ###  ###    ######## 

"""


setup(
    name='powerowl',
    version="0.1.0",
    packages=find_namespace_packages(include=[
        'powerowl.*'
    ]),
    install_requires=[
        'ipaddress==1.0.23',
        'matplotlib>=3.9.2',
        'netifaces==0.11.0',
        'networkx>=2.5',
        'numpy',
        'pandapower==2.14.11',
        #'pandapower @ git+https://github.com/e2nIEE/pandapower.git@2feba868882479fba6c8b0882c1bc77dfc71c77d#egg=pandapower'
        'pandas',
        'pydot',
        'plotly',
        'igraph==0.9.9',
        'pyyaml',
        'setuptools',
        'shapely',
        'ifcfg'
    ],
    python_requires=">=3.10.0",
    author="Lennart Bader (Fraunhofer FKIE)",
    author_email="lennart.bader@fkie.fraunhofer.de",
)
