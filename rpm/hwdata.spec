Name:           hwdata
Version:        0.387
Release:        1
License:        GPLv2+
Summary:        Hardware identification and configuration data
Source:         %{name}-%{version}.tar.bz2
URL:            https://github.com/sailfishos/hwdata
BuildArch:      noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids database and MonitorsDb databases.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./configure --libdir=%{_libdir}

%install
%make_install

%files
%license LICENSE COPYING
%dir %{_datadir}/%{name}
%{_libdir}/modprobe.d/dist-blacklist.conf
%{_datadir}/%{name}/*
%{_datadir}/pkgconfig/hwdata.pc
