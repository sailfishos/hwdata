Name:           hwdata
Version:        0.291
Release:        1
License:        GPLv2+
Summary:        Hardware identification and configuration data
Group:          System/Base
Source:         %{name}-%{version}.tar.bz2
Url:            http://git.fedorahosted.org/git/hwdata.git
Requires:       module-init-tools >= 3.2
BuildArch:      noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids database and MonitorsDb databases.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
./configure

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE COPYING
%dir %{_datadir}/%{name}
%{_libdir}/modprobe.d/dist-blacklist.conf
%{_datadir}/%{name}/*

