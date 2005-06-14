# TODO:
# - make use of external lrmi
Summary:	Utility for formatting Phoenix NoteBIOS hibernation partitions under Linux
Name:		lphdisk
Version:	0.9.1
Release:	0.2
License:	Artistic
Group:		Applications/System
Source0:	http://www.procyon.com/~pda/lphdisk/%{name}-%{version}.tar.bz2
# Source0-md5:	2ba99b08e7816ff3249eaf953fb5dc18
URL:		http://www.procyon.com/~pda/lphdisk/
BuildRequires:	lrmi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lphdisk is a linux reimplementation of the PHDISK.EXE (DOS) utility
provided with most Phoenix NoteBIOS-equipped laptop models. It will
properly format a NoteBIOS hibernation partition (type A0) to make it
usable by the BIOS for suspending to disk, avoiding the need to use
buggy and outdated DOS utilities to perform this configuration step.

This utility is intended to be the Linux equivalent of the DOS-only
utility "PHDISK.EXE" from Phoenix. This utility prepares and formats
the hibernation partition for notebook computers that use Phoenix
NoteBIOS. Once this partition has been prepared, it can be used with
the BIOS's APM Suspend-To-Disk feature.

Note that one does not need this utility to be able to take advantage
of the Suspend-To-Disk feature of these Phoenix NoteBIOS laptops. Once
the hibernation partition is prepared, either from the DOS utility
PHDISK.EXE that Phoenix provides, or lphdisk, it can be used to
suspend a machine's memory to disk.

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CREDITS NEWS README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*.8*
