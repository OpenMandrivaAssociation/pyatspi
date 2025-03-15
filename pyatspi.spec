%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Python bindings for at-spi
Name:		pyatspi
Version:	2.46.1
Release:	4
Group:		Development/Python
License:	LGPLv2 and GPLv2
Url:		https://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:	https://ftp.gnome.org/pub/GNOME/sources/pyatspi/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	python
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

%prep
%autosetup -p1

%build
%configure \
	--build=%{_build}

%make_build

%install
%make_install

%files -n python-atspi
%doc COPYING COPYING.GPL AUTHORS README*
%{py3_puresitedir}/pyatspi
