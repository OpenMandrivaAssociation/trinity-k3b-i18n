%bcond clang 1

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif

%define tde_pkg k3b-i18n
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
#define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:			trinity-%{tde_pkg}
Version:		1.0.5
Release:		%{?tde_version:%{tde_version}_}4
Summary:		Internationalization support for TDE [Trinity]
Group:			Applications/Archiving
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


BuildArch:	noarch

# Speed build options
%define debug_package %{nil}
%define __spec_install_post %{nil}
AutoReq: no

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/multimedia/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}
BuildRequires:	desktop-file-utils

BuildRequires:	gettext

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

Requires(post): coreutils
Requires(postun): coreutils

Requires:		trinity-k3b


%description
K3b provides a comfortable user interface to perform most CD/DVD
burning tasks. While the experienced user can take influence in all
steps of the burning process the beginner may find comfort in the
automatic settings and the reasonable k3b defaults which allow a quick
start.

##########

%package Danish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Danish (da) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-da < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-da = %{?epoch:%{epoch}:}%{version}-%{release}

%description Danish
This package contains the Danish translations for K3B.

%files Danish
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/da/k3b
%{tde_prefix}/share/locale/da/LC_MESSAGES/*.mo

##########

%package German
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		German (de) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-de < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-de = %{?epoch:%{epoch}:}%{version}-%{release}

%description German
This package contains the German translations for K3B.

%files German
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/de/k3b
%{tde_prefix}/share/locale/de/LC_MESSAGES/*.mo

##########

%package Greek
Group:			Applications/Archiving
Requires:		trinity-k3b >= %{version}
Summary:		Greek (el) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-el < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-el = %{?epoch:%{epoch}:}%{version}-%{release}

%description Greek
This package contains the greek translations for K3B.

%files Greek
%defattr(-,root,root,-)
#%{tde_prefix}/share/doc/tde/HTML/el/k3b
%{tde_prefix}/share/locale/el/LC_MESSAGES/*.mo

##########

%package Spanish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Spanish (es) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-es < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-es = %{?epoch:%{epoch}:}%{version}-%{release}

%description Spanish
This package contains the Spanish translations for K3B.

%files Spanish
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/es/k3b
%{tde_prefix}/share/locale/es/LC_MESSAGES/*.mo

##########

%package Estonian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Estonian (et) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-et < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-et = %{?epoch:%{epoch}:}%{version}-%{release}

%description Estonian
This package contains the Estonian translations for K3B.

%files Estonian
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/et/k3b
%{tde_prefix}/share/locale/et/LC_MESSAGES/*.mo

##########

%package French
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		French (fr) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-fr < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-fr = %{?epoch:%{epoch}:}%{version}-%{release}

%description French
This package contains the French translations for K3B.

%files French
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/fr/k3b
%{tde_prefix}/share/locale/fr/LC_MESSAGES/*.mo

##########

%package Italian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Italian (it) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-it < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-it = %{?epoch:%{epoch}:}%{version}-%{release}

%description Italian
This package contains the Italian translations for K3B.

%files Italian
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/it/k3b
%{tde_prefix}/share/locale/it/LC_MESSAGES/*.mo

##########

%package Dutch
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Dutch (nl) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-nl < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-nl = %{?epoch:%{epoch}:}%{version}-%{release}

%description Dutch
This package contains the Dutch translations for K3B.

%files Dutch
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/nl/k3b
%{tde_prefix}/share/locale/nl/LC_MESSAGES/*.mo

##########

%package Polish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Polish (pl) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-pl < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-pl = %{?epoch:%{epoch}:}%{version}-%{release}

%description Polish
This package contains the Polish translations for K3B.

%files Polish
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/pl/k3b
%{tde_prefix}/share/locale/pl/LC_MESSAGES/*.mo

##########

%package Portuguese
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Portuguese (pt) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-pt < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-pt = %{?epoch:%{epoch}:}%{version}-%{release}

%description Portuguese
This package contains the Portuguese translations for K3B.

%files Portuguese
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/pt/k3b
%{tde_prefix}/share/locale/pt/LC_MESSAGES/*.mo

##########

%package Brazil
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Brazilian Portuguese (pt_BR) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-pt_BR < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-pt_BR = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:		trinity-k3b-i18n-ptbr < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-ptbr = %{?epoch:%{epoch}:}%{version}-%{release}

%description Brazil
This package contains the Brazilian Portuguese translations for K3B.

%files Brazil
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/pt_BR/k3b
%{tde_prefix}/share/locale/pt_BR/LC_MESSAGES/*.mo

##########

%package Russian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Russian (ru) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-ru < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-ru = %{?epoch:%{epoch}:}%{version}-%{release}

%description Russian
This package contains the Russian translations for K3B.

%files Russian
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/ru/k3b
%{tde_prefix}/share/locale/ru/LC_MESSAGES/*.mo

##########

%package Swedish
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Swedish (sv) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-sv < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-sv = %{?epoch:%{epoch}:}%{version}-%{release}

%description Swedish
This package contains the Swedish translations for K3B.

%files Swedish
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/sv/k3b
%{tde_prefix}/share/locale/sv/LC_MESSAGES/*.mo

##########

%package Ukrainian
Group:			Applications/Archiving
Requires:		trinity-k3b
Summary:		Ukrainian (uk) translations for K3B [Trinity]

Obsoletes:		trinity-k3b-i18n-uk < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:		trinity-k3b-i18n-uk = %{?epoch:%{epoch}:}%{version}-%{release}

%description Ukrainian
This package contains the Ukrainian translations for K3B.

%files Ukrainian
%defattr(-,root,root,-)
%{tde_prefix}/share/doc/tde/HTML/uk/k3b
%{tde_prefix}/share/locale/uk/LC_MESSAGES/*.mo


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"


%install -a
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/af
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ar
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/bg
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/br
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/bs
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ca
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/cs
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/cy
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/en_GB
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/es_AR
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/eu
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/fa
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/fi
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ga
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/gl
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/he
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/hi
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/hu
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/is
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ja
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ka
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/km
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/lt
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/mk
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ms
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/nb
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/nds
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ne
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/nn
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/pa
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/rw
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/se
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/sk
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/sr
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/sr@Latn
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/ta
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/tr
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/uz
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/uz@cyrillic
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/zh_CN
%__rm -rf %{buildroot}%{tde_prefix}/share/locale/zh_TW

