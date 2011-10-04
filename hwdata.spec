#
# Please submit bugfixes or comments via http://bugs.meego.com/
#

Name:           hwdata
Version:        0.232
Release:        1
License:        GPLv2+ and LGPLv2+
Summary:        Hardware identification and configuration data
Group:          System/Base
Source:         hwdata-%{version}.tar.bz2

Url:            http://git.fedorahosted.org/git/hwdata.git
Requires:       module-init-tools >= 3.2
BuildArch:      noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids database and MonitorsDb databases.

%prep

%setup -q

%build
# nothing to build

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE COPYING
%dir %{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist.conf
%{_datadir}/%{name}/*

