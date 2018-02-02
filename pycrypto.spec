#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9B8AA8CA2C77FFB0 (dlitz@dlitz.net)
#
Name     : pycrypto
Version  : 2.6.1
Release  : 32
URL      : http://pypi.debian.net/pycrypto/pycrypto-2.6.1.tar.gz
Source0  : http://pypi.debian.net/pycrypto/pycrypto-2.6.1.tar.gz
Source99 : http://pypi.debian.net/pycrypto/pycrypto-2.6.1.tar.gz.asc
Summary  : Cryptographic modules for Python.
Group    : Development/Tools
License  : Python-2.0
Requires: pycrypto-legacypython
Requires: pycrypto-python3
Requires: pycrypto-python
BuildRequires : gmp-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: cve-2013-7459.patch

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

%package legacypython
Summary: legacypython components for the pycrypto package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the pycrypto package.


%package python
Summary: python components for the pycrypto package.
Group: Default
Requires: pycrypto-legacypython
Requires: pycrypto-python3

%description python
python components for the pycrypto package.


%package python3
Summary: python3 components for the pycrypto package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pycrypto package.


%prep
%setup -q -n pycrypto-2.6.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507169048
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python setup.py test
%install
export SOURCE_DATE_EPOCH=1507169048
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
