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

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The hwdata-devel package contains files for developing applications that use
hwdata.


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

%files devel
%{_datadir}/pkgconfig/hwdata.pc
