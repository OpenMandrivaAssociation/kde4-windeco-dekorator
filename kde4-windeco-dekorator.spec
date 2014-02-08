Summary:	Themable and Customizable Window Decoration Engine for KDE 4
Name:		kde4-windeco-dekorator
Version:	0.5.1
Release:	14
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde-look.org/content/show.php?content=87921
Source0:	dekorator-%{version}.tar.bz2
Source1:	elementary-emerald-theme.tar.gz
Source2:	kwindeKoratorrc
Patch0:		dekorator-0.5.1-kde4.8-rosa.patch
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	pkgconfig(qimageblitz)
Suggests:	kde4-kwin-dekorator-themes

%description
Unofficial port of the famous "deKorator" window decoration engine to KDE 4.
You can find themes at http://www.kde-look.org/index.php?xcontentmode=21

%files
%doc AUTHORS CHANGELOG.original COPYING README README.original TODO
%{_kde_libdir}/kde4/kwin3_deKorator.so
%{_kde_libdir}/kde4/kwin_deKorator_config.so
%{_kde_appsdir}/kwin/deKorator.desktop
%{_kde_appsdir}/deKorator/themes/*
%{_kde_configdir}/deKoratorthemes.knsrc
%{_kde_configdir}/kwindeKoratorrc

#--------------------------------------------------------------------

%prep
%setup -qn dekorator-%{version}
%apply_patches

%build
%cmake_kde4
%make

%install
pushd build
%makeinstall_std
tar xf %{SOURCE1}
mkdir -p %{buildroot}/%{_kde_appsdir}/deKorator/themes/
cp -r Elementary %{buildroot}/%{_kde_appsdir}/deKorator/themes/
mkdir -p %{buildroot}/%{_kde_configdir}/
cp %{SOURCE2} %{buildroot}/%{_kde_configdir}/
popd

