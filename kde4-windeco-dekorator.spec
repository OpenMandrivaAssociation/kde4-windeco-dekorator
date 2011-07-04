Name:           kde4-windeco-dekorator
Group:          Graphical desktop/KDE
Summary:        Themable and Customizable Window Decoration Engine for KDE 4
License:        GPL v2 or later
Url:            http://www.kde-look.org/content/show.php?content=87921
Version:        0.5.1
Release:        %mkrel 3.1
Source0:        dekorator-%{version}.tar.bz2
Source1:        elementary-emerald-theme.tar.gz
Source2:        kwindeKoratorrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  phonon-xine curl kdelibs4-devel kdebase4-workspace-devel qimageblitz-devel

%description
Unofficial port of the famous "deKorator" window decoration engine to KDE 4.
You can find themes at http://www.kde-look.org/index.php?xcontentmode=21


Authors:
--------
    Moty Rahamim <moty.rahamim@gmail.com>

%prep
%setup -q -n dekorator-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
rm -rf $RPM_BUILD_ROOT
pushd build
%makeinstall_std
%__tar xf %{SOURCE1}
%__mkdir -p $RPM_BUILD_ROOT/%{_kde_appsdir}/deKorator/themes/
%__cp -r Elementary $RPM_BUILD_ROOT/%{_kde_appsdir}/deKorator/themes/
%__mkdir -p $RPM_BUILD_ROOT/%{_kde_configdir}/
%__cp %{SOURCE2} $RPM_BUILD_ROOT/%{_kde_configdir}/
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG.original COPYING README README.original TODO
%{_kde_libdir}/kde4/kwin3_deKorator.so
%{_kde_libdir}/kde4/kwin_deKorator_config.so
%{_kde_appsdir}/kwin/deKorator.desktop
%{_kde_appsdir}/deKorator/themes/*
%{_kde_configdir}/deKoratorthemes.knsrc
%{_kde_configdir}/kwindeKoratorrc



