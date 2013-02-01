Name:		kde4-windeco-dekorator
Version:	0.5.1
Release:	12
Summary:	Themable and Customizable Window Decoration Engine for KDE 4
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde-look.org/content/show.php?content=87921
Source0:	dekorator-%{version}.tar.bz2
Source1:	elementary-emerald-theme.tar.gz
Source2:	kwindeKoratorrc
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	qimageblitz-devel
Suggests:	kde4-kwin-dekorator-themes

%description
Unofficial port of the famous "deKorator" window decoration engine to KDE 4.
You can find themes at http://www.kde-look.org/index.php?xcontentmode=21

%prep
%setup -q -n dekorator-%{version} -a1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
mkdir -p %{buildroot}%{_kde_appsdir}/deKorator/themes/
cp -r Elementary %{buildroot}%{_kde_appsdir}/deKorator/themes/
install -m644 %{SOURCE2} -D %{buildroot}%{_kde_configdir}/

%files
%doc AUTHORS CHANGELOG.original COPYING README README.original TODO
%{_kde_libdir}/kde4/kwin3_deKorator.so
%{_kde_libdir}/kde4/kwin_deKorator_config.so
%{_kde_appsdir}/kwin/deKorator.desktop
%{_kde_appsdir}/deKorator/themes/*
%{_kde_configdir}/deKoratorthemes.knsrc
%{_kde_configdir}/kwindeKoratorrc
