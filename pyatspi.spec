%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Python bindings for at-spi
Name:		pyatspi
Version:	2.16.0
Release:	1
Group:		Development/Python
License:	LGPLv2 and GPLv2
Url:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pyatspi/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python3
BuildRequires:	python-gobject3-devel
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.90.1

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package includes a python client library for at-spi.

%package -n python-atspi
Summary:	Python bindings for at-spi
Group:		Development/Python
Requires:	python-dbus
Requires:	python-gi
# both pkgs are incorrect
%rename		pyatspi
%rename		python-pyatspi
%rename		python3-atspi

%description -n python-atspi
This package includes a python client library for at-spi.

%package -n python2-atspi
Summary:	Python3 bindings for at-spi
Group:		Development/Python
Requires:	python2-dbus
Requires:	python2-gobject3

%description -n python2-atspi
This package includes a python3 client library for at-spi.

%prep
%setup -q
mkdir ../py3build
cp -a . ../py3build
mv ../py3build .

%build
export PYTHON=%{__python2}
%configure2_5x \
	--build=%{_build}

pushd py3build
export PYTHON=%{__python3}
%configure2_5x \
	--build=%{_build}
popd

%make

%install
%makeinstall_std
%makeinstall_std -C py3build

%files -n python-atspi
%doc COPYING COPYING.GPL AUTHORS README
%{py3_puresitedir}/pyatspi

%files -n python2-atspi
%doc COPYING COPYING.GPL AUTHORS README
%{py2_puresitedir}/pyatspi

