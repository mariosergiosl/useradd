#
# spec file for package shadow
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Summary:        Utilities to Manage User and Group Accounts
License:        BSD-3-Clause and GPL-2.0+
Group:          System/Base
Name:           shadow
Version:        4.1.5.1
Release:        8.1.2
Url:            http://pkg-shadow.alioth.debian.org/
Source:         http://pkg-shadow.alioth.debian.org/releases/shadow-%{version}.tar.bz2
Source1:        pamd.tar.bz2
Source2:        README.changes-pwdutils
Source3:        useradd.local
Source4:        userdel-pre.local
Source5:        userdel-post.local
Patch:          shadow-login_defs.diff
Patch1:         userdel-scripts.diff
Patch2:         useradd-script.diff
Patch3:         chkname-regex.diff
Patch4:         useradd-default.diff
Patch5:         getdef-new-defs.diff
Patch6:         shadow-4.1.5.1-manfix.patch
Patch7:         shadow-4.1.5.1-logmsg.patch
Patch8:         shadow-4.1.5.1-errmsg.patch
Patch9:         shadow-4.1.5.1-backup-mode.patch
BuildRequires:  audit-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  pam-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         permissions
Provides:       pwdutils = 3.2.20
Obsoletes:      pwdutils <= 3.2.19

%description
This package includes the necessary programs for converting plain
password files to the shadow password format and to manage user and
group accounts.

%prep
%setup -q -a 1
%patch -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p1
%patch7 -p1
%patch8 -p0
%patch9 -p1

iconv -f ISO88591 -t utf-8  doc/HOWTO > doc/HOWTO.utf8
mv -v doc/HOWTO.utf8 doc/HOWTO

%build
export CFLAGS="$RPM_OPT_FLAGS -fpie"
export LDFLAGS="-pie"

%configure \
        --disable-shadowgrp \
	--enable-account-tools-setuid \
        --with-audit \
        --with-libpam \
        --with-sha-crypt \
	--with-acl \
	--with-attr \
	--with-nscd \
        --with-selinux \
        --without-libcrack \
        --disable-shared \
	--with-group-name-max-length=32
make

%install
cp %SOURCE2 .
make install DESTDIR=$RPM_BUILD_ROOT gnulocaledir=$RPM_BUILD_ROOT/%{_datadir}/locale MKINSTALLDIRS=`pwd`/mkinstalldirs

# install useradd.local, userdel.local, ...
install -m 0755 %SOURCE3 $RPM_BUILD_ROOT/%{_sbindir}/
install -m 0755 %SOURCE4 $RPM_BUILD_ROOT/%{_sbindir}/
install -m 0755 %SOURCE5 $RPM_BUILD_ROOT/%{_sbindir}/

# Remove binaries we don't use.
rm $RPM_BUILD_ROOT/%{_bindir}/groups
rm $RPM_BUILD_ROOT/%{_mandir}/man1/groups.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/groups.*

rm $RPM_BUILD_ROOT/%{_sbindir}/grpconv
rm $RPM_BUILD_ROOT/%{_mandir}/man8/grpconv.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/grpconv.*
rm $RPM_BUILD_ROOT/%{_sbindir}/grpunconv
rm $RPM_BUILD_ROOT/%{_mandir}/man8/grpunconv.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/grpunconv.*

rm $RPM_BUILD_ROOT/%{_sbindir}/groupmems
rm $RPM_BUILD_ROOT/%{_mandir}/man8/groupmems.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/groupmems.*
rm $RPM_BUILD_ROOT/etc/pam.d/groupmems

rm $RPM_BUILD_ROOT/%{_bindir}/login
rm $RPM_BUILD_ROOT/%{_mandir}/man1/login.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/login.*
rm $RPM_BUILD_ROOT/etc/pam.d/login

rm $RPM_BUILD_ROOT/%{_bindir}/su
rm $RPM_BUILD_ROOT/%{_mandir}/man1/su.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man1/su.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/suauth.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/suauth.*
rm $RPM_BUILD_ROOT/etc/pam.d/su

rm $RPM_BUILD_ROOT/%{_bindir}/faillog
rm $RPM_BUILD_ROOT/%{_mandir}/man5/faillog.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/faillog.*
rm $RPM_BUILD_ROOT/%{_mandir}/man8/faillog.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/faillog.*

rm $RPM_BUILD_ROOT/%{_sbindir}/logoutd
rm $RPM_BUILD_ROOT/%{_mandir}/man8/logoutd.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/logoutd.*
rm $RPM_BUILD_ROOT/%{_sbindir}/nologin
rm $RPM_BUILD_ROOT/%{_mandir}/man8/nologin.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/nologin.*

rm $RPM_BUILD_ROOT/%{_sbindir}/chgpasswd
rm $RPM_BUILD_ROOT/%{_mandir}/man8/chgpasswd.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man8/chgpasswd.*
rm $RPM_BUILD_ROOT/etc/pam.d/chgpasswd

