from setuptools import setup, find_packages, find_namespace_packages

# Package metadata and the console script live in pyproject.toml. One install covers VGGT-SLAM and its two
# submodules: vggt (third_party/vggt, MIT-SPARK/VGGT_SPARK; a namespace package without __init__.py files) and
# salad (third_party/salad; only the salad package, its training-only top-level modules are left out).
setup(
    packages=find_packages(include=['evals', 'evals.*', 'vggt_slam', 'vggt_slam.*'])
        + find_namespace_packages(where='third_party/vggt', include=['vggt', 'vggt.*'])
        + find_packages(where='third_party/salad', include=['salad', 'salad.*']),
    package_dir={
        'vggt': 'third_party/vggt/vggt',
        'salad': 'third_party/salad/salad',
    },
    py_modules=['vslamlab_vggtslam_mono'],
)
