%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Python bindings for at-spi
Name:		pyatspi
Version:	2.5.5
Release:	1
Epoch:		1
Group:		Development/Python
License:	LGPLv2 and GPLv2
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:  python
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.1

Requires:	python-dbus

%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This version of at-spi is a major break from previous versions.
It has been completely rewritten to use D-Bus rather than
ORBIT / CORBA for its transport protocol.

This package includes a python client library for at-spi.

%prep
%setup -q

%build
%configure2_5x \
	--build=%{_build}

%make

%install
%makeinstall_std

%files
%doc COPYING COPYING.GPL AUTHORS README
%{py_puresitedir}/pyatspi