Summary:   GTK user interface for comex project
Name:      comex-gtk
Version:   0.1.6.0
Release:   %mkrel 1
License:   GPLv2
#ExcludeArch: ppc64
Group:     Office
Source:    http://comex-project.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL:       http://comex-project.googlecode.com/
BuildArch: noarch
# don't generate debug file because is empty
# % define debug_package %{nil}

BuildRequires: mono
BuildRequires: log4net-devel
BuildRequires: comex-base-devel >= 0.1.8.4
BuildRequires: gtk-sharp2-devel >= 2.8.3
BuildRequires: glade-sharp2 >= 2.8.3
BuildRequires: pkgconfig

Requires: mono
Requires: log4net
Requires: comex-base >= 0.1.8.4
Requires: gtk-sharp2 >= 2.8.3
Requires: glade-sharp2 >= 2.8.3
Requires: glib-sharp2 >= 2.8.3


%description
Is GTK user interface of a simple application that can be used to exchange
data with smartcards using PC/SC standard readers or smartmouse
phoenix serial reader.


%prep
%setup -q

%build
%configure2_5x --libdir=%_prefix/lib 
%make

%install
rm -fr %{buildroot}
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc copying.gpl comex-gtk/readme
%{_bindir}/%{name}
%_prefix/lib/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


