Summary:	Utility for formatting Phoenix NoteBIOS hibernation partitions under Linux
Summary(pl.UTF-8):   Narzędzie do formatowania partycji hibernacji Phoenix NoteBIOS pod Linuksem
Name:		lphdisk
Version:	0.9.1
Release:	0.9
License:	Artistic
Group:		Applications/System
Source0:	http://www.procyon.com/~pda/lphdisk/%{name}-%{version}.tar.bz2
# Source0-md5:	2ba99b08e7816ff3249eaf953fb5dc18
Patch0:		%{name}-build_fix.patch
URL:		http://www.procyon.com/~pda/lphdisk/
BuildRequires:	lrmi-devel
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lphdisk is a linux reimplementation of the PHDISK.EXE (DOS) utility
provided with most Phoenix NoteBIOS-equipped laptop models. It will
properly format a NoteBIOS hibernation partition (type A0) to make it
usable by the BIOS for suspending to disk, avoiding the need to use
buggy and outdated DOS utilities to perform this configuration step.
Once this partition has been prepared, it can be used with the BIOS's
APM Suspend-To-Disk feature.

%description -l pl.UTF-8
lphdisk to linuksowa reimplementacja dosowego narzędzia PHDISK.EXE
dostarczanego z większością modeli laptopów zawierających Phoenix
NoteBIOS. Narzędzie to odpowiednio formatuje partycję hibernacji
NoteBIOS (typu A0) czyniąc ją używalną dla BIOS-u przy opcji suspend
to disk - unikając używania zawierających błędy i przestarzałych
narzędzi dosowych do wykonania tego kroku. Po przygotowaniu partycji
można jej używać z opcją APM Suspend-To-Disk BIOS-u.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I/usr/include/lrmi"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
