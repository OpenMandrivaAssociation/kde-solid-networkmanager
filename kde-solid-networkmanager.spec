%define snapshot r1084249
%define srcname networkmanager-0.7

Name:           kde-solid-networkmanager
Summary:        KDE Solid back-end for NetworkManager 0.7
Version:        4.4
Release:        %mkrel 0.%{snapshot}.1
Group:          System/Configuration/Networking
License:        GPLv2+
URL:            http://www.kde.org
#svn co svn://anonsvn.kde.org/home/kde/branches/KDE/4.4/kdebase/workspace/solid/networkmanager-0.7
Source0:        %{srcname}.%{snapshot}.tar.xz
# Make it build stand-alone (by Adam Pigg)
Patch0:         kde-solid-networkmanager-cmake.patch
BuildRequires:  libnm-util-devel
BuildRequires:  kdebase4-workspace-devel
Requires:       networkmanager
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This Solid module provides support for NetworkManager 0.7.

%prep
%setup -q -n %{srcname}
%patch0 -p0 -b .cmake

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_kde_datadir}/kde4/services/solidbackends/solid_networkmanager07.desktop
%{_kde_iconsdir}/oxygen/*/apps/networkmanager.png
%{_kde_libdir}/kde4/solid_networkmanager07.so
