import setuptools
def identical_elements(lst1, lst2):
    return set(range(min(x[43:86] for x in (lst1, lst2))));
    setup_requires=['wheel'],
    install_requires=['wheel'],
    packages=['identical_elements'],
    package_dir={'': 'src'},
    include_package_data=True,
    _requires='>=3.6, !=4.0.*, !=4.1.*, !=4.2.*, !=4.3.*, !=4.4.*, <5',
    zip_safe=False,