rm $RPM_BUILD_ROOT/%{_mandir}/man3/getspnam.*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man3/getspnam.*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/gshadow.5*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/gshadow.5*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/passwd.5*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/passwd.5*
rm $RPM_BUILD_ROOT/%{_mandir}/man5/shadow.5*
rm $RPM_BUILD_ROOT/%{_mandir}/*/man5/shadow.5*

rm -rf $RPM_BUILD_ROOT%{_mandir}/{??,??_??}

%find_lang shadow

%clean
rm -rf $RPM_BUILD_ROOT

%post
%set_permissions /usr/bin/chage
%set_permissions /usr/bin/chfn
%set_permissions /usr/bin/chsh
%set_permissions /usr/bin/expiry
%set_permissions /usr/bin/gpasswd
%set_permissions /usr/bin/newgrp
%set_permissions /usr/bin/passwd

%verifyscript
%verify_permissions /usr/bin/chage
%verify_permissions /usr/bin/chfn
%verify_permissions /usr/bin/chsh
%verify_permissions /usr/bin/expiry
%verify_permissions /usr/bin/gpasswd
%verify_permissions /usr/bin/newgrp
%verify_permissions /usr/bin/passwd

%files -f shadow.lang
%defattr(-,root,root)
%doc NEWS doc/HOWTO README README.changes-pwdutils
%attr(0644,root,root) %config %{_sysconfdir}/login.defs
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/default/useradd
%config /etc/pam.d/chage
%config /etc/pam.d/chfn
%config /etc/pam.d/chsh
%config /etc/pam.d/passwd
%config /etc/pam.d/useradd
%config /etc/pam.d/chpasswd
%config /etc/pam.d/groupadd
%config /etc/pam.d/groupdel
%config /etc/pam.d/groupmod
%config /etc/pam.d/newusers
%config /etc/pam.d/useradd
%config /etc/pam.d/userdel
%config /etc/pam.d/usermod
%attr(4755,root,shadow) %{_bindir}/chage
%attr(4755,root,shadow) %{_bindir}/chfn
%attr(4755,root,shadow) %{_bindir}/chsh
%attr(4755,root,shadow) %{_bindir}/expiry
%attr(4755,root,shadow) %{_bindir}/gpasswd
%{_bindir}/lastlog
%attr(4755,root,root) %{_bindir}/newgrp
%attr(4755,root,shadow) %{_bindir}/passwd
%{_bindir}/sg
%{_sbindir}/groupadd
%{_sbindir}/groupdel
%{_sbindir}/groupmod
%{_sbindir}/grpck
%{_sbindir}/pwck
%{_sbindir}/useradd
%{_sbindir}/userdel
%{_sbindir}/usermod
%{_sbindir}/pwconv
%{_sbindir}/pwunconv
%{_sbindir}/chpasswd
%{_sbindir}/newusers
%{_sbindir}/vipw
%{_sbindir}/vigr
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/useradd.local
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/userdel-pre.local
%verify(not md5 size mtime) %config(noreplace) %{_sbindir}/userdel-post.local
%{_mandir}/man1/chage.1*
%{_mandir}/man1/chfn.1*
%{_mandir}/man1/chsh.1*
%{_mandir}/man1/expiry.1*
%{_mandir}/man1/gpasswd.1*
%{_mandir}/man1/newgrp.1*
%{_mandir}/man1/passwd.1*
%{_mandir}/man1/sg.1*
%{_mandir}/man3/shadow.3*
%{_mandir}/man5/login.defs.5*
%{_mandir}/man8/chpasswd.8*
%{_mandir}/man8/groupadd.8*
%{_mandir}/man8/groupdel.8*
%{_mandir}/man8/groupmod.8*
%{_mandir}/man8/grpck.8*
%{_mandir}/man8/lastlog.8*
%{_mandir}/man8/newusers.8*
%{_mandir}/man8/pwck.8*
%{_mandir}/man8/pwconv.8*
%{_mandir}/man8/pwunconv.8*
%{_mandir}/man8/useradd.8*
%{_mandir}/man8/userdel.8*
%{_mandir}/man8/usermod.8*
%{_mandir}/man8/vigr.8*
%{_mandir}/man8/vipw.8*

%changelog
* Tue Sep 17 2013 kukuk@suse.de
- Add some fixes from Fedora:
  - shadow-4.1.5.1-backup-mode.patch: open backup file with correct
    permissions.
  - shadow-4.1.5.1-logmsg.patch: fix error message
  - shadow-4.1.5.1-errmsg.patch: print error reason
  - shadow-4.1.5.1-manfix.patch: fix manual page
* Tue Feb  5 2013 kukuk@suse.de
- Cleanup login.defs and enable ENCRYPT_METHOD [bnc#802006]
* Tue Nov 13 2012 kukuk@suse.de
- Fix getdef default variables (getdef-new-defs.diff)
* Tue Nov 13 2012 kukuk@suse.de
- Fix default group value in /etc/default/useradd
  (useradd-default.diff)
* Thu Sep 27 2012 kukuk@suse.de
- Implement CHARACTER_CLASS support
  (chkname-regex.diff)
* Wed Sep 26 2012 kukuk@suse.de
- Add support for useradd.local
  (useradd-script.diff)
* Tue Sep 25 2012 kukuk@suse.de
- Fix spec file
- Adjust login.defs
  (shadow-login_defs.diff)
- Add userdel*.local script support and scrips
  (userdel-scripts.diff)
* Mon Sep 24 2012 kukuk@suse.de
- Initial package [FATE#314473]
