from setuptools import setup, find_packages

app_name = 'django-chronograph'

setup(
    name=app_name,
    version='0.1.11',
    description='Django chronograph application.',
    author='Weston Nielson',
    author_email='wnielson@gmail.com',
    packages = find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
