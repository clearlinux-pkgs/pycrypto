#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x9B8AA8CA2C77FFB0 (dlitz@dlitz.net)
#
Name     : pycrypto
Version  : 2.6.1
Release  : 43
URL      : http://pypi.debian.net/pycrypto/pycrypto-2.6.1.tar.gz
Source0  : http://pypi.debian.net/pycrypto/pycrypto-2.6.1.tar.gz
Source99 : http://pypi.debian.net/pycrypto/pycrypto-2.6.1.tar.gz.asc
Summary  : Cryptographic modules for Python.
Group    : Development/Tools
License  : Python-2.0
Requires: pycrypto-license = %{version}-%{release}
Requires: pycrypto-python = %{version}-%{release}
Requires: pycrypto-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : gmp-dev
BuildRequires : python3-dev
Patch1: cve-2013-7459.patch
Patch2: CVE-2018-6594.patch

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

%package license
Summary: license components for the pycrypto package.
Group: Default

%description license
license components for the pycrypto package.


%package python
Summary: python components for the pycrypto package.
Group: Default
Requires: pycrypto-python3 = %{version}-%{release}

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
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540316185
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pycrypto
cp COPYRIGHT %{buildroot}/usr/share/package-licenses/pycrypto/COPYRIGHT
cp LEGAL/copy/LICENSE.python-2.2 %{buildroot}/usr/share/package-licenses/pycrypto/LEGAL_copy_LICENSE.python-2.2
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pycrypto/COPYRIGHT
/usr/share/package-licenses/pycrypto/LEGAL_copy_LICENSE.python-2.2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
