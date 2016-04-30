#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pycrypto
Version  : 2.6.1
Release  : 17
URL      : https://pypi.python.org/packages/source/p/pycrypto/pycrypto-2.6.1.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pycrypto/pycrypto-2.6.1.tar.gz
Summary  : Cryptographic modules for Python.
Group    : Development/Tools
License  : Python-2.0
Requires: pycrypto-python
BuildRequires : gmp-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Python Cryptography Toolkit (pycrypto)
======================================
This is a collection of both secure hash functions (such as SHA256 and
RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal,
etc.).  The package is structured to make adding new modules easy.
This section is essentially complete, and the software interface will
almost certainly not change in an incompatible way in the future; all
that remains to be done is to fix any bugs that show up.  If you
encounter a bug, please report it in the Launchpad bug tracker at

%package python
Summary: python components for the pycrypto package.
Group: Default

%description python
python components for the pycrypto package.


%prep
%setup -q -n pycrypto-2.6.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
